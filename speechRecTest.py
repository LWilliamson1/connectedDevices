#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

import requests
import json
url = 'http://192.168.1.117/api/5020c25b696a73b540fbee2c7bcbde38/lights/1/'
response = requests.get(url).json()
print response

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    textArr = text.split()
    print("Google Speech Recognition thinks you said " + text)
    if(text == "turn lights on"):
        data = '{"on":true, "sat":254, "bri":254,"hue":10000}'
        response = requests.put(url+'state', data=data)
        print response.json()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



# recognize speech using Wit.ai
# WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# # recognize speech using IBM Speech to Text
# IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
# IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
# try:
#     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
# except sr.UnknownValueError:
#     print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from IBM Speech to Text service; {0}".format(e))

# # recognize speech using AT&T Speech to Text
# ATT_APP_KEY = "INSERT AT&T SPEECH TO TEXT APP KEY HERE" # AT&T Speech to Text app keys are 32-character lowercase alphanumeric strings
# ATT_APP_SECRET = "INSERT AT&T SPEECH TO TEXT APP SECRET HERE" # AT&T Speech to Text app secrets are 32-character lowercase alphanumeric strings
# try:
#     print("AT&T Speech to Text thinks you said " + r.recognize_att(audio, app_key=ATT_APP_KEY, app_secret=ATT_APP_SECRET))
# except sr.UnknownValueError:
#     print("AT&T Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from AT&T Speech to Text service; {0}".format(e))
