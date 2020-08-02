from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver

driver_path = 'C:/games/chromedriver'
web_driv = webdriver.Chrome(executable_path = driver_path)
search_url = "https://myanimelist.net/animelist/Shishere?status=2"
web_driv.get(search_url)

url = web_driv.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(url,'html.parser')

for anime_name , anime_tag , anime_type1 in zip(soup.find_all("td",class_='data title clearfix'),soup.find_all('td', class_='data progress'),soup.find_all('td', class_='data type')):
    #print(anime_name.a.text)
    #print(anime_type1.text)
    tag1=anime_tag.div['class']
    tag=tag1[0].split('-')[1]
    
    anime_url = requests.get(f'https://myanimelist.net/anime/{tag}/{anime_name.a.text}')
    soup1 = BeautifulSoup(anime_url.content , 'html.parser')
    episodes = soup1.find('div', class_="spaceit").text.split('\n  ')[1]
    #print(episodes)
    for dur in soup1.find_all('div', class_="spaceit"):
        if(dur.span.text=='Duration:'):
            #print(dur.text.split('\n  ')[1])
            duration = dur.text.split('\n  ')[1]
            break 
            
    print(anime_name.a.text,anime_type1.text,episodes,duration)
