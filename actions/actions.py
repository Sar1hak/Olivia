"""
WEBSITE
rasa run -m models --enable-api --cors "*"

"""
"""
POSTMAN
rasa run -m models --enable-api --cors "*" --debug

POST: http://locahost:5005/model/parse
KEY: Content-Type
Value: aaplication/json
"""
# importing required libraries
import re
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Optional, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (BotUttered, SlotSet, 
                             EventType,
                             AllSlotsReset,
                             SessionStarted,
                             ActionExecuted)


class ActionGetNews(Action):
    def name(self) -> Text:
        return "action_get_news"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        print("Extracting Data from External API ...")

        from newsapi import NewsApiClient
        #from key import my_api_key
        import datetime as dt
        import pandas as pd
        
        my_api_key = "ff669753f7a74ace97b7aabb419655ab"
        #newsapi = NewsApiClient(api_key=my_api_key)
        #data = newsapi.get_everything(q='jupyter lab', languages='en', page_size=20)
        dispatcher.utter_message("News Feature in progress")
        #dispatcher.utter_message(text=str(data['articles'][0]))

        #url = ('https://jsonplaceholder.typicode.com/todos/1')
        #response = requests.get(url)
        #print (response.json())
        
        #from GoogleNews import GoogleNews
        #googlenews = GoogleNews()
        #googlenews = GoogleNews('en','d')

        #googlenews.search('India')
        #googlenews.getpage(1)

        #googlenews.result()
        #news = googlenews.gettext()

        #data = response.json()
        #dispatcher.utter_message(
        #                text=json.dumps(data))
        #dispatcher.utter_message(text=news[0])
        return []

class ActionGetNews(Action):
    def name(self) -> Text:
        return "action_get_weather"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        print("Extracting Data from External API ...")

        from newsapi import NewsApiClient
        #from key import my_api_key
        import datetime as dt
        import pandas as pd
        
        dispatcher.utter_message("Weather Feature in progress")
        return []









## Sending images from local 
"""
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/img/<path:path>')
def get_image(path):
    image_path = 'img/{}'.format(path)

    return send_file(image_path, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
"""


class ActionGetTime(Action):
    def name(self) -> Text:
        return "action_get_time"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        print("Extracting Data from External API ...")

        from datetime import datetime
        dispatcher.utter_message("According to Indian Standard Time")
        dispatcher.utter_message(f"Date: ", str(datetime.now().date()))
        dispatcher.utter_message(f"Time: ", str(datetime.now().time()))
        return []

class ActionGetName(Action):
    def name(self) -> Text:
        return "action_get_name"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # print("Extracting Data from External API ...")
        message = tracker.latest_message['text']
        print("Track latest messsage: ",message)
        SlotSet("name",message)
        json_response = {
                "intent": "names",
                "user_message": [message],
                "slot":["name"],
                "type":["text","str"],
                "next_message": "greet",
                "next_slot": [""],
                "next_type":["text","str"]
               }
        dispatcher.utter_message(json.dumps(json_response))
        return []
        #:
        #use_entities: []