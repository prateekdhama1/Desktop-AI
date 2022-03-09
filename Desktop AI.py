import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import requests
import bs4
import sys




engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
print(voices[1].id)


engine.setProperty('voices', voices[1].id)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("hope you are doing great sir,how can i help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except:
        print("Say that again please...")
        return "none"
    return query
# def res ():
#      res1= requests.get('https://google.com/search?q='+''.join(query))
#      res1.raise_for_status()

#      soup=bs4.BeautifulSoup(res1.text,"html.parser")
#      linkelement = soup.select('.r a')
#      linktoopen = min(1, len(linkelement))
#      for i in range(linktoopen):
#          webbrowser.open('https://google.com'+linkelement[i].get('href'))





def speak(audio):

    engine.say(audio)
    engine.runAndWait()
if _name_ == "_main_":
   wishme()
   
   while True:

       query = takecommand().lower()

       if 'wikipedia' in query:

           speak('searching wikipedia')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:

            webbrowser.open("youtube.com")
       elif 'open facebook' in query:

            webbrowser.open("facebook.com")
       elif 'open whatsapp' in query:

            webbrowser.open("web.whatsapp.com")
       elif 'open google' in query:

            webbrowser.open("google.com")
       elif 'the time' in query:
           strtime  = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir, the time is {strtime}")
       elif 'open code' in query:
           codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)
       elif 'open chrome' in query:
           codepath1 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(codepath1)
       elif 'open maps' in query:
           codepath2 = "C:\\Program Files\\Google\\Google Earth Pro\\client\\googleearth.exe"
           os.startfile(codepath2)
       elif 'thanks friday' in query:
           speak('have a nice day sir')
           break
       elif 'search' in query:
           r=sr.Recognizer()
           with sr.Microphone() as source:
               audio=r.listen(source)
           try:
               text = r.recognize_google(audio)
               
               url = 'https://www.google.co.in/search?q='
               search_url =url+text
               webbrowser.open(search_url)
           except:
               speak('say that again please')


       else:
           speak('say that again please')