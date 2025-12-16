## 🤖 ChatBot Telegram em Python – Bot Rata 🐭

Este projeto consiste no desenvolvimento de um **chatbot em Python para o Telegram**, utilizando técnicas básicas de **Processamento de Linguagem Natural (PLN)** com **NLTK** e **TF-IDF**, voltado para fornecer informações sobre **horários de aula da FATEC Ribeirão Preto**.

O bot é capaz de responder perguntas com base em um arquivo de conteúdo (`content.txt`), além de lidar com comandos, saudações, humor e informações dinâmicas como **data e hora**.

---

## 🚀 Funcionalidades

- 📚 Respostas automáticas baseadas em similaridade de texto (**TF-IDF + Cosine Similarity**)
- 💬 Reconhecimento de:
  - Saudações  
  - Agradecimentos  
  - Humor
    
- ⏰ Retorno de **data e hora atual** (fuso horário de São Paulo)
- 📄 Base de conhecimento carregada via arquivo `content.txt`
- 🤖 Integração direta com a **API do Telegram**
- 🧠 Uso de **NLTK** para tokenização, lematização e remoção de stopwords

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- Telegram Bot API  
- NLTK  
- Scikit-learn  
- NumPy  
- Requests  
- Pytz  

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as dependências:

```bash
pip install -r requirements.txt
````

## Configuração
### Token do Telegram

Crie um bot no Telegram usando o @BotFather e obtenha o token.
export TELEGRAM_TOKEN="SEU_TOKEN_AQUI"


E no código:

import os
self.token = os.getenv("TELEGRAM_TOKEN")


### Base de Conhecimento

Edite o arquivo content.txt com as informações que o bot deverá usar para responder perguntas
(ex: cursos, professores, secretaria, eventos, horários).

### Execução

Para iniciar o bot:
```bash
python bot.py
``` 

O bot ficará em execução contínua, aguardando mensagens no Telegram.

## Como o Bot Funciona

O texto do usuário é normalizado:

- Conversão para minúsculas

- Remoção de pontuação

- Tokenização

- Lematização

As frases do content.txt são vetorizadas com TF-IDF

A resposta é escolhida pela maior similaridade de cosseno

Caso não haja similaridade suficiente, o bot retorna uma mensagem padrão de erro


### Exemplos de Comandos

- /start → Menu inicial

- /humor → Piada nerd 🤓

- Qual a hora? → Retorna data e hora

- Oi, Olá → Saudação

- kkkkk → Resposta divertida





