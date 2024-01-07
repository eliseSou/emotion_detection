import requests

"""

Add here code to :
- get and process data from the discord bot
- apply model on it (including preprocessing)
- give results to the web server

"""

def get_voice_extract():
    pass

def apply_model():
    pass

def send_results(prediction):
    URL = "http://127.0.0.1/emotion"
    r = requests.post(url=URL, data=prediction)*
    print(r)


prediction = "sad"


""" voice_extract = get_voice_extract()
prediction = apply_model(voice_extract) """
send_results(prediction)