import speech_recognition as sr
import pyttsx3 as tts

#making recognizer variable
recognizer = sr.Recognizer()
#making speaker variable
speaker = tts.init()
#setting speed of the voice of bot
speeker.setProperty('rate', 150)
#getting voice property
voices = speeker.getProperty('voices')
print(voices)
#setting voice 1 = female, 0 = male
speeker.setProperty('voice', voices[1].id)
