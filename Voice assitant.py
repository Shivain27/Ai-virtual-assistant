import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivainvats1@gmail.com', '')
    server.sendmail('Anurag.vats1@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
   # while True:
      
    query = takeCommand().lower()

        # Logic for executing tasks based on query
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            try:
                speak("Can you please repeat")
                query=takeCommand()
            except Exception as e:
                speak(f"Sorry could not find anything for {query}")
                    


    if 'open youtube' in query:
            webbrowser.open("youtube.com")

    if 'open google' in query:
            webbrowser.open("google.com")

    if 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
    if 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
    if 'weather' in query:
            webbrowser.open("weather.com")                 


    
    if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    if 'simon says' in query:
            query=query.replace("simon says", "")
            speak(query)        

        

    elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Anurag.vats1@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 
    elif 'bye' or 'quit' in query:
        speak("Thank you sir, do let me know if I can be of any other help")
        exit            