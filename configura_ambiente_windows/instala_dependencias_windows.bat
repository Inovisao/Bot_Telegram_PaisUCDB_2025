@echo off
echo ==========================================
echo Configurando ambiente para o Bot Telegram
echo ==========================================


call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2




REM Criar ambiente conda (se não existir)
call conda create -n bot_telegram python=3.10 -c conda-forge -y
REM Instalar dependências dentro do ambiente
echo Ambiente criado! Instalando bibliotecas
call conda activate bot_telegram
call python -m pip install -r requirements.txt


echo ==========================================
echo O ambiente está ativado, para testar rode o codigo abaixo!
echo python bot_telegram.py
echo ==========================================



