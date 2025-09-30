# 📌 Bot de Jokenpô com IA no Telegram

Este projeto implementa um bot no **Telegram** que joga **Pedra ✊, Papel ✋ ou Tesoura ✌** com você.  
O bot usa uma **IA treinada no Teachable Machine**, capaz de classificar imagens enviadas pelos usuários.

---

## 🚀 Estrutura do Projeto

```
├── configura_ambiente_linux/          # Script único para Linux
│   └── configura_ambiente_linux.sh
├── configura_ambiente_windows/        # Scripts para Windows
│   ├── configura_miniconda_windows.bat
│   └── instala_dependencias_windows.bat
├── bot_telegram.py                    # Código principal do bot
├── requirements.txt                   # Dependências do projeto
├── README.md                          # Esta documentação
```

### Criação do Bot no Telegram
1. Instale o **Telegram** no celular.  
2. Procure pelo usuário **@BotFather**.  
3. Envie `/newbot` e siga as instruções:  
   - Defina um **nome**.  
   - Defina um **username** (ex.: `jokenpo_bot`).  
4. Copie o **token** fornecido.  
   > Você usará esse token para executar o bot.

---

### 3️⃣ Instalação do Ambiente Virtual (Conda)

- Baixe ou clone esse repositório no seu computador

#### 🔹 No Windows
- **Passo 1:** Instale o **Miniconda** (caso ainda não tenha):  
   ```bash
   configura_ambiente_windows\configura_miniconda_windows.bat
   ```

- **Passo 2:** Crie o ambiente e instale as dependências:  
   ```bash
   configura_ambiente_windows\instala_dependencias_windows.bat
   ```

---

#### 🔹 No Linux
Execute o script único que prepara tudo automaticamente:  
```bash
./configura_ambiente_linux/configura_ambiente_linux.sh
```

---

### 4️⃣ Executar o Bot
1. Certifique-se de que os arquivos `keras_model.h5` e `labels.txt` estão na mesma pasta do bot.  
2. Ative o ambiente Conda criado pelo script.  
3. No terminal, rode:  
   ```bash
   python bot_telegram.py SEU_TOKEN_AQUI
   ```
4. Abra o **Telegram**, encontre seu bot e envie uma **foto da sua mão** (Pedra, Papel ou Tesoura).  
5. O bot vai:
   - Classificar sua jogada.
   - Fazer uma jogada aleatória.
   - Informar quem ganhou.

--- 

## 📦 Dependências
O projeto utiliza as seguintes bibliotecas principais:
- `python-telegram-bot`
- `tensorflow`
- `pillow`
- `rembg`
- `numpy`

> Todas elas já estão listadas em `requirements.txt`.

---
- Testado por **André Gonçalves** em 29/09/2025.  
