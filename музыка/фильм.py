from bs4 import BeautifulSoup
import requests
import telebot

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')



@bot.message_handler(commands=['start'])
def start(mes):
    bot.send_message(mes.chat.id,
                 "Привет! Я музыкальный бот. Отправь мне название исполнителя или трека")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.0.0 Safari/537.36'}
    #query = start.text
    url = f'https://vk.com/audios350619743?block=new_songs'
    recponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(recponse.text, 'lxml')
    #data = soup.find('div', class_='CatalogBlock__itemsContainer audio_page__audio_rows_list _audio_page__audio_rows_list _audio_pl audio_w_covers ')

    youtube = soup.find('div', class_='audio_row__title _audio_row__title')
    youtube_link = youtube.find_all('a', {'onmouseover': 'setTitle'})

    song_url = youtube_link('href')
    for count in song_url:
        print(count.text.strip())
        #bot.send_audio(start.chat.id, link)



bot.infinity_polling()

