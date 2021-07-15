import pyttsx3
import speech_recognition as sr
import wikipedia
from services import jokes, wiki, news, yt
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    # takes input from mic and returns string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.energy_threshold = 100
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"{query}")
        except Exception as e:
            print(e)
            print("Say that again please..")
            return "None"
        return query


if __name__ == "__main__":
    speak("hey there, ask me anything")
    query = takeCommand()

    if "play" in query:
        print('Playing on Youtube...')
        speak('Playing on Youtube...')
        page = yt.youtube()
        page.playVideo(query)

    elif "joke" in query:
        page = jokes.jokes()
        joke = page.getJoke()
        print(joke)
        speak(joke)

    elif "news" in query:
        page = news.news()
        headline = page.getNews()
        print(headline)
        speak(headline)

    else:
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query, sentences=2)
        page = wiki.infoWiki()
        page.getInfo(query)
        speak("According to Wikipedia")
        speak(results)
