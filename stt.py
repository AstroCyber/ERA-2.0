import speech_recognition as sr
import imp_audio

#getting variable recognizer
recognizer = imp_audio.recognizer
#getting variable speaker
speaker = imp_audio.speaker

def get():
    try:
        #listening your voice and saving it in source2 variable
        with sr.Microphone() as source2:
            print("Listening..")
            speaker.say("Listening")
            speaker.runAndWait()
            #adjusting for noices
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)
            #saving the sound in mp3 format
            audio2 = recognizer.listen(source2)
            #recognizing the mp3 voice to text
            MyText = recognizer.recognize_google(audio2)
            #converting MyText variable to lower
            MyText = MyText.lower()
            print(MyText)
        return MyText

    except sr.RequestError as e:
        print("Request-Error")

    except sr.UnknownValueError as ue:
        print("Unknown-Value-Error")

    except OSError:
        print("OS-Error")
