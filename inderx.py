
import requests import tkinter as tk
from tkinter import messagebox # API key and base URL
api_key = "af65cc8c73716b9270d9cfbc2e77ce00"
base_url = "https://api.openweathermap.org/data/2.5/weather" # Function to fetch weather data
 

 
def get_weather():
city = city_entry.get() if not city:
messagebox.showwarning("Input Error", "Please enter a city name.") return

# Make API request
weather = requests.get(f"{base_url}?q={city}&units=imperial&APPID={api_key}") if weather.status_code == 404:
messagebox.showerror("Error", "Invalid city name. Please try again.") else:
weather_data = weather.json()
main_weather = weather_data["weather"][0]["main"] temp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]


# Displaying the results in the GUI result_label.config(
text=f"Weather in {city}:\n{main_weather}\n" f"Temperature: {temp} °F\nHumidity: {humidity}%",
fg="white", bg="#4A90E2"
)

# Setting up the GUI window

app = tk.Tk() app.title("Weather App") app.configure(bg="#4A90E2")

# Make the window full screen app.geometry("500x400")

# Adding a title label

title_label = tk.Label(app, text="Weather Forecast", font=("Arial", 24, "bold"), bg="#4A90E2", fg="white")
title_label.pack(pady=20)

# Frame to hold city input and button input_frame = tk.Frame(app, bg="#4A90E2") input_frame.pack(pady=10)

# Label and Entry for city input

city_label = tk.Label(input_frame, text="Enter City Name:", font=("Arial", 14), bg="#4A90E2", fg="white")
 

 
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(input_frame, width=30, font=("Arial", 14)) city_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to fetch weather

get_weather_button = tk.Button(app, text="Get Weather", font=("Arial", 14, "bold"), bg="#E94E77", fg="white", command=get_weather) get_weather_button.pack(pady=20)

# Label to display results

result_label = tk.Label(app, text="", font=("Arial", 16), justify="center", bg="#4A90E2", fg="white")
result_label.pack(pady=20) app.mainloop()

import requests import tkinter as tk
from tkinter import messagebox # API key and base URL
api_key = "af65cc8c73716b9270d9cfbc2e77ce00"
base_url = "https://api.openweathermap.org/data/2.5/weather" # Function to fetch weather data
 

 
def get_weather():
city = city_entry.get() if not city:
messagebox.showwarning("Input Error", "Please enter a city name.") return

# Make API request
weather = requests.get(f"{base_url}?q={city}&units=imperial&APPID={api_key}") if weather.status_code == 404:
messagebox.showerror("Error", "Invalid city name. Please try again.") else:
weather_data = weather.json()
main_weather = weather_data["weather"][0]["main"] temp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]


# Displaying the results in the GUI result_label.config(
text=f"Weather in {city}:\n{main_weather}\n" f"Temperature: {temp} °F\nHumidity: {humidity}%",
fg="white", bg="#4A90E2"
)

# Setting up the GUI window

app = tk.Tk() app.title("Weather App") app.configure(bg="#4A90E2")

# Make the window full screen app.geometry("500x400")

# Adding a title label

title_label = tk.Label(app, text="Weather Forecast", font=("Arial", 24, "bold"), bg="#4A90E2", fg="white")
title_label.pack(pady=20)

# Frame to hold city input and button input_frame = tk.Frame(app, bg="#4A90E2") input_frame.pack(pady=10)

# Label and Entry for city input

city_label = tk.Label(input_frame, text="Enter City Name:", font=("Arial", 14), bg="#4A90E2", fg="white")
 

 
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(input_frame, width=30, font=("Arial", 14)) city_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to fetch weather

get_weather_button = tk.Button(app, text="Get Weather", font=("Arial", 14, "bold"), bg="#E94E77", fg="white", command=get_weather) get_weather_button.pack(pady=20)

# Label to display results

result_label = tk.Label(app, text="", font=("Arial", 16), justify="center", bg="#4A90E2", fg="white")
result_label.pack(pady=20) app.mainloop()
