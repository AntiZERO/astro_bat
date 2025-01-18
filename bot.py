# Patch audioop before importing discord
import audioop_patch
import discord
from discord.ext import tasks
from config import *
from news_apis.nasa_api import NASANews
from utils.formatter import make_post_pretty

class AstroBat(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.nasa = NASANews(NASA_API_KEY)
        
        # Future feature ideas:
        # - Track ISS passes over Austin
        # - Local stargazing conditions
        # - ACC Astronomy Club event reminders
        
    async def setup_hook(self):
        self.check_space_news.start()
    
    async def on_ready(self):
        print(f"{BOT_EMOJI} {BOT_NAME} is ready to explore the cosmos! {STAR_EMOJI}")
        
    @tasks.loop(seconds=UPDATE_INTERVAL)
    async def check_space_news(self):
        channel = self.get_channel(ASTRONOMY_CHANNEL_ID)
        if not channel:
            print(f"{BOT_EMOJI} Lost in space - can't find the astronomy channel!")
            return
        
        nasa_post = await self.nasa.get_astronomy_pic()
        if nasa_post:
            embed = make_post_pretty(nasa_post)
            await channel.send(embed=embed)

def main():
    print(f"{BOT_EMOJI} {BOT_NAME} preparing for launch...")
    bot = AstroBat()
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()