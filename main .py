import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import musiclibrary
import requests

rcognizer = sr.Recognizer()
engine = pyttsx3.init()
#newsapi = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def processCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    elif "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open map" in c.lower():
        webbrowser.open("https://www.google.com/maps/@24.3969766,78.0994204,13z?entry=ttu")      
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    '''elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")  
        if r.status_code == 200:
            data = r.json()   
        # Extract and print the headlines
        articles = data.get('articles', [])
        for article in articles:
            speak(article['title'])
            print(article['title'])'''

if __name__ == "__main__":
    speak("Initializing jarvis.....")
    while True:
        r = sr.Recognizer()

           
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
               # print("Adjusting for ambient noise, please wait...")
               # r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)  # Listen for audio input
    
        # Recognize speech using Google Web Speech API
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yaa")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source ) 
                    command = r.recognize_google(audio)
                    processCommand(command)
            #print(f"You said: {commend}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except Exception as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

