import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Declaring the engine and setting the properties
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function which makes the VA speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait
    
# Gretting fucntion whenever the VA is started
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("A very Good Morning! from Jarvis. How may I help you ?")
    elif hour>=12 and hour<18:
        speak("A very Good Afternoon! from Jarvis. How may I help you ?")
    else:    
        speak("A very Good Evening! from Jarvis. How may I help you ?")

# Taking the user commands and recognising them    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio,"en-in")
        print(query)
    except Exception as e:
        print("Say that again")
        return "NONE"

# Method to send a mail 
def sendEmail(email,content):
    server = smtplib.SMTP("smtp@gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sender@gmail.com","pass") # Put the email-id and pass at the respective positions.
    server.sendmail("receivers.mail.com",email,content)
    server.close()

# Main function containing the basic tasks using if-else can be modified acc to needs.
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 4 )
            print(results)
            speak(results)
        
        elif "open google" in query:
            speak("Opening Google...")
            webbrowser.open("google.com")
        
        elif "open youtube" in query:
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
        
        elif "open facebook" in query:
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
        
        elif "the time" in query:
            tm = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time now is: {tm}")
        
        elif "open visual studio" in query:
            loc = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(loc)
        
        elif "open pycharm" in query:
            loc = "C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.4\bin\pycharm64.exe"
            os.startfile(loc)
        
        elif "sent an email" in query:
            try:
                speak("Tell me the email address")
                email = takeCommand()
                speak("What should I say")
                content = takeCommand()
                sendEmail(email,content)
                speak("Email has been sent")
                print("Email has been sent")
            except Exception as e:
                print("Not able to sent the email.Please try again.")