import telebot
import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
# Замените 'YOUR_GENIUS_API_KEY' на ваш ключ API Genius
bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')
lastfm_api_key = '1778d48da99e2ba93b111ebf1d4700fb'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я музыкальный бот. Отправь мне название исполнителя или трека, и я найду для тебя информацию из Last.fm.")


@bot.message_handler(func=lambda message: True)
def find_music_info(message):
    query = message.text

    # Выполняем запрос к Last.fm API
    lastfm_url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={query}&api_key={lastfm_api_key}&format=json'

    response = requests.get(lastfm_url)
    data = response.json()

    if 'results' in data and 'trackmatches' in data['results']:
        trackmatches = data['results']['trackmatches']['track']

        if trackmatches:
            first_track = trackmatches[0]
            track_name = first_track['name']
            artist_name = first_track['artist']
            track_url = first_track['url']

            response_text = f"Я нашел информацию о треке '{track_name}' исполнителя {artist_name} на Last.fm:\n{track_url}"
        else:
            response_text = f"Извините, я не смог найти информацию о '{query}' на Last.fm."
    else:
        response_text = "Произошла ошибка при поиске музыки на Last.fm."

    bot.reply_to(message, response_text)


if __name__ == '__main__':
    bot.polling()
