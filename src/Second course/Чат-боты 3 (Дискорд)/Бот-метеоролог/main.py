import requests
from discord.ext import commands
from geopy.geocoders import Nominatim

TOKEN = "your_token"
API_URL = "https://api.weather.yandex.ru/v2/forecast"
YANDEX_API_KEY = "your_api_key"

storage = {}
geolocator = Nominatim(
    user_agent="ForecastBot (Discord)"
)


class Place:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


WIND_DIR = {
    "nw": "северо-западное", "n": "северное", "sw": "юго-западное",
    "ne": "северо-восточное", "e": "восточное", "w": "западное",
    "se": "юго-восточное", "s": "южное", "c": "штиль"
}
PREC = {
    0: "без осадков", 1: "дождь", 2: "дождь со снегом",
    3: "снег", 4: "град"
}


class YLBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help(self, ctx):
        await ctx.send(f"/help_bot - инструкция по работе команд\n"
                       f'/place <place> - задать место прогноза\n'
                       f"/current - сообщение о текущей погоде\n"
                       f"/forecast <days> - прогноз на <days> дней")

    @commands.command(name="place")
    async def place(self, ctx, place_name):
        location = geolocator.geocode(place_name)
        storage[ctx.message.author] = Place(
            location.latitude, location.longitude
        )
        await ctx.send("Место прогноза успешно установлено!")

    @commands.command(name="current")
    async def current(self, ctx):
        # Поля: температура, давление, влажность,
        # направление и сила ветра

        place = storage.get(ctx.message.author, None)
        if not place:
            return await ctx.send(
                "Ошибка. Укажите место прогноза."
            )

        r = requests.get(API_URL, params={
            "lat": place.latitude, "lon": place.longitude,
            "lang": "ru_RU", "limit": 1, "hours": "false"
        }, headers={"X-Yandex-API-Key": YANDEX_API_KEY})
        print(r.text)
        resp = r.json()["fact"]

        await ctx.send(
            "Прогноз на сегодня:\n"
            f"Температура: {resp['temp']} °C\n"
            f"Давление: {resp['pressure_mm']} мм рт. ст.\n"
            f"Влажность: {resp['humidity']}%\n"
            f"Направление ветра: {WIND_DIR[resp['wind_dir']]}\n"
            f"Сила ветра: {resp['wind_speed']} м/c"
        )

    @commands.command(name="forecast")
    async def forecast(self, ctx, days):
        place = storage.get(ctx.message.author, None)
        if not place:
            return await ctx.send(
                "Ошибка. Укажите место прогноза."
            )
        if int(days) > 7:
            return await ctx.send(
                "Извините. Мы можем выдавать прогноз максимум на 7 дней"
            )

        r = requests.get(API_URL, params={
            "lat": place.latitude, "lon": place.longitude,
            "lang": "ru_RU", "limit": int(days), "hours": "false"
        }, headers={"X-Yandex-API-Key": YANDEX_API_KEY})
        resp = r.json()["forecasts"]

        resp_text = ""
        for forecast in resp:
            resp_text += f"Прогноз погоды на {forecast['date']}:\n" \
                         f"Средняя дневная температура: {forecast['parts']['evening']['temp_avg']}\n" \
                         f"Тип осадков: {PREC[forecast['parts']['evening']['prec_type']]}\n\n"

        await ctx.send(resp_text)


bot = commands.Bot(command_prefix="/")
bot.add_cog(YLBotClient(bot))
bot.run(TOKEN)
