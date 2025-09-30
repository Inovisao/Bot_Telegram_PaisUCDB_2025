"""
Bot do Telegram para classificar imagens com IA.
Retorna apenas a classe prevista e a confiabilidade.
"""

# --- IMPORTAÇÃO DAS BIBLIOTECAS ---
from PIL import Image
import os
import logging
import sys
import numpy as np
from tensorflow.keras.models import load_model
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# --- CONFIGURAÇÕES GLOBAIS ---
TOKEN = sys.argv[1] if len(sys.argv) > 1 else None

ARQUIVO_MODELO = 'keras_model.h5'
ARQUIVO_LABELS = 'labels.txt'
TAMANHO_IMAGEM = (224, 224)

# --- CONFIGURAÇÃO DO LOGGING ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# --- FUNÇÃO DE CLASSIFICAÇÃO ---
def classifica_imagem(imagem_pil, context):
    """Prepara e classifica uma imagem usando o modelo Keras."""
    model = context.bot_data['modelo_keras']
    nomes_classes = context.bot_data['nomes_classes']

    # Pré-processamento
    data = np.ndarray(shape=(1, TAMANHO_IMAGEM[0], TAMANHO_IMAGEM[1], 3),
                      dtype=np.float32)
    image_resized = imagem_pil.convert("RGB").resize(TAMANHO_IMAGEM, Image.Resampling.NEAREST)
    image_array = np.asarray(image_resized)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predição
    prediction = model.predict(data, verbose=0)
    index = np.argmax(prediction)

    # Extrai apenas o nome da classe do labels.txt
    classe = nomes_classes[index].strip().split(" ", 1)[1].replace('"', '')

    return classe, prediction[0][index]

# --- HANDLERS ---
async def start(update, context):
    await update.message.reply_text('Olá! Envie uma imagem e eu direi a classe que identifiquei.')

async def processa_imagem(update, context):
    try:
        # Baixa a foto
        photo_file = await update.message.photo[-1].get_file()
        file_path = f"{photo_file.file_id}.jpg"
        await photo_file.download_to_drive(file_path)

        imagem = Image.open(file_path)
        classe, confianca = classifica_imagem(imagem, context)

        resposta = f"Classe identificada: *{classe}*\nConfiança: *{confianca:.2%}*"
        await update.message.reply_text(resposta, parse_mode='Markdown')

    except Exception as e:
        logger.error(f"Erro: {e}", exc_info=True)
        await update.message.reply_text("Erro ao processar a imagem.")

# --- MAIN ---
def main():
    if not TOKEN:
        logger.critical("Token do bot não fornecido.")
        sys.exit(1)

    application = Application.builder().token(TOKEN).build()

    try:
        logger.info("Carregando modelo e labels...")
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        application.bot_data['modelo_keras'] = load_model(ARQUIVO_MODELO, compile=False)

        with open(ARQUIVO_LABELS, 'r', encoding='utf-8') as f:
            application.bot_data['nomes_classes'] = f.readlines()

        logger.info("Modelos carregados.")
    except FileNotFoundError:
        logger.critical("Modelo ou labels não encontrados.")
        sys.exit(1)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, processa_imagem))

    logger.info("Bot pronto.")
    application.run_polling()

if __name__ == '__main__':
    main()
