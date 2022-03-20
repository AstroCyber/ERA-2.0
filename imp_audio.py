import speech_recognition as sr
import pyttsx3 as tts

#making recognizer variable
recognizer = sr.Recognizer()
#making speaker variable
speaker = tts.init()
#setting speed of the voice of bot
speaker.setProperty('rate', 150)
#getting voice property
voices = speaker.getProperty('voices')
print(voices)
#setting voice 1 = female, 0 = male
speaker.setProperty('voice', voices[1].id)
