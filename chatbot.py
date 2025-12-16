import nltk
import numpy as np
import string
import warnings

import requests
import json

############################################


import telegram
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

############################################
import datetime
import pytz

import random
warnings.filterwarnings("ignore")


# From scikit learn library, import the TFidf vectorizer to convert a collection of raw documents to a matrix of TF-IDF features.
from sklearn.feature_extraction.text import TfidfVectorizer
# Also, import cosine similarity module from scikit learn library
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords


f = open('content.txt','r', encoding = 'utf-8')
paragraph = f.read()
nltk.download('stopwords')
nltk.download('punkt')   # for first-time use only. Punkt is a Sentence Tokenizer
nltk.download('wordnet')    # for first-time use only. WordNet is a large lexical database of English.
sent_tokens = nltk.sent_tokenize(paragraph)
word_tokens = nltk.word_tokenize(paragraph)


cumprimento = ['Ola','ola','oi','oie','Oie','OIE','OI','Oi','Bom dia','Olá', 'Olá! 😊 Como posso ajudá-lo hoje?']
xau_response = ['Xau','Xau','Tenha um ótimo dia','Tenha um otimo dia']
agradecimento = ['Obrigada', 'Obrigada']
agradecimento_response = ['Seja bem vindo' , 'Sem problemas']
hora=['Qual a Hora','Qual a hora?', 'Que dia é hoje?']
animacao=['kkkkkkkk','kakakakak','kakakak','kakaka','Kakaka','Jkakaka']
animacao_response=['kkkkkkkk','se riu é porque é nerd','kakakakak','kakakak','kakaka','Kakaka']
error=['encontrou algum erro?', 'desculpe, entre em contato para que possamos resolver!']
inicio=[' Ola, Sou o Bot Rata 🐭\n Estamos aqui para te ajudar a encontrar as informações rápidas sobre a Fatec Ribeirão Preto 🚀 \n Digite Rata a qualquer momento e voltará ao menu principal \n⚡ Informações + rapidas sobre a sala de aula: \n // Digite Nome da disciplina e nome do professor \n/cursos \n/secretaria \n/eventos \n/matricula \n/humor.']
nome=['Como se chama?','Qual seu nome']
nome_response=[' Ola, Sou o Bot Rata da Fatec 🐭']
saudacao=['Tudo bem?','Como vc esta?']
saudacao_response=['Sou um bot, todos os dias são maravilhosos']


# Lemmitization
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]   
    
    
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def Normalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
  


def response(user_response):
    robo_response = 'SEU_TOKEN_AQUI'
    stopwords = nltk.corpus.stopwords.words('portuguese')
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Normalize, stop_words=stopwords)
    tfidf = TfidfVec.fit_transform(sent_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]

    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]


    if (req_tfidf == 0):
        robo_response = robo_response + "Me Desculpe, não entendi sua pergunta!, \n Escreva Fatec para começar."
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]    # return the sentences at index -2 as answer
        return robo_response   


def bot_initialize(user_msg):
        flag=True
        while(flag==True):
            user_response = user_msg
          # If bot_response is empty, get a response from OpenAI
            if(user_response not in xau_response):
                if(user_response == '/start'):
                    bot_resp = random.choice(inicio)
                    return bot_resp
                elif(user_response == '/humor'):
                    bot_resp =  """O que um nerd fala quando toma vacina?"""
                    return bot_resp
                elif(user_response =='Não sei'):
                    bot_resp = """As Definições de Virus foram atualizadas"""
                    return bot_resp
                elif(user_response in hora):
                    tz = pytz.timezone('America/Sao_Paulo')  # Definir o fuso horário desejado
                    now = datetime.datetime.now(tz)
                    time = now.strftime("%H:%M:%S")
                    date = now.strftime("%d/%m/%Y")
                    bot_resp = f"A hora atual é {time} e a data atual é {date}."
                    return bot_resp
                elif(user_response in agradecimento):
                    bot_resp = random.choice(agradecimento_response)
                    return bot_resp
                elif(user_response in cumprimento):
                    bot_resp = random.choice(cumprimento) 
                    return bot_resp
                elif user_response in animacao:
                    bot_resp = random.choice(animacao_response)
                    return bot_resp
                elif user_response in saudacao:
                    bot_resp = random.choice(saudacao_response)
                    return bot_resp
                else:
                    user_response = user_response.lower()
                    bot_resp = response(user_response)
                    sent_tokens.remove(user_response)   
                    return bot_resp
            else:
                flag = False
                bot_resp = random.choice(xau_response)
                return bot_resp
            

class telegram_bot():
    def __init__(self):
        self.token =  ""    #write your token here!
        self.url = f"https://api.telegram.org/bot{self.token}"
    def get_updates(self,offset=None):
            url = f"{self.url}/getUpdates?timeout=60"    # In 100 seconds if user input query then process that, use it as the read timeout from the server
            if offset:
                 url = f"{url}&offset={offset+1}"
            url_info = requests.get(url)
            return json.loads(url_info.content)
    def send_message(self,msg,chat_id):
            url = f"{self.url}/sendMessage?chat_id={chat_id}&text={msg}"
            if msg is not None:
                requests.get(url)


tbot = telegram_bot()
update_id = None

def make_reply(msg):     # user input will go here
    if msg is not None:
      reply = bot_initialize(msg)     # user input will start processing from bot_initialize function
      return reply
      
while True:
    print("...")
    updates = tbot.get_updates(offset=update_id)
    updates = updates['result']
    print(updates)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            print(update_id)
            try:
                message = item["message"]["text"]
                print(message)
            except:
                message = None
            from_= item["message"]["from"]["id"]
            print(from_)
            reply = make_reply(message)
            tbot.send_message(reply, from_)
