# Bot_Telegram_Pais_UCDB

Este é um bot para Telegram que utiliza um modelo de Inteligência Artificial para classificar imagens de Pedra, Papel e Tesoura (Jokenpo). Ao enviar uma foto, o bot responderá com a classificação e a confiança da predição.

## Pré-requisitos

* Python 3.x instalado em seu sistema.

## Passo a Passo para Utilização

Siga as etapas abaixo para configurar e executar o bot em sua máquina.

### 1. Organize os Arquivos

Certifique-se de que os seguintes arquivos estejam na mesma pasta do projeto:
* `bot_telegram.py`
* `keras_model.h5`
* `labels.txt`

### 2. Instale as Dependências

Abra seu terminal ou prompt de comando na pasta do projeto e instale as bibliotecas Python necessárias. Execute o seguinte comando:

```bash
pip install pillow numpy tensorflow python-telegram-bot
