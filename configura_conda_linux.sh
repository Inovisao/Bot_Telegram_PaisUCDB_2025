#!/bin/bash
echo "=========================================="
echo " Configurando ambiente para o Bot Telegram"
echo "=========================================="

# Criar ambiente conda
conda create -n bot_telegram python==3.10 -y

# Ativar ambiente
source ~/anaconda3/etc/profile.d/conda.sh 2>/dev/null || source ~/miniconda3/etc/profile.d/conda.sh
conda activate bot_telegram

# Instalar dependências
pip install -r requirements.txt

echo "Ambiente configurado com sucesso"
