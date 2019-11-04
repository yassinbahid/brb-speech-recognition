


import speech_recognition as sr
import time
import pyttsx3
import geocoder
import geocoder
import requests
from weather import Weather, Unit
import win32com
# Record Audio
r = sr.Recognizer()


## Name Resognition
fam_dict = {"john": "Mister Kreider", "mister kreider": "Mister Kreider", "maria": "Missus Kreider", "Missus Kreider": "Missus Kreider", "kim": "Miss Kim", "kim": "Miss Kim", "maya": "Miss Maya", "kristy": "Missus Kristy", 'mitch': "Mister Mitch", "johnny": "Mister John"}

## Commands

def place():
    city = geocoder.ip('me').geojson.get('features')[0].get('properties').get('city')
    return(city)
def weather(d = 0):
    desc_dic = {'light snow': 'there is some light snow', 'Snow' : 'there is snow', 'Heavy snow' : 'there is heavy snow', 'Sleet': 'there is sleet', 'Light shower sleet': 'there is light shower sleet ', 'Shower sleet' : 'there is shower sleet ', 'Light rain and snow': 'there is light rain and snow ', 'Rain and snow': 'There is rain and snow ', 'Light shower snow': 'There is shower snow ','Shower snow': 'There is a shower snow', 'Heavy shower snow' : 'There is heavy snow', 'light rain': 'It is lightly rainy', 'moderate rain': 'It is moderatly rainy', 'heavy intensity rain': 'it is raining heavily', 'very heavy rain': 'There is very heavy rain', 'extreme rain': 'there is extreme levels of rain', 'freezing rain': 'there is freezing rain', 'light intensity shower rain': 'there is light intensity rain', 'shower rain': 'There is shower rain', 'heavy intensity shower rain': 'there is shower rain with heavy intensity', 'ragged shower rain': 'there is ragged shower rain', 'light intensity drizzle': 'There is a light intensity drizzle', 'drizzle': 'there is some drizzle', 'heavy intensity drizzle': 'there is drizzle with heavy intensity', 'light intensity drizzle rain': 'there is some light intensity drizzle rain', 'drizzle rain': 'there is some drizzle rain', 'heavy intensity drizzle rain': 'there is some heavy drizzle rain', 'shower rain and drizzle': 'there is shower rain and drizzle', 'heavy shower rain and drizzle': 'there is heavy shower rain and drizzle', 'shower drizzle': 'there is sime shower drizzle', 'thunderstorm with light rain': 'there is a thunderstorm with light rain', 'thunderstorm with rain': 'there is a thunderstorm with rain', 'thunderstorm with heavy rain': 'there is a thunderstorm with heavy rain', 'light thunderstorm': 'there is a light thunderstorm', 'thunderstorm': 'there is a thunderstorm', 'heavy thunderstorm': 'there is a heavy thunderstorm', 'ragged thunderstorm': 'there is a ragged thunderstorm', 'thunderstorm with light drizzle': 'there is a thunderstorm with light drizzle', 'thunderstorm with drizzle': 'there is thunderstorm with drizzle', 'thunderstorm with heavy drizzle': 'there is a thunderstorm with heavy drizzle', 'mist': 'It is misty right now', 'Smoke': 'There is smoke in the air', 'Haze': 'there is haze', 'sand/ dust whirls': 'there is dust whirls', 'fog': 'it is foggy right now', 'sand': 'there is sand', 'dust': 'the atmosphere is dusty', 'volcanic ash': 'there are volcanic ashes in the air', 'squalls': 'there are squalla', 'tornado': 'there is a tornado', 'clear sky': 'The sky is clear right now', 'few clouds: 11-25%': 'The Sky is predominently clear, there are minimale clouds', 'scattered clouds: 25-50%': 'there are a few scattered clouds', 'broken clouds: 51-84%': 'there are quite a few broken clouds', 'overcast clouds: 85-100%': 'the sky is predominantly cloudy'}

    g = place()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=39eb95d8b69ee4d031700e8a56b8c29d&units=metric'.format(g)
    
    res = requests.get(url).json()
    t = 'The weather forcast is:..........'
    weath = res.get('weather')[0]
    description = res.get('weather')[0].get('description')
    temp = str(res.get('main').get('temp')*9/5 + 32)
    humidity =  str(res.get('main').get('humidity'))
    
    t = t + desc_dic.get(description)
    t = t + '. The average temperature is ' + temp + '. the humidity is ' + humidity

    return(t)

##Command Dictionary

key_words = {"time": "time", "weather": weather(), "list": "list", "email": "email", "calendar": "calendar",}


## Questions
qes_list = {"how": "how", "what": "what", "where": "place", "when": "time", "why": "reason", "who": "person"}

t = 'Hello '

commands = []



r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak Anything :")
    audio = r.listen(source)
    print('done')
    try:
        sp = r.recognize_google(audio,  language="en")
        print("You said : {}".format(sp))
    except:
        print("Sorry could not recognize what you said")
        sp = ''




## Name Resognition
an = 0
for i in fam_dict:
    if i in sp:
        if an > 0:
            t = t + "and "
        t = t + fam_dict.get(i) + " "
for i in key_words:
    if i in sp:
        #exacute command:
        t = key_words.get(i)
    
        



if 'present yourself' in sp:
    t = t + "My name is Barnaby. I am yassin's new assistant. He just started making me. I am not as smart or elloquent as alexa or the google assistant, But I'm learning"

engine = pyttsx3.init()
engine.say(t)
engine.runAndWait() 