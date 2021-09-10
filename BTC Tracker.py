import requests
import serial
import time
from bs4 import BeautifulSoup

s = serial.Serial('COM3', baudrate=9600)
time.sleep(2)
i = 0

if s.isOpen():
  while (True):
      while i < 1:
          url = 'https://www.google.com/search?&q=bitcoin price in america'
          req = requests.get(url)
          scrap = BeautifulSoup(req.text, 'html.parser')
          bitcoin_price = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
          print(bitcoin_price)
          s.write(bitcoin_price.encode())

  
  
