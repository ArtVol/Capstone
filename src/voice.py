#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import pprint

import speech_recognition as sr
import clothesAdvisor
from converter import Converter
from playsound import playsound
from time import ctime
from gtts import gTTS
from xml_parse import doParse

class Voice():
    def speak(self, audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        playsound('audio.mp3')
        #os.system("mpg321 audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data

    def weather(self, data):
        return "Today is " + data["weather"][0]["description"] + ". Temperature is about " + str(int(data["main"]["temp"])) + ". "

    def dress(self, data):
        converter = Converter()
        parse = {}
        with open("clothes.xml") as src:
            parse = doParse(src)

        weather = converter.conv(parse, data)
        data = {
            "RAIN": weather["RAIN"],
            "WIND": weather["WIND"],
            "TEMP": weather["TEMP"]
        }
        # print clothesAdvisor.clothesAdvisor(data)

        ostr = "No time to explain, dress up " + clothesAdvisor.clothesAdvisor(data) + "and go OUT!. Good day."

        #ostr = "In my mind, you should dress up " + clothesAdvisor.clothesAdvisor(data) + ". Good day."
        return ostr

    def jarvis(self, data):
        print (self.weather(data) )#+ self.dress(data))

        # if "how are you" in data:
        #     self.speak("I am fine")
        #
        # if "what time is it" in data:
        #     self.speak(ctime())
        #
        # if "where is" in data:
        #     data = data.split(" ")
        #     location = data[2]
        #     self.speak("Hold on, I will show you where " + location + " is.")
        #     os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")


