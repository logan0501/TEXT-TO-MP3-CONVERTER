import pyttsx3
engine=pyttsx3.init()
def setvolume(volume,text):
    newvo=engine.getProperty('volume')
    engine.setProperty('volume',volume)
    engine.say(text)
    engine.runAndWait()
def setrate(rate,text):
    newrate=engine.getProperty('rate')
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
def setvoice(voice,text):
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[voice].id)
    engine.say(text)
    engine.runAndWait()
def speakouttext(text):
    engine.say(text)
    engine.runAndWait()
def saveaudio(name,text):
    engine.save_to_file(text,name+'.mp3')
    engine.runAndWait()
    print("Audio saved sucessfully")
def start():
    res=0
    while res!=6:
        print("1.speak out your text")
        print("2.change volume")
        print("3.change voice")
        print("4.change speed")
        print("5.save your audio")
        print("6.exit")
        res=int(input("enter your response "))
        if res==1:
            text=input("enter some text you want to play with ")
            speakouttext(text)
        elif res==2:
            vol=float(input("enter volume(floating value) "))
            setvolume(vol,text)
        elif res==3:        
            gen=int(input("enter 1 for Female and 0 for Male voice"))
            setvoice(gen,text)
        elif res==4:   
            rate=int(input("enter rate(int value(current rate is 200)) "))
            setrate(rate,text)
        elif res==5:
            filename=input("enter file name")
            saveaudio(filename,text)
        elif res==6:
            print("Project ends")
            engine.stop()
        else:    
            print("enter right choice")

start()
