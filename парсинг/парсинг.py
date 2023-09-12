import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}  # изменяем данные для отправки

for count in range(1, 8):  # парсим все 7 страниц
    time.sleep(5)  # задержка чтоб не блокировали
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    responce = requests.get(url, headers=headers)  # получаем данные с сайта
    soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
    data = soup.find_all('div', class_='w-full rounded border')  # обращаемся с определенному классу

    for counter in data:
        name = counter.find('h4').text  # обращаемся к тегам в этом классе
        name1 = counter.find('h5').text  # обращаемся к тегам в этом классе
        im = 'https://scrapingclub.com' + counter.find('img', class_='card-img-top img-fluid').get(
            'src')  # получаем картинку из этого класса,

        print(name + '\n' + name1 + '\n' + im)

