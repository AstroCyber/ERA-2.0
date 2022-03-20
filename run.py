import imp_audio
import stt
import webbrowser as web
import pywhatkit as pwk
import sys
import hello

#getting recognizer
recognizer = imp_audio.recognizer

#getting speaker
speaker = imp_audio.speaker


def run():
    hello.greet()
    while 1:
            #check point 1
            print("check 1")
            #getting your voice input
            get2 = stt.get()
            try:
                #checking if u said {your bot name} in my case its echo
                if "echo" in get2:
                    #check point 2
                    print("check 2")
                    #getting your input again if you said echo
                    get = stt.get()
                    try:
                        #checking if u want to open your email
                        if "mail" in get:
                            print("which email do you use sir")
                            speaker.say("which email do you use sir")
                            speaker.runAndWait()
                            email = stt.get()
                            #checking if you said gmail in your input
                            if "gmail" in email:
                                print("Sure Sir Opening Gmail...")
                                speaker.say("Sure Sir Opening Gmail...")
                                speaker.runAndWait()
                                #opening gmail in your default browser
                                web.open('http://google.com/mail/')
                            #checking if you said outlook in your input
                            if "outlook" in email:
                                print("Sure Sir Opening Outlook...")
                                speaker.say("Sure Sir Opening Outlook...")
                                speaker.runAndWait()
                                web.open('http://outlook.com/mail/')
                        #checking if there is exit in your input
                        elif "exit" in get:
                            print("Exiting The Program")
                            speaker.say("Exiting The Program")
                            speaker.runAndWait()
                            #exiting program with exit code [0]
                            sys.exit(0)
                        #checking if there is play in your input
                        elif "play" in get:
                            #getting the song name
                            music = get.replace("play", "")
                            #checking if input is none
                            if music == "":
                                print("Pls Enter Valid Input")
                                speaker.say("Pls Enter Valid Input")
                                speaker.runAndWait()
                            #playing the song if there is a valid input 
                            else:
                                print(f"Playing...{music}")
                                speaker.say(f"playing..{music}")
                                speaker.runAndWait()
                                pwk.playonyt(music)
                    #closing try by excepting TypeError of NoneType 
                    except TypeError:
                        pass
                else:
                  pass
            #closing try by excepting TypeError of NoneType
            except TypeError:
                pass
