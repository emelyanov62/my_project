import requests
from bs4 import BeautifulSoup
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

responce = requests.get(url)  # получаем данные с сайта
soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
data = soup.find('div', class_='w-full rounded border')  # обращаемся с определенному классу
name = data.find('h4').text  #  обращаемся к тегам в этом классе
name1 = data.find('h5').text  #  обращаемся к тегам в этом классе

      # подставляем сайт
im = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src') #  получаем картинку из этого класса,

print(name + '\n' + name1 + '\n' + im)
