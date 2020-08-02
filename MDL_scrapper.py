from bs4 import BeautifulSoup
import requests

url = requests.get('https://mydramalist.com/dramalist/7509375') 
soup = BeautifulSoup(url.content,'html.parser')

i=[4,84]

for names,id,j in zip(soup.find_all('a',class_="title text-primary _600"),soup.find_all('tr'),range(100)):
    if(j>=i[0]):
        name = names.text.replace(' ','-')
        #print(name)
        link =names['href']
        tag = id['id'].split('ml')[1]
        search_url = requests.get(f'https://mydramalist.com{link}')
        soup1 = BeautifulSoup(search_url.content , 'html.parser')
        for info in soup1.find('ul', class_='list m-b-0').find_all('li'):
            if(info.b.text=='Drama:'):
                Series =info.span.text
            if(info.b.text=='Movie:'):
                Series=info.span.text
            if(info.b.text=='Special:'):
                Series=info.span.text
            if(info.b.text=='Country:'):
                Country=info.text.split(': ')[1]
            if(info.b.text=='Episodes:'):
                Episodes=info.text.split(': ')[1]
            if(info.b.text=='Duration:'):
                Duration=info.text.split(': ')[1]
        try:
            print(f"{Series},{Country},{Episodes},{Duration}")
        except:
            continue 
                       
        if(j>=i[1]):
            break  
            
    
