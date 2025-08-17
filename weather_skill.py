import requests

API_KEY = "your_openweathermap_api_key"  # replace with your real API key

def can_handle(command: str) -> bool:
    return "weather" in command.lower()

def handle(command: str, speak):
    city = "your city"

    # Try to extract city from command
    words = command.lower().split()
    if "in" in words:
        idx = words.index("in")
        if idx + 1 < len(words):
            city = words[idx + 1].capitalize()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            speak(f"Sorry, I couldn't find the weather for {city}.")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        speak(f"The weather in {city} is {condition} with a temperature of {temp}°C.")
    except Exception as e:
        speak(f"Sorry, I failed to fetch the weather: {e}")
