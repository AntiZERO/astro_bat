import os
from dotenv import load_dotenv

load_dotenv()

# Bot identity & branding
BOT_NAME = "AstroBat"
TAGLINE = "Your favorite space-savvy Riverbat! 🦇✨"
BOT_EMOJI = "🦇"  # Used in messages
STAR_EMOJI = "✨"  # For space stuff!

# API Keys and Channel IDs
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
NASA_API_KEY = os.getenv('NASA_API_KEY')
ASTRONOMY_CHANNEL_ID = int(os.getenv('ASTRONOMY_CHANNEL_ID'))

# ACC branding
ACC_PURPLE = 0x4B0082
UPDATE_INTERVAL = 3600  # Check every hour