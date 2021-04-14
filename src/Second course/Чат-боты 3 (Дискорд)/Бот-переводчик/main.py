import datetime
from discord.ext import commands

import googletrans
# Install with this command: pip install googletrans==3.1.0a0

TOKEN = ""


class LanguageDir:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to


users = {

}
translator = googletrans.Translator()


class YLBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help(self, ctx):
        await ctx.send(f"/help_bot - инструкция по работе команд\n"
                       f'/set_lang <from> <to> - смена направления перевода на "с <from> на <to>"\n'
                       f"/text <phrase> - перевод <phrase> согласно выбранному направлению перевода")

    @commands.command(name="set_lang")
    async def set_lang(self, ctx, fr, to):
        if fr in googletrans.LANGUAGES and to in googletrans.LANGUAGES:
            users[ctx.message.author] = LanguageDir(fr, to)
            await ctx.send(
                f"Текущее направление перевода: {fr} - {to}"
            )
        else:
            await ctx.send(
                "Выберите корректное направление перевода!"
            )

    @commands.command(name="text")
    async def text(self, ctx):
        dir = users.get(ctx.message.author, None)

        content = ctx.message.content[5:]

        if not dir:
            await ctx.send("Установите направление перевода!\n"
                           "Помощь: /help_bot")
        else:
            await ctx.send(
                translator.translate(text=content,
                                     src=dir.fr, dest=dir.to).text
            )


bot = commands.Bot(command_prefix="/")
bot.add_cog(YLBotClient(bot))
bot.run(TOKEN)
