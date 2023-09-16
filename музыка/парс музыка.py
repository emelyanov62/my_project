import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}

def music():
    url = f'https://vk.com/audios350619743?block=recent&section=all'
    resource = requests.get(url, headers=headers)