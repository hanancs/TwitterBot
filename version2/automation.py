from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://twitter.com/login')
 
email = ""
password = ""

login_field = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')

password_field = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

login_button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')

login_field.send_keys(email)
password_field.send_keys(password)

time.sleep(1)

login_button.click()


tweet = "Hello Everyone! This is selenium auomated tweet for testing purposes"


tweetInputField = driver.find_element_by_xpath(
  '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')

tweetInputField.send_keys(tweet)

tweetButton = driver.find_element_by_xpath(
  '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
  
time.sleep(1)

tweetButton.click()