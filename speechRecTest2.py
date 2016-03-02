import speech_recognition as sr

import speech_recognition as sr

import requests
import json
url = 'http://192.168.1.117/api/5020c25b696a73b540fbee2c7bcbde38/lights/1/'
response = requests.get(url).json()
print response

commands = {"turn the lights on": {"data": '{"on":true, "sat":254, "bri":254,"hue":10000}'}, "turn the lights off": {"data": '{"on":false}'}}


r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        #print("Say something!")
        with m as source: audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            #value = r.recognize_google(audio)

            text = r.recognize_google(audio)
            textArr = text.split()
            print("Google Speech Recognition thinks you said " + text)
            if(text in commands):
                data = commands[text]["data"]
                response = requests.put(url+'state', data=data)
                print response.json()
            # we need some special handling here to correctly print unicode characters to standard output
            #if str is bytes: # this version of Python uses bytes for strings (Python 2)
            #    print(u"You said {}".format(value).encode("utf-8"))
            #else: # this version of Python uses unicode for strings (Python 3+)
            #    print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
