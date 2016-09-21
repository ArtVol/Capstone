#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import os
from time import strftime

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from clothesAdvisor import clothesAdvisor
from converter import Converter

class Voice():
    def speak(self, audioString, filename):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save(filename)
        playsound(filename)

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
        out = "Today is "
        # Today
        for item in data["DESCRIPTION"]:
            cur_time = item.split(" ")[1].split(":")[0]
            if item.split(" ") <= strftime("%Y-%m-%d"):
                out += data["DESCRIPTION"][item] +" at "+ cur_time+ " o'clock "
        # Tomorrow
        for item in data["DESCRIPTION"]:
            cur_time = item.split(" ")[1].split(":")[0]
            if item.split(" ") > strftime("%Y-%m-%d"):
                out = ".Tomorrow is "
                out += data["DESCRIPTION"][item] +" at "+ cur_time+ " o'clock"

        out += ". You can feel " + data["WIND"] + ". Temperature is about " + str(data["TEMP"]["NOW"])\
               + ". Day temperature is about " + str(data["TEMP"]["DAY"]) + " and night is "\
               + str(data["TEMP"]["NIGHT"]) + ". "

        return out

    def get_voice_text(self, data):
        converter = Converter()
        weather = converter.conv(data)

        umbrella_alert = "Don't forget your Umbrella!" if "rain" in data["RAIN"] else ""
        weather["DESCRIPTION"] = data["RAIN"]

        out = self.weather(weather) + "No time to explain, dress up " + clothesAdvisor(weather)\
              + umbrella_alert + ". Good day."

        return out

    def get_html_text(self, data):
        converter = Converter()
        weather = converter.conv(data)
        out = ""
        weather["DESCRIPTION"] = data["RAIN"]
        out += clothesAdvisor(weather)

        return out

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


