# Bot de Jokenpo para Telegram (Versão Simplificada)

Um bot que usa IA para adivinhar se a sua foto é Pedra, Papel ou Tesoura. O modelo de IA foi treinado com a ferramenta **Teachable Machine**, que gera os arquivos `keras_model.h5` e `labels.txt`.

---
Testador por André Golçalves em 29/09/2025

### Passo 1: Preparar o Ambiente

1.  Garanta que os arquivos `bot_telegram.py`, `keras_model.h5`, e `labels.txt` estejam na mesma pasta.
2.  Abra um terminal nessa pasta e configure os ambiente virtais:

    2.1 Windows:

    ```bash
       configura_venv_windows.bat
    ```
    2.2 Linux:
    ```bash
        configura_conda_linux.sh
    ```

### Passo 2: Obter o Token do Telegram

1.  No Telegram, inicie uma conversa com o **@BotFather**.
2.  Envie o comando `/newbot` e siga as instruções para criar seu bot.
3.  Copie o **token** que o BotFather te fornecer ao final.

### Passo 3: Executar o Bot

1.  Volte ao terminal.
2.  Execute o script com o comando abaixo, substituindo `SEU_TOKEN_AQUI` pelo token que você copiou:
    ```bash
    python bot_telegram.py SEU_TOKEN_AQUI
    ```
3.  Pronto! Encontre seu bot no Telegram e envie uma imagem para testar.
