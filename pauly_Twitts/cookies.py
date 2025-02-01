
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://twitter.com/Pauly0x')
# Здесь происходит вход в систему
cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)