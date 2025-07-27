from flask import Flask, request, jsonify
import pyttsx3
import requests
import AppOpener
import musicLibrary as ml
import webbrowser

app = Flask(__name__)

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle commands
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        # Code to open Google in the browser (can be modified for web-based context)
        return "Opening Google"
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        return "Opening Facebook"
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        return "Opening YouTube"
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        return "Opening LinkedIn"
    elif c.lower().startswith("open"):
        ks = c.lower().split(" ")[1]
        speak(f"Opening {ks}")
        AppOpener.open(ks)
        return f"Opening {ks}"
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        webbrowser.open(ml.music[song])
        speak(f"Playing {song}")
        return f"Playing {song}"
    elif "headlines" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=dea7fd51939c4765bfbe86a1c87fc69d")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            headlines = [article['title'] for article in articles]
            for headline in headlines:
                speak(headline)
            return "Headlines spoken"
        else:
            return f"Failed to fetch headlines, status code: {r.status_code}"

# Routes
@app.route('/')
def index():
    return "<h1>Welcome to Luffy Assistant!</h1>"

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    if command:
        response = processCommand(command)  # Pass the command to the function
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "No command provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
