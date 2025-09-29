@echo off
echo ==========================================
echo Instalando miniconda
echo ==========================================

REM Criar ambiente virtual com venv nativo
python -m venv bot_telegram

REM Ativar ambiente
call bot_telegram\Scripts\activate.bat

REM Atualizar pip
python -m pip install --upgrade pip

REM Instalar dependencias
pip install -r requirements.txt

echo ==========================================
echo Ambiente configurado com sucesso!
echo Agora execute:
echo     bot_telegram\Scripts\activate
echo     python bot_telegram.py SEU_TOKEN_AQUI
echo ==========================================
pause
