import requests

def get_weather(city="London"):
    try:
        api = f"http://wttr.in/{city}?format=3"
        return requests.get(api).text
    except:
        return "Sorry, I couldn't fetch the weather."

def register():
    return {
        "name": "weather",
        "commands": ["weather", "temperature", "forecast"],
        "function": lambda command, speak: speak(get_weather())
    }
