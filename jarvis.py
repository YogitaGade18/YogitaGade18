from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import wikipedia
import os
import datetime
import smtplib
import speech_recognition as sr
from playsound import playsound
import webbrowser
import pyjokes

print("INITIALIZING LILY....")
sir = "Yogittta!! How can I help for you?"

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning"+sir)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon"+sir)
    else:
        speak("Good Evening"+sir)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said:{query}\n ")

    except Exception as e:
        # print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yogitagade1998@gmail.com', 'Rosewood@1812')
    server.sendmail('yogitagade9137@gmail.com', to, content)
    server.close()

class Widget:
    def __init__(self):
        root = Tk()
        root.title('AI personal Assistant')
        root.geometry("1180x700")

        file = r'F:\GIFS\ai assistant.png'

        image = Image.open(file)

        zoom = 0.5

        #multiple image size by zoom
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

        img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
        panel = Label(root,image=img)
        panel.pack(side='right', fill='both', expand='no')

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click Run Lily to Give command')

        userFrame = LabelFrame(root,text="User", font=('Black ops one',10,'bold'))
        userFrame.pack(fill='both', expand='yes')

        left = Message(userFrame,textvariable=self.userText,bg='#ff0055',fg='white')
        left.config(font=("Century Gothic",24,'bold'))
        left.pack(fill='both',expand='yes')

        compFrame = LabelFrame(root,text="Lily",font=('Black ops one',10,'bold'))
        compFrame.pack(fill='both', expand='yes')

        left2 = Message(compFrame,textvariable=self.compText,bg='#00ff00',fg='white')
        left2.config(font=("Century Gothic",24,'bold'))
        left2.pack(fill='both',expand='yes')

        self.compText.set('Hello I am Lily!!! What Can I do for you Yogittta?')

        btn = Button(root,text='Run Lily', font=('Black ops one',10,'bold'),bg='black',fg='white',command=self.clicked).pack(fill='x',expand='no')
        btn2 = Button(root,text='Close!', font=('Black ops one',10,'bold'),bg='black',fg='white',command = root.destroy).pack(fill='x',expand='no')

        self.compText.set('Hello, I am Lily! What can i do for you mam ??')
        root.bind("<Return>", self.clicked)
        root.mainloop()

    def clicked(self):
        print('Working')
        self.query = takecommand().lower()
        self.userText.set('Listening...')
        self.userText.set(self.query)
        #query = query.lower()


        if 'wikipedia' in self.query:
            speak('Searching Wikipedia...')
            query = self.query.replace("wikipedia", "")
            results = wikipedia.summary(self.query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in self.query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in self.query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in self.query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in self.query:
            music_dir = 'E:\\Play Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
            print(strTime)

        elif 'open code' in self.query:
            codePath="C:\\Users\\Yogita\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in self.query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "yogitagade9137@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
                print("Sorry my friend . I am not able to send this email")

        elif "get out" in self.query or "exit" in self.query:
            speak("All right mam! Have a great time")
            exit()

        elif "news" in self.query:
            news = webbrowser.open_new_tab("https://www.gadgetsnow.com/?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnav")
            speak('Here are some news. Happy reading')

        elif "Thank you" in self.query:
            speak("Your Welcome!!")

        elif "search" in self.query:
            query = self.query.replace("search", "")
            webbrowser.open_new_tab(query)



        elif "joke" in self.query:
            joke =pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "shut down" in self.query:
            os.system("shutdown /s /t 5")

        elif "restart" in self.query:
            os.system("shutdown /r /t 5")

        elif "sleep" in self.query:
            os.system("rundll32.exe powrprof.dll, SetSuspendedState 0,1,0")



if __name__=='__main__':
    speak('Lily IS STARTING')
    wishMe()
    widget = Widget()   