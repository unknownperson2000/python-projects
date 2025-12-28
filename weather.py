import tkinter as tk
import requests

API_KEY = "59bd16ad95e948a97a16d58d191066e1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if city == "":
        result_label.config(text="Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        result_label.config(text="City not found")
        return

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]

    result = (
        f"City: {city}\n"
        f"Temperature: {temp}°C\n"
        f"Condition: {weather}\n"
        f"Humidity: {humidity}%"
    )

    result_label.config(text=result)

# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

tk.Label(root, text="Weather App", font=("Arial", 16, "bold")).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), width=20)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
