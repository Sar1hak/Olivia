# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Optional, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)



#import xlsxwriter
import pandas as pd

#from actions import config
#from actions.api import community_events
#from actions.api.algolia import AlgoliaAPI
#from actions.api.discourse import DiscourseAPI
#from actions.api.gdrive_service import GDriveService
#from actions.api.mailchimp import MailChimpAPI

logger = logging.getLogger(__name__)


class ActionSubmitPersonalData(Action):
    def name(self) -> Text:
        return "action_submit_personal_data"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        import datetime
        
        if tracker.get_slot('confirm_data_intake') == True:
            user_name = tracker.get_slot("person_name")
            age = tracker.get_slot("age")
            #gender = tracker.get_latest_entity_values("gender")
            gender = tracker.get_slot("gender")

            blood_type = [{"label":"A+","value":"/personal_data{'blood_type':'A+'}"},
                          {"label":"B+","value":"/personal_data{'blood_type':'B+'}"},
                          {"label":"A-","value":"/personal_data{'blood_type':'A-'}"},
                          {"label":"B-","value":"/personal_data{'blood_type':'B-'}"},
                          {"label":"AB+","value":"/personal_data{'blood_type':'AB+'}"},
                          {"label":"AB-","value":"/personal_data{'blood_type':'AB-'}"},
                          {"label":"O-","value":"/personal_data{'blood_type':'O-'}"},
                          {"label":"O+","value":"/personal_data{'blood_type':'O+'}"}]
            
            blood_value = {"payload":"dropDown","data":blood_type}
            dispatcher.utter_message(text = "Select your Blood type",json_message = blood_value)
            
            contact = tracker.get_slot("phone_num")
            mail = tracker.get_slot("email")
        else:
            dispatcher.utter_message(
                        text=f"Going Anonymous")
            dispatcher.utter_message(
                        text=f"I am going to take just some basic information")
            user_name = "Anonymous"
            age = "-"
            #gender = tracker.get_latest_entity_values("gender")
            gender = "-"
            contact = "XXXXXXXXXX"

        history = tracker.get_slot("history")
        date = datetime.datetime.now().strftime("%d/%m/%y")
        
        personal_info = [user_name, age, gender, blood_value, history, date, contact, mail]

        #with xlsxwriter.Workbook('test.xlsx') as workbook:
        #    worksheet = workbook.add_worksheet()
        #    
        #    for row_num, data in enumerate(personal_info):
        #        worksheet.write_row(row_num, 0, data)
        
        pd.Series(personal_info)
        personal_info.to_excel('aFileName.xlsx')
        '''
        # ADDIND TO GOOGLE DRIVE SHEETS
        try:
        
            #gdrive = GDriveService()
            #gdrive.store_data(personal_info)
            dispatcher.utter_message(template="utter_confirm_request")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_request_failed")
            return []
        '''
        #delete this after upper googledrive setted
        return []



"""class ActionSubmitAnonymousData(Action):
    def name(self) -> Text:
        return "action_submit_anonymous_data"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        #Once we have all the information, attempt to add it to the
        #Google Drive database

        import datetime

        user_name = "Anonymous"
        age = "-"
        #gender = tracker.get_slot("gender")
        gender = tracker.get_latest_entity_values("gender")
        '''
        gender=[{"label":"male","value":"/personal_data{'slot_name':'male'}"},
              {"label":"female","value":"/personal_data{'slot_name':'female'}"},
              {"label":"others","value":"/personal_data{'slot_name':'others'}"}]
        message={"payload":"buttons","gender":gender}
        dispatcher.utter_message(text="What is your gender/sex ?",json_message=message)
        '''
        history = tracker.get_slot("history")
        contact = "xxxxxxxxxx"
        exercise = tracker.get_slot("exercise")
        sleep = tracker.get_slot("sleep")
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        personal_info = [user_name, age, gender, history, date, contact, exercise, sleep]
        '''
        # ADDIND TO GOOGLE DRIVE SHEETS
        try:
        
            #gdrive = GDriveService()
            #gdrive.store_data(personal_info)
            dispatcher.utter_message(template="utter_confirm_request")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_request_failed")
            return []
        '''
        #delete this after upper googledrive setted
        return []
"""




class ActionSubmitHealthData(Action):
    def name(self) -> Text:
        return "action_submit_health_data"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        import datetime
        exercise, sleep, water, stress, problems ="","","","",""

        exercise = tracker.get_slot("exercise")
        print(exercise)
        sleep = tracker.get_slot("sleep")
        water = tracker.get_slot("water")
        stress = tracker.get_slot("stress")
        problems = tracker.get_slot("problems")
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        #sales_form_config = domain.get("forms", {}).get("personal_data_form", {})
        #sales_form_required_slots = list(sales_form_config.keys())
        
        #user_name = domain.get("forms", {}).get("personal_data_form", {"person_name"})
        
        health_info = [date, exercise, sleep, water, stress, problems]
        dispatcher.utter_message("Thanks for the information!")

        #database = "diseases.json"
        #data = json.loads(open(database).read())
        '''
        # ADDIND TO GOOGLE DRIVE SHEETS
        try:
        
            #gdrive = GDriveService()
            #gdrive.store_data(personal_info)
            dispatcher.utter_message(template="utter_confirm_request")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_request_failed")
            return []
        '''
        #delete this after upper googledrive setted
        return []






class ActionEnquire(Action):
    def name(self) -> Text:
        return "action_enquire"
    
    
    def similar(a, b):
        """
           get the probability of a string being similar to another string
        """
        from difflib import SequenceMatcher,  get_close_matches
        # get close matches may return the most similar options
        #s1 = "abcdefg"
        #list_one = ["abcdefghi" , "abcdef" , "htyudjh" , "abcxyzg"]
        #match = get_close_matches(s1,list_one , n=2 , cutoff=0.6)
        return SequenceMatcher(None, a, b).ratio()
        
        #import Levenshtein
        #return Levenshtein.ratio(a, b)  
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Display required information for a particular disease"""
        file = open("data/diseasesdb.json",) 
        disease_data = json.load(file) 
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'disease_name':
                name = blob['value'].lower()
                if name in disease_data:
                    data_file = disease_data[name]
                    dispatcher.utter_message(
                        text=f"Disease/Problem: {data_file['key']}")
                    overview = "".join(data_file['overview'])
                    dispatcher.utter_message(
                        text=f"Overview: {overview}")
                    # Continue with further information
                    ask=[{"label":"Yes","value":"/personal_data{'slot_name':'yes'}"},
                            {"label":"No","value":"/personal_data{'slot_name':'no'}"}]
                    message={"payload":"buttons","response":ask}
                    dispatcher.utter_message(text=f"Would you like to know further about {name} ?",json_message=message)
                    #dispatcher.utter_button_template(buttons=ask)
                    if message =="yes":
                        enquiry_options=[{"label":"Symptoms","value":"/personal_data{'slot_name':'symptoms'}"},
                                         {"label":"Causes","value":"/personal_data{'slot_name':'causes'}"},
                                         {"label":"Risk Factors","value":"/personal_data{'slot_name':'risk_factor'}"},
                                         {"label":"Treatment","value":"/personal_data{'slot_name':'treatment'}"},
                                         {"label":"Medication","value":"/personal_data{'slot_name':'medication'}"},
                                         {"label":"Home Remedies","value":"/personal_data{'slot_name':'home_remedies'}"},
                                         {"label":"Link","value":"/personal_data{'slot_name':'link'}"},
                                         {"label":"All","value":"/personal_data{'slot_name':'all'}"}]
                        enquiry_value={"payload":"dropDown","data":enquiry_options}
                        dispatcher.utter_message(text="Select what you would like to view:",json_message=enquiry_value)


                        if enquiry_value == "All":
                            dispatcher.utter_message(
                                text=f"Symptoms: {data_file['symptoms']}")
                            dispatcher.utter_message(
                                text=f"Causes: {data_file['causes']}")
                            dispatcher.utter_message(
                                text=f"Risk Factors: {data_file['risk_factor']}")
                            dispatcher.utter_message(
                                text=f"Treatment: {data_file['treatment']}")
                            dispatcher.utter_message(
                                text=f"Medication: {data_file['medication']}")
                            dispatcher.utter_message(
                                text=f"Home Remedies: {data_file['home_remedies']}")
                        else:
                            dispatcher.utter_message(
                                text=f" {data_file[enquiry_value]}")
                    else:
                        dispatcher.utter_message(text=f"Cool")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
            else:
                dispatcher.utter_message(
                        text=f"I do not recognize, are you sure it is correctly spelled?")

        return []        


"""class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/diseasesdb.json")
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
            )
        super().__init__(knowledge_base)
"""




class ActionDiseaseEvaluation(Action):
    def name(self) -> Text:
        return "action_disease_evaluation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        dispatcher.utter_message(
                        text=f"Evaluating Data and finding matching symptoms")
        #database = "diseases.json"
        #data = json.loads(open(database).read())
        '''
        # ADDIND TO GOOGLE DRIVE SHEETS
        try:
        
            #gdrive = GDriveService()
            #gdrive.store_data(personal_info)
            dispatcher.utter_message(template="utter_confirm_request")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_request_failed")
            return []
        '''
        #delete this after upper googledrive setted
        return []






'''
class ActionSubmitPersonalData(Action):

    def name(self) -> Text:
        return "action_submit_personal_data"
   
    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot('confirm_data_intake') == True:
            return ['person_name','age','gender','history','phone_num','blood_type','email','exercise','water','sleep','stress',
                    'confirm_data_intake']
        else:
            return ['history','blood_type','exercise','water','sleep','stress','confirm_data_intake']
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "confirm_data_intake": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="personal_data", value=True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None"),
            ],
            "water": [
                self.from_text(intent="personal_data"),
            ],
            "history": [
                self.from_text(intent="personal_data"),
            ],
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        import datetime
        
        if tracker.get_slot('confirm_data_intake') == True:
            user_name = tracker.get_slot("person_name")
            age = tracker.get_slot("age")
            #gender = tracker.get_latest_entity_values("gender")
            gender = tracker.get_slot("gender")

            blood_type = [{"label":"A+","value":"/personal_data{'blood_type':'A+'}"},
                          {"label":"B+","value":"/personal_data{'blood_type':'B+'}"},
                          {"label":"A-","value":"/personal_data{'blood_type':'A-'}"},
                          {"label":"B-","value":"/personal_data{'blood_type':'B-'}"},
                          {"label":"AB+","value":"/personal_data{'blood_type':'AB+'}"},
                          {"label":"AB-","value":"/personal_data{'blood_type':'AB-'}"},
                          {"label":"O-","value":"/personal_data{'blood_type':'O-'}"},
                          {"label":"O+","value":"/personal_data{'blood_type':'O+'}"}]
            
            blood_value = {"payload":"dropDown","data":blood_type}
            dispatcher.utter_message(text="Select your Blood type",json_message = blood_value)
            
            contact = tracker.get_slot("phone_num")
            mail = tracker.get_slot("email")
        else:
            user_name = "Anonymous"
            age = "-"
            #gender = tracker.get_latest_entity_values("gender")
            gender = "-"
            contact = "XXXXXXXXXX"

        history = tracker.get_slot("history")
        date = datetime.datetime.now().strftime("%d/%m/%y")
        
        personal_info = [user_name, age, gender, blood_value, history, date, contact, mail]

        #with xlsxwriter.Workbook('test.xlsx') as workbook:
        #    worksheet = workbook.add_worksheet()
        #    
        #    for row_num, data in enumerate(personal_info):
        #        worksheet.write_row(row_num, 0, data)
        
        pd.Series(personal_info)
        personal_info.to_excel('aFileName.xlsx')
        #delete this after upper googledrive setted
        return []
'''



'''

- story: get_personal_info none
  steps:
  - action: utter_take_info
  - intent: response1
    entities:
    - confirm_data_intake: "False"
  - slot_was_set:
    - confirm_data_intake: "False"
  - action: action_submit_personal_data
  - action: utter_personal_data_summary
  - action: utter_info_thanks

'''







import requests

class ActionGetNews(Action):
    def name(self) -> Text:
        return "action_get_news"
        
    """
    def get_request():
        import requests

        url = ('http://newsapi.org/v2/everything?'
               'q=tesla&'
               'from=2021-02-18&'
               'sortBy=publishedAt&'
               'apiKey=ff669753f7a74ace97b7aabb419655ab')
        api_key = "ff669753f7a74ace97b7aabb419655ab"
        response = requests.get(url)
        print (response.json())

        
        #headers = {'Authorization': 'Bearer example-auth-code'}
        # #payload = {'name':'Mark', email: 'mark@bearer.sh'}
        # 
        # #response =  requests.post(url, headers=headers, json=payload)
        # 
        # #response_API = requests.get(url)
        # #print(response_API.status_code)
        # #data = response_API.text
        # ### Load data in json format
        # #parse_json = json.loads(data)
        # #active_case = parse_json['articles']['description']
        # #print(active_case)
        return response.json()
    """

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""
        print("qwertyuil")

        dispatcher.utter_message(
                        text=f"Getting News values")
        
        
        url = ('https://jsonplaceholder.typicode.com/todos/1')
        #api_key = "ff669753f7a74ace97b7aabb419655ab"
        response = requests.get(url)
        print (response.json())

        data = response.json()
        dispatcher.utter_message(
                        text=json.dumps(data))
        return []
