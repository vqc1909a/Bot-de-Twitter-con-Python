#Webdrive es para que te abra un navegador especifico como Firefox, Edge, Chrome cuando le des una URL

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

email_twitter = os.environ['email_twitter']
password_twitter = os.environ['password_twitter']

class TwitterBot:
     def __init__(self, username, password):
          self.username = username
          self.password = password
          self.bot = webdriver.Firefox()
     
     def login(self):
          bot = self.bot;     
          bot.get('https://twitter.com/login')
          #ESTO NO ES NECESARIO PORQUE VA A ESPERAR QUE CARGUE LA PAGINA Y TE ESPERA 5 SEGUNDOS
          time.sleep(5)
          #Webdriver puede buscar elementos html desde su id, clase o name como los inputs
          email = bot.find_element_by_name('session[username_or_email]')
          password = bot.find_element_by_name('session[password]')
          email.clear()
          password.clear()
          email.send_keys(self.username)
          password.send_keys(self.password)
          password.send_keys(Keys.ENTER)
          time.sleep(5)

     def like_tweet(self, hashtag):
          bot = self.bot
          bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
          time.sleep(5)

          for i in range(0,1):
               #cada vez que bajes va a encontrar imagenes de los tweets que contiene las urls que te dirigin a sus tweets pra que le des corazon
               bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
               time.sleep(5)
               tweets = bot.find_elements_by_css_selector("a.css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1ny4l3l")

               links = []
               for tweet in tweets:
                    if("status" in tweet.get_attribute('href')):
                         links.append(tweet.get_attribute('href'))

               for link in links:
                    bot.get(link)
                    time.sleep(3)
                    try:
                         iconos = bot.find_elements_by_class_name("css-18t94o4")
                         for icono in iconos:
                             if(icono.get_attribute('aria-label') == "Me gusta"):
                                   icono.click()
                         time.sleep(5)
                    except Exception as ex:
                         time.sleep(10)
          

ed = TwitterBot(email_twitter, password_twitter)

ed.login()
ed.like_tweet("web development")

