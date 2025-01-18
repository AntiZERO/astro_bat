import discord
from config import ACC_PURPLE, BOT_NAME, BOT_EMOJI, STAR_EMOJI

def make_post_pretty(article):
    # Create a nice-looking Discord message
    embed = discord.Embed(
        title=f"{BOT_EMOJI} {STAR_EMOJI} {article['title']}",
        description=article['description'][:200] + "...",
        color=ACC_PURPLE
    )
    
    if article['media_type'] == 'image' and article['image_url']:
        embed.set_image(url=article['image_url'])
    
    embed.set_footer(text=f"Brought to you by {BOT_NAME} | ACC Astronomy Club")
    return embed