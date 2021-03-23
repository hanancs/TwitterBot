from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitterbot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login/')
        time.sleep(1) 
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self_username)
        password.send_keys(self.password)

ed = Twitterbot('benhanandavid@gmail.com','balumahendra')
ed.login()