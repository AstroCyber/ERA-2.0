import imp
import time_get as time

def greet():
    #greeting user with good [morning/evening] Sir Its [Hr]:[Min] [am/pm]
    print(f"Good {time.mn} Sir Its {time.current_timeH}:{time.current_timeM} {time.ampm}")
    imp.speaker.say(f"Good {time.mn} Sir Its {time.current_timeH}:{time.current_timeM} {time.ampm}")
    imp.speaker.runAndWait()
