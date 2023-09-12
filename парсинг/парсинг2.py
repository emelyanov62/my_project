import requests
from bs4 import BeautifulSoup

cou = 0
for count in range(1, 8): # парсим все 7 страниц
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    responce = requests.get(url)  # получаем данные с сайта
    soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
    data = soup.find_all('div', class_='w-full rounded border')  # обращаемся с определенному классу


    for counter in data:
        cou += 1
        name = counter.find('h4').text  # обращаемся к тегам в этом классе
        name1 = counter.find('h5').text  # обращаемся к тегам в этом классе
        im = 'https://scrapingclub.com' + counter.find('img', class_='card-img-top img-fluid').get(
            'src')  # получаем картинку из этого класса,

        print(name + '\n' + name1 + '\n' + im)

print(cou)