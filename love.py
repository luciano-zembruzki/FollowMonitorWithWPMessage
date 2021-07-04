from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random
import os
import wget
from gtts import gTTS
from io import BytesIO
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
from pywhatkit import pywhatkit


phrases = [
'Sabe quando você quer que um momento dure para sempre? Então, é assim quando estou com você.',
'Você é o maior presente que Deus poderia me dar. Te amo hoje e sempre!',
'Eu te amo. E nunca me imaginaria amando alguém com tanta intensidade, nem sabia que tinha tanta capacidade pra amar assim.',
'Minha felicidade não tem preço, tem o seu nome.',
'Não dá para negar, é você, tem sido você e vai continuar sendo você... Minha escolha, minha certeza, meu amor.',
'Amo seu jeito, seu riso, seu tudo e até as imperfeições eu amo em você!',
'Um dia me perguntaram "O que você viu nela?" e eu respondi "O que faltava em mim!"',
'Te amo. Com todas as letras, palavras e pronúncias. Em todas as línguas e sotaques. Em todos os sentidos e jeitos. Simplesmente, te amo.',
'Eu não preciso de mil motivos para sorrir, você já é o suficiente.',
'Meu amor, você é o que tenho de mais especial e nem consigo imaginar minha vida sem ser ao seu lado.',
'O mundo é uma verdadeira imensidão e nunca consegui achar alguém tão especial como você!',
'O tempo passa e o meu amor por você só aumenta a cada dia.',
'Pra nós, todo o amor do mundo.',
'Eu nunca me cansarei de dizer que é você quem eu amo, e é o seu lado que eu quero acordar todos os dias.',
'Todos vivem por uma razão, a minha é você.',
'De qualquer jeito seu sorriso vai ser meu raio de sol.',
'Você é realmente a razão da minha vida.',
'Por sua causa, eu tenho lindos sonhos para sonhar. Por sua causa, minha vida está cheia de amor.',
'Com você, o meu mundo é melhor.',
'Naquele dia que você me olhou. Me balançou por dentro, me virou o mundo! Percebi, tinha que ser você.',
'Não é exagero dizer que você me roubou no momento em que me olhou.',
'E se eu puder fazer por ti o que ninguém jamais fez por mim, eu faço!',
'Você chegou do nada para ser meu tudo!',
'Sem você, eu posso tudo, menos ser feliz!',
'Eu preciso dizer que eu te amo, te ganhar ou perder sem engano.',
'Eu quero colo, eu quero carinho. E meu carinho eu quero te dar!'
]


def text_to_speech(text):
    print("Enviando mensagem....")
    mp3_fp = BytesIO()
    Message = text
    speech = gTTS(text = Message, lang='pt')
    speech.save('mp3_fp.mp3')
    playsound('mp3_fp.mp3')

browser = webdriver.Chrome("./chromedriver")

browser.get("http://instagram.com")

username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.send_keys("<SEU USER>")
password.send_keys('<SUA SENHA>')

submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

submit.click()

not_now = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

not_now.click()
not_now2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))

not_now2.click()

stop = 0
last_followers_count = 0
while stop == 0:
    browser.get('https://www.instagram.com/python_simplificado/')
    followers_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))
    if last_followers_count > 0:
        print("Você tinha {} seguidores".format(followers_count))
    followers_count = int(followers_element.text)
    print("Você tem agora {} seguidores".format(followers_count))
    if (followers_count > last_followers_count) and (last_followers_count > 0) :
        text_to_speech("Novo seguidor! Vou enviar mensagem para Gabriela")
        pywhatkit.sendwhatmsg_instantly("+5511111111111", str(random.choice(phrases)), 30, False)
    last_followers_count = followers_count
    sleep(2)

