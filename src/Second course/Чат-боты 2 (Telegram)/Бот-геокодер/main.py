import requests
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "your_token"


def get_ll_spn(toponym):
    envelope = toponym["boundedBy"]["Envelope"]
    lower_corner = [float(e) for e in envelope["lowerCorner"].split()]
    upper_corner = [float(e) for e in envelope["upperCorner"].split()]

    delta_x = upper_corner[0] - lower_corner[0]
    delta_y = upper_corner[1] - lower_corner[1]

    return ",".join(toponym["Point"]["pos"].split()), ",".join([str(delta_x), str(delta_y)])


def geocoder(update, context):
    geocoder_uri = geocoder_request_template = "http://geocode-maps.yandex.ru/1.x/"
    response = requests.get(geocoder_uri, params={
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "format": "json",
        "geocode": update.message.text
    })

    if not response:
        update.message.reply_text(
            "Ошибка выполнения запроса\n"
            f"HTTP статус: {response.status_code} ({response.reason})"
        )
        return

    results = response.json()["response"]["GeoObjectCollection"]["featureMember"]
    if len(results) == 0:
        update.message.reply_text(
            "Не удалось найти топоним по переданному тексту"
        )
        return

    toponym = results[0]["GeoObject"]
    ll, spn = get_ll_spn(toponym)
    # Можно воспользоваться готовой функцией,
    # которую предлагалось сделать на уроках, посвящённых HTTP-геокодеру.

    static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map&pt={ll},pm2rdm"
    context.bot.send_photo(
        update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
        # Ссылка на static API, по сути, ссылка на картинку.
        # Телеграму можно передать прямо её, не скачивая предварительно карту.
        static_api_request,
        caption="Нашёл:"
    )


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, geocoder))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
