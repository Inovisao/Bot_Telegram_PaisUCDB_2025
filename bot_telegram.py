from PIL import Image
import os
import logging
import sys
import numpy as np
import random
from tensorflow.keras.models import load_model
from rembg import remove
from rembg.session_factory import new_session
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# --- CONSTANTES E CONFIGURAÇÕES GLOBAIS ---
TOKEN = sys.argv[1] if len(sys.argv) > 1 else None

PASTA_IMAGENS_RECEBIDAS = './Telegram_Imagens_Recebidas/'
PASTA_IMAGENS_PROCESSADAS = './Imagens_Processadas_Sem_Fundo/'
ARQUIVO_MODELO = 'keras_model.h5'
ARQUIVO_LABELS = 'labels.txt'
TAMANHO_IMAGEM = (224, 224)
MODELO_REMBG = "u2netp"

REGRAS_VITORIA = {
    "Pedra": "Tesoura",
    "Tesoura": "Papel",
    "Papel": "Pedra"
}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- FUNÇÕES AUXILIARES ---

def classifica_imagem(imagem_pil, bot_data):
    model = bot_data['modelo_keras']
    nomes_classes = bot_data['nomes_classes']

    data = np.ndarray(shape=(1, TAMANHO_IMAGEM[0], TAMANHO_IMAGEM[1], 3), dtype=np.float32)
    image_resized = imagem_pil.convert("RGB").resize(TAMANHO_IMAGEM, Image.Resampling.NEAREST)
    image_array = np.asarray(image_resized)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data, verbose=0)
    index = np.argmax(prediction)

    return nomes_classes[index], prediction[0][index]


# --- HANDLERS ---

def start(update, context):
    update.message.reply_text('Olá! Envie uma imagem da sua mão (pedra, papel ou tesoura) e eu jogarei Jokenpo com você.')

def help_command(update, context):
    update.message.reply_text('Este bot usa uma IA para reconhecer sua jogada. Apenas envie uma foto!')

def processa_imagem(update, context):
    os.makedirs(PASTA_IMAGENS_RECEBIDAS, exist_ok=True)
    os.makedirs(PASTA_IMAGENS_PROCESSADAS, exist_ok=True)

    try:
        photo_file = update.message.photo[-1].get_file()
        file_path = os.path.join(PASTA_IMAGENS_RECEBIDAS, f"{photo_file.file_id}.jpg")
        photo_file.download(file_path)
        logger.info(f"Processando arquivo: {file_path}")

        imagem_original = Image.open(file_path)

        logger.info("Realizando pré-classificação...")
        classe_inicial, confianca_inicial = classifica_imagem(imagem_original, context.bot_data)
        jogada_inicial = classe_inicial[2:].strip()

        if jogada_inicial == "Nenhum(a)":
            logger.info("Pré-classificação: 'Nenhum(a)'. Processo interrompido.")
            resposta = f'Sua jogada foi classificada como *{jogada_inicial}*. (Confiança: *{confianca_inicial:.2%}*)'
            update.message.reply_text(resposta, parse_mode='Markdown')
            return

        logger.info("Imagem parece válida. Removendo fundo...")
        imagem_sem_fundo = remove(imagem_original, session=context.bot_data['sessao_rembg'])

        nome_base_arquivo = os.path.splitext(os.path.basename(file_path))[0]
        caminho_salvo = os.path.join(PASTA_IMAGENS_PROCESSADAS, f"{nome_base_arquivo}.png")
        imagem_sem_fundo.save(caminho_salvo)
        logger.info(f"Imagem sem fundo salva em: {caminho_salvo}")

        imagem_para_modelo = Image.new("RGB", imagem_sem_fundo.size, (255, 255, 255))
        imagem_para_modelo.paste(imagem_sem_fundo, mask=imagem_sem_fundo.split()[3])

        logger.info("Realizando classificação final...")
        class_name, confidence_score = classifica_imagem(imagem_para_modelo, context.bot_data)
        usuario_jogou = class_name[2:].strip()

        opcoes_validas = [label[2:].strip() for label in context.bot_data['nomes_classes'] if "Nenhum" not in label]
        bot_jogou = random.choice(opcoes_validas)

        if usuario_jogou == bot_jogou:
            resultado = "Resultado: *Empate!* 😐"
        elif REGRAS_VITORIA[usuario_jogou] == bot_jogou:
            resultado = "Resultado: *Você venceu!* 🎉"
        else:
            resultado = "Resultado: *Você perdeu!* 😢"

        resposta = (
            f'Você jogou: *{usuario_jogou}*\n'
            f'O bot jogou: *{bot_jogou}*\n\n'
            f'{resultado}\n\n'
            f'(Confiança da sua jogada: {confidence_score:.2%})'
        )
        update.message.reply_text(resposta, parse_mode='Markdown')

    except Exception as e:
        logger.error(f"Ocorreu um erro inesperado: {e}", exc_info=True)
        update.message.reply_text("Desculpe, ocorreu um erro ao processar sua imagem.")

# --- FUNÇÃO PRINCIPAL ---

def main():
    if not TOKEN:
        logger.critical("ERRO: O token do bot não foi fornecido na linha de comando.")
        sys.exit(1)

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    try:
        logger.info("Carregando modelos de IA...")
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        dispatcher.bot_data['modelo_keras'] = load_model(ARQUIVO_MODELO, compile=False)
        with open(ARQUIVO_LABELS, 'r', encoding='utf-8') as f:
            dispatcher.bot_data['nomes_classes'] = f.readlines()
        dispatcher.bot_data['sessao_rembg'] = new_session(model_name=MODELO_REMBG)

        logger.info("Modelos carregados com sucesso.")
    except FileNotFoundError:
        logger.critical(f"ERRO: Arquivo de modelo '{ARQUIVO_MODELO}' ou de labels '{ARQUIVO_LABELS}' não encontrado.")
        sys.exit(1)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.photo, processa_imagem))

    logger.info("Bot configurado e pronto para receber mensagens.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
