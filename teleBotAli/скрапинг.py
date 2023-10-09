import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/116.0.0.0 Safari/537.36'}  # изменяем данные для отправки

def get():
    url = 'https://aliexpress.ru/item/1005006060501854.html?sku_id=12000035648928421&spm=a2g2w.' \
          'productlist.search_results.1.44c51a33Nv1JRw'
    resource = requests.get(url, headers=headers)
    soup = BeautifulSoup(resource.text, 'lxml')
    data = soup.find('div', class_='SnowProductGallery_'
                                       'SnowProductGallery__previews__jy810')
    img_tag = data.find_all('img')
    for count in img_tag:
        image_url = count['src']
        print(image_url)
    description_element = soup.find('h1', class_='snow-ali-kit_Typography__base__1shggo '
                                                 'snow-ali-kit_Typography-Primary__base__1xop0e '
                                                 'snow-ali-kit_Typography__strong__1shggo '
                                                 'snow-ali-kit_Typography__sizeHeadingL__1shggo '
                                                 'HazeProductDescription_HazeProductDescription__name__1bnud '
                                                 'HazeProductDescription_HazeProductDescription__smallText__1bnud')
    print(description_element.text)

get()