import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.google.com/search?q=inception+movie+duration")    ##Jus need to put the movie name in place of inception

soup = BeautifulSoup(page.content)

article= soup.find("div", attrs={'id': 'main'})

dur=soup.find("div",attrs={'class':'BNeawe tAd8D AP7Wnd'}).text

duration=dur.split('‧')[2]    ##Gives the duration of the movie

Movie_category=dur.split('‧')[1]  ##gives the genre/category
