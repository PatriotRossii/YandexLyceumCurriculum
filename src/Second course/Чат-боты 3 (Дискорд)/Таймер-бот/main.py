import asyncio
import datetime
from discord.ext import commands

TOKEN = "your_token"
timers = {}


class Timer:
    def __init__(self, time, delta):
        self.installed = time
        self.delta_time = delta

    def last(self):
        return self.installed + self.delta_time <= datetime.datetime.now()


class YLBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_timer')
    async def set_timer(self, ctx, hours, minutes, seconds):
        author = ctx.message.author

        hours, minutes, seconds = int(hours), int(minutes), int(seconds)

        timers[author] = Timer(datetime.datetime.now(), datetime.timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        ))

        await ctx.send(f"The timer should start in {hours} hours, {minutes} minutes and {seconds} seconds")


async def check_updates():
    while True:
        to_delete = []
        for key, timer in timers.items():
            if timer.last():
                await key.send("Time X has come!")
                to_delete.append(key)
        for key in to_delete:
            del timers[key]
        await asyncio.sleep(1)


bot = commands.Bot(command_prefix="")

bot.add_cog(YLBotClient(bot))
bot.loop.create_task(check_updates())

bot.run(TOKEN)
