import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes as pk


listener = sr.Recognizer()
engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150) 

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk('hi Vishal, What can i do for you ?')

def take_command():
    try:
        with sr.Microphone() as source:
           
            print("listening....")
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bruno" in command:
                command =command.replace('bruno','')
                print(command)
            
    except:
        pass
    return command

def run_alexa():
    com =take_command()
    print(com)
    if 'play' in com:
        song= com.replace('play','')
        talk('playing'+song)
        pk.playonyt(song)
    elif "time" in com:
        time =datetime.datetime.now().strftime('%H:%M %p')
        talk('current time is'+time)
    elif "who is" in com:
        person =com.replace("who is",'')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif "what is" in com:
        person1 =com.replace("what is",'')
        info1 = wikipedia.summary(person1,1)
        print(info1)
        talk(info1)
    elif "joke" in com:
        talk(pk.get_joke())
    elif "date" in com:
        talk("sorry, i am in relation with wifi")
    else:
        talk("sorry, i didn't got what you said !, please repeat the command")
        
while True:
    run_alexa()