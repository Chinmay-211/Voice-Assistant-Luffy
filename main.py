
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary as ml
import requests
import AppOpener

recoginzer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="dea7fd51939c4765bfbe86a1c87fc69d"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        print("Opening Google")
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        print("Opening Facebook")
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        print("Opening YouTube")
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif c.lower().startswith("open"):
        ks=c.lower().split(" ")[1]
        print(f"Opening {ks}")
        AppOpener.open(ks)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        webbrowser.open(ml.music[song])
    elif "headlines" in c.lower():
        print("Headlines condition met")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            print("API request successful")
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            print(f"API request failed with status code: {r.status_code}")
    

if __name__=="__main__":
    speak("Initializing Luffy.....")
    while True:
        

        # recognize speech using Sphinx
        try:
                #LIsten for THe waake word Jarvis
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.....")
                # Updated timeout and phrase_time_limit
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            print("Recogninzing....")
            with sr.Microphone() as source:
                print("Listening.....")
                # Updated timeout and phrase_time_limit
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word= r.recognize_google(audio)
            if(word.lower()=="luffy"):
                print("Hello Sir How can i help you")
                speak("Hello Sir How can i help you")
                #listen for command
                with sr.Microphone() as source:
                    print("Luffy Activated")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error")
        
