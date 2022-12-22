import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_data(place, days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=imperial&cnt={days * 8}"
    data = requests.get(url).json()

    return data["list"]


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=1))
