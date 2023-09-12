import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}  # изменяем данные для отправки

def get():
    for count in range(1, 8): # парсим все 7 страниц
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        responce = requests.get(url, headers=headers)  # получаем данные с сайта
        soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
        data = soup.find_all('div', class_='w-full rounded border')  # обращаемся с определенному классу

        for counter in data: # ссылка на карточку товара
            card = 'https://scrapingclub.com' + counter.find('a').get('href')  # обращаемся с определенному классу и получаем ссылку
                                                                                # на карточки товара
            yield card  # функция генератор


# код начинается с for далее вызывается функция get в нем получаем ссылку card и далее ее обрабатываем
for lis in get():  # вызов функции get
    responc = requests.get(lis, headers=headers)  # получаем данные с сайта
    #time.sleep(3)
    soup = BeautifulSoup(responc.text, 'lxml')  # обрабатываем данные
    #da = soup.find('div', class_='my-8 w-full rounded border').text  # обращаемся с определенному классу
    op = soup.find('p', class_='card-description').text
    name = soup.find('h3').text # обращаемся к тегам в этом классе
    name1 = soup.find('h4').text # обращаемся к тегам в этом классе
    image = 'https://scrapingclub.com' + soup.find('img', class_='card-img-top').get('src')  #  получаем картинку из этого класса

    #print(image)                                                                                    # обязательно подставляем ссылку на сайт
    print(image + '\n' + name + '\n' + name1 + '/n' + op + '/n')