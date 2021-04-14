import os

import discord
import requests

TOKEN = ""
CAT_API = "https://api.thecatapi.com/v1/images/search"
DOG_API = "https://dog.ceo/api/breeds/image/random"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился к Дискорду '
              f'и готов показать случайного котика '
              f'(или песика)!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()
        cat, dog = "кот" in content, "собак" in content

        if cat or dog:
            if cat:
                r = requests.get(CAT_API)
                image_url = r.json()[0]["url"]
            else:
                r = requests.get(DOG_API)
                image_url = r.json()["message"]

            image_content = requests.get(image_url).content

            f = open(f"{os.path.basename(image_url)}", "wb")
            f.write(image_content)
            f.close()

            await message.channel.send(file=discord.File(f"{os.path.basename(image_url)}"))


client = YLBotClient()
client.run(TOKEN)
