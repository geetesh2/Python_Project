import pyttsx3

engine = pyttsx3.init('sapi5')
#sapi5 is a microsoft api for speech
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    pass