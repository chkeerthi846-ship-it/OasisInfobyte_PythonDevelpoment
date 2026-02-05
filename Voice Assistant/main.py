import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# -------- TEXT TO SPEECH --------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# -------- SPEECH INPUT --------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# -------- FEATURES --------
def tell_time():
    speak("The time is " + datetime.datetime.now().strftime("%I:%M %p"))

def tell_date():
    speak("Today's date is " + datetime.datetime.now().strftime("%B %d, %Y"))

# -------- MAIN --------
speak("Hello. I am your voice assistant.")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak("Searching for " + query)
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif "exit" in command or "stop" in command:
        speak("Goodbye.")
        break

    else:
        speak("Sorry, I did not understand.")
