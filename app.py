from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = 'your_openweathermap_api_key'  # Replace with your own API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"]
                }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = 'your_openweathermap_api_key'  # Replace with your own API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"]
                }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
