import sys
import types

class AudioopMock:
    def __getattr__(self, name):
        def mock_method(*args, **kwargs):
            return None
        return mock_method

# Create a mock audioop module
audioop_mock = AudioopMock()
sys.modules['audioop'] = audioop_mock

# In main bot.py script, import this patch before importing discord