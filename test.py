import speech_recognition as sr
import time
import os
import random 
from gtts import *
import playsound
from PyDictionary import PyDictionary

dictionary=PyDictionary()

r = sr.Recognizer()

def dictionary_speak(audio_string):
	tts = gTTS(text=audio_string, lang="en")
	r = random.randint(1, 10000000)
	audio_file = "audio-" + str(r) + ".mp3"
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def record_audio():
  with sr.Microphone() as source:
    audio = r.listen(source)
    voice_data = ""
    #try:
    voice_data = r.recognize_google(audio)
    #except sr.UnkownValueError:
    dictionary_speak("Sorry, i did not get that")
    return voice_data

dictionary_speak("hey how can i help you?")

#thisdict =	{
 #  "LOL": "Laughing out loud",
 #  "AKA": "Also known as",
 #  "ATM": "At the moment",
 #  "B4": "Before",
 #  "BRB": "Be right back",
 #  "BTW": "By the Way",
 #  "CMON": "Come on",
 #  "CU" : "See you",
 #  "JK" : "Just kidding",
 #  "NVM" : "Never mind",
 #  "PLS": "Please",
 #  "SYL" : "See you later",
 #  "TU" : "Thank you",
 #  "TTYL" : "Talk to you later",
 #  "UW" : "You're welcome",
 #  "WUP" : "What's up?",
 # # "YW" : "You're welcome",

#}
#dictionary_speak(thisdict)



#dictionary_speak(dictionary.meaning("indentation"))

def respond(voice_data):
	if "what does lol mean" in voice_data:
		dictionary_speak("Laughing out loud, it is used in reaction to something considered extremely funny")

time.sleep(1)
while 1:
	voice_data = record_audio()
	respond(voice_data)
#print("How can i help you?")
#print(voice_data)
