import aiohttp

class NASANews:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.nasa.gov/planetary/apod"
    
    async def get_astronomy_pic(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.url,
                    params={"api_key": self.api_key}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "title": data['title'],
                            "description": data['explanation'],
                            "image_url": data.get('url'),
                            "media_type": data.get('media_type', 'image'),
                            "source": "NASA APOD"
                        }
                    else:
                        print(f"{BOT_EMOJI} Oops! Couldn't get NASA pic: {response.status}")
                        return None
        except Exception as e:
            print(f"{BOT_EMOJI} Houston, we have a problem: {str(e)}")
            return None