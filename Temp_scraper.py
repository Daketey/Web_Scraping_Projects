import serial
import requests
from bs4 import BeautifulSoup
import time

serialPort = serial.Serial(port = "COM8", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

page = requests.get("https://weather.com/en-IN/weather/today/l/c66381d31d49569685d988b25abde35ecc58748aea8dbf608290fa7b2bb13780")

soup = BeautifulSoup(page.content, "lxml")
article= soup.find('main')

while True:
    page = requests.get("https://weather.com/en-IN/weather/today/l/c66381d31d49569685d988b25abde35ecc58748aea8dbf608290fa7b2bb13780")
    soup = BeautifulSoup(page.content, "lxml")
    article= soup.find('main')
    headline = article.h1.text
    headplace = headline.split(',')[0]
    headstate = headline.split(',')[1]
    head = f'{headplace},{headstate}'
    print(head)
    timeist = soup.find('div',class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--timestamp--1ybTk').text
    timeist= timeist.split('f')[1]
    print(timeist)
    temp = soup.find('span', class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY').text
    temp = str(temp.replace("°",""))
    temp=str(180-int(temp))
    print("X"+temp)
    newtemp = "X"+temp
    serialPort.write(str.encode(newtemp))
    cond = soup.find('div',class_='_-_-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--mZC_p').text
    print(cond)
    time.sleep(30)
                        
