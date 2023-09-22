import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}  # изменяем данные для отправки

# Загрузить веб-страницу
url = "https://muzofond.fm"

# Проверить, был ли успешный запрос к веб-серверу
def start():
    tot = int(input('цифра: '))
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('ul', class_='menu-box')
    ad = data.find_all('a')
    first_element = ad[tot]
    card = first_element.get('href')

    if tot == 0:
        ne = 'https://muzofond.fm/collections/new/%D0%' \
             'BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%BA%D0%B8%20%D0%' \
             'B8%20%D1%85%D0%B8%D1%82%D1%8B%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8'
        responc = requests.get(ne, headers=headers)
        soup= BeautifulSoup(responc.text, 'lxml')
        data = soup.find('li', class_='play')['data-url']
        #first_element = ad[tot]
        #card = first_element.get('href')

        print(data)

start()


