###V1.1.4
import time
import asyncio
import signal
import telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
bot_token = "BOT_TOKEN"
bot = telebot.TeleBot(bot_token) 
chat_id = -1002035404292
cookies = {}
last_text = ""
new_text = ""

url = "https://twitter.com/Pauly0x" 

def main():
    global last_text
    global new_text

    while(True):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.set_window_size(900,1000)
        driver.get(url)
        time.sleep(10)
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        for i in range(1,60):
            driver.get(url)
            time.sleep(10)

            text_el = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span')
            try: 
                text_el = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[3]/div/span')                                 
                new_text = text_el[0].text              
            except IndexError:
                try:
                    text_el = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[2]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span')                                 
                    new_text = text_el[0].text
                except IndexError:
                    print("Index err " + time.localtime )
                    bot.send_message(583851776,f"Index err {time.localtime}")
                    bot.send_message(583851776,f"text_el {text_el}")
            if(new_text != last_text):
                last_text = new_text
                post = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[2]/div/div/article")
                screenshot_filename = 'tweet.png'
                post[0].screenshot(screenshot_filename)
                print("new post")
                photo = open('tweet.png', 'rb')
                #bot.send_photo(chat_id, photo)
                photo.close()
            time.sleep(30)
        driver.close()
def signal_handler(signum, frame):
    print('Received SIGINT, stopping server')
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
asyncio.run(main())