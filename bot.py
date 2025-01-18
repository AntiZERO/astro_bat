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
        self.astronomy_channel = None
        self.guild = None
        self.check_space_news = self.check_space_news_loop
        
        # Future feature ideas:
        # - Track ISS passes over Austin
        # - Local stargazing conditions
        # - ACC Astronomy Club event reminders
        
    async def setup_hook(self):
        self.check_space_news.start()
    
    async def on_ready(self):
        print(f"{BOT_EMOJI} {BOT_NAME} is ready to explore the cosmos! {STAR_EMOJI}")

        try:
            # Check if the bot is connected to any guilds
            if len(self.guilds) > 0:
                # Get the guild (server) object
                self.guild = self.guilds[0]

                # Get the astronomy channel from the guild
                self.astronomy_channel = self.guild.get_channel(ASTRONOMY_CHANNEL_ID)
                if self.astronomy_channel is None:
                    print(f"{BOT_EMOJI} Lost in space - can't find the 'astronomy' channel!")
            else:
                print(f"{BOT_EMOJI} Lost in space - the bot is not connected to any servers!")
        except Exception as e:
            print(f"{BOT_EMOJI} Encountered an error: {e}")

    @tasks.loop(seconds=UPDATE_INTERVAL)
    async def check_space_news(self):
        try:
            if self.astronomy_channel is None:
                print(f"{BOT_EMOJI} Lost in space - can't find the 'astronomy' channel!")
                return

            nasa_post = await self.nasa.get_astronomy_pic()
            if nasa_post:
                embed = make_post_pretty(nasa_post)
                await self.astronomy_channel.send(embed=embed)
        except Exception as e:
            print(f"{BOT_EMOJI} Encountered an error: {e}")

def main():
    print(f"{BOT_EMOJI} {BOT_NAME} preparing for launch...")
    bot = AstroBat()
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()