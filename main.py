import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import client

engine = pyttsx3.init()
r = sr.Recognizer()
newsapi = "fb27f411dd3c46708dbf571c7607f3d7"

def music():
    try:
        with sr.Microphone() as source:
            speak("which song")
            audio = r.listen(source)
            song = r.recognize_google(audio)
            return song
        
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred; {e}")

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif "music" in c.lower():

            song = music()
            link = musiclibrary.music[song]
            webbrowser.open(link)

    elif "deactivate" in c.lower():
        speak("jarvis is deactivated.")
        exit()

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # pasre the json response
            data = r.json()

            # extracts the articles
            articles = data.get('articles',[])

            # print the headlines
            for article in articles:    
                speak(article['title'])

    else:
        # let the open ai handle this
        a = client.ai(c)
        speak(a)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Inistializing Jarvis.....")
    while True:

        # Recognize speech using Google's speech recognition service
        print("Recognizing....")

        try:
             # Listen for the wake word jarvis
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                word = r.recognize_google(audio)
            
            if "jarvis" in word.lower():
                speak("ya ")           

                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
    
                processcommand(command)

        except Exception as e:
            print("error; {0}".format(0))