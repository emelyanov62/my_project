import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}  # изменяем данные для отправки

# Загрузить веб-страницу
url = "https://muzofond.fm"

# Проверить, был ли успешный запрос к веб-серверу

responce = requests.get(url, headers=headers)
# получаем данные с сайта
soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
data = soup.find('div', class_='burger_menu boxShadow')
ad = data.find_all('a')
# обращаемся с определенному классу

print(ad)
#print(data.text)
#print(responce.text)

