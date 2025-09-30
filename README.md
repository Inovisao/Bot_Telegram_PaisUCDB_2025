# 📌 Bot de Classificação de Imagens com IA no Telegram  

Este projeto implementa um bot no **Telegram** que utiliza um modelo de **IA treinado no Teachable Machine** (ou outro modelo Keras) para **classificar imagens enviadas pelos usuários**.  

O bot retorna:  
- 📷 **Classe identificada** (de acordo com o arquivo `labels.txt`).  
- 📊 **Confiabilidade (probabilidade)** da predição.  

---

## 🚀 Estrutura do Projeto  

```
├── configura_ambiente_linux/          # Script único para Linux
│   └── configura_ambiente_linux.sh
├── configura_ambiente_windows/        # Scripts para Windows
│   ├── configura_miniconda_windows.bat
│   └── instala_dependencias_windows.bat
├── bot_telegram.py                    # Código principal do bot
├── keras_model.h5                     # Modelo treinado (Keras/TensorFlow)
├── labels.txt                         # Lista de classes do modelo
├── requirements.txt                   # Dependências do projeto
├── README.md                          # Esta documentação
```

### 📲 Criação do Bot no Telegram  
1. Instale o **Telegram** no celular.  
2. Procure pelo usuário **@BotFather**.  
3. Envie `/newbot` e siga as instruções:  
   - Defina um **nome**.  
   - Defina um **username** (ex.: `meu_bot_ia`).  
4. Copie o **token** fornecido.  
   > Você usará esse token para executar o bot.  

---

### ⚙️ Instalação do Ambiente Virtual (Conda)  

- Baixe ou clone este repositório no seu computador.  

#### 🔹 No Windows  
- **Passo 1:** Instale o **Miniconda** (caso ainda não tenha):  
   ```bash
   configura_miniconda_windows.bat
   ```  
- **Passo 2:** Crie o ambiente e instale as dependências:  
   ```bash
   instala_dependencias_windows.bat
   ```  

#### 🔹 No Linux  
Execute o script único que prepara tudo automaticamente:  
```bash
./configura_ambiente_linux.sh
```  

---

### ▶️ Executar o Bot  
1. Certifique-se de que os arquivos `keras_model.h5` e `labels.txt` estão na mesma pasta do bot.  
   - Estrutura do `labels.txt`:  
     ```
     0 "Classe1"
     1 "Classe2"
     2 "Classe3"
     ```  
2. Ative o ambiente Conda criado pelo script.  
3. No terminal, rode:  
   ```bash
   python bot_telegram.py SEU_TOKEN_AQUI
   ```  
4. Abra o **Telegram**, encontre seu bot e envie **qualquer imagem**.  
5. O bot vai responder com:  
   - ✅ Nome da classe prevista.  
   - 📊 Confiança da predição (em %).  

---

## 📦 Dependências  
O projeto utiliza as seguintes bibliotecas principais:  
- `python-telegram-bot`  
- `tensorflow`  
- `pillow`  
- `numpy`  

> Todas as dependências já estão listadas em `requirements.txt`.  

---

🔬 Projeto testado por **André Gonçalves** em 29/09/2025.  
