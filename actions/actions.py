# This files contains your custom actions which can be used to run
# custom Python code.

import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Optional, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    AllSlotsReset,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)
#from mailchimp3 import MailChimp
#from mailchimp3.mailchimpclient import MailChimpError
#from mailchimp3.helpers import check_email

#import xlsxwriter
import pandas as pd

#from actions import config
#from actions.api import community_events
#from actions.api.algolia import AlgoliaAPI
#from actions.api.discourse import DiscourseAPI
#from actions.api.gdrive_service import GDriveService
#from actions.api.mailchimp import MailChimpAPI

logger = logging.getLogger(__name__)
file = open("data/diseasesdb.json",) 
disease_data = json.load(file)

class ValidatePersonalDataForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_personal_data_form"
    
    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        
        return slots_mapped_in_domain
    
    def validate_person_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(f"User name given = {slot_value} length = {len(slot_value)}")
        dispatcher.utter_message(text=f"What a random name. Hahahahahahah")
        return {"age": slot_value}

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(f"Age given = {slot_value} length = {len(slot_value)}")
        if slot_value <= 1 and slot_value>=150:
            dispatcher.utter_message(text=f"That's not a valid. I'm assuming you mis-spelled.")
            return {"age": None}
        else:
            return {"age": slot_value}

    def validate_gender(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        slot_value= slot_value.lower()
        print(f"Gender given = {slot_value} length = {len(slot_value)}")
        if slot_value in ["male","female"]:
            return {"last_name": slot_value}
        else:
            return {"last_name": "others"}
    
    def validate_phone_num(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print(f"Phone number given = {slot_value} length = {len(slot_value)}")
        if len(slot_value)!= 10:
            return {"phone_num": None}
        else:
            return {"phone_num": slot_value}
    
    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:

        print(f"Email given = {slot_value} length = {len(slot_value)}")
        """
        try:
            email = str(slot_value)
            check_email(email)
            return {"email": slot_value}
        except ValueError:  # purposely raised in case of invalid email
            dispatcher.utter_message(text=f"That's not a valid mail id. I'm assuming you mis-spelled.")
            return {"email": None}
        except Exception as e:
            logger.warning(
                f"Error: exception in check_email.\n"
                f"{type(e)} - {e}\n"
                f"email = {email}\n"
                f"type(email) = {type(email)}"
            )
            return {"email": None}
        """
        return {"email": slot_value}

    def validate_blood_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print(f"Blood type given = {slot_value} length = {len(slot_value)}")
        value = slot_value.replace(dict.fromkeys(['pos','positive','plus'],"+"))
        value = slot_value.replace(dict.fromkeys(['neg','negetive','minus'],"-"))
        value = value.replace(" ","").upper()
        if value in ['A+''AB+''B+''O+''A-''AB-''B-''O-']:
            return {"blood_type": value}
        else:
            dispatcher.utter_message(text=f"That's not a valid blood type. I'm assuming you mis-spelled.")
            return {"blood_type": None}
    



class ActionSubmitPersonalDataForm(Action):
    def name(self) -> Text:
        return "action_submit_personal_data_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        
        if tracker.get_slot('confirm_data_intake') == True:
            user_name = tracker.get_slot("person_name")
            age = tracker.get_slot("age")
            #gender = tracker.get_latest_entity_values("gender")
            gender = tracker.get_slot("gender")

            blood_type = tracker.get_slot("blood_type")
            
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
            blood_type = "+-"

        history = tracker.get_slot("history")
        date = datetime.datetime.now().strftime("%d/%m/%y")
        
        personal_info = [user_name, age, gender, blood_type, history, date, contact, mail]

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



class ValidateHealthDataForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_health_data_form"
    
    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        
        return slots_mapped_in_domain
    
    def validate_exercise(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(f"Exercise = {slot_value} length = {len(slot_value)}")
        return {"exercise": slot_value}

    def validate_water(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(f"Water in take = {slot_value} length = {len(slot_value)}")
        
        import string
        #Removing unnecessary cahracters from string
        all=string.maketrans('','')
        nodigs=all.translate(all, string.digits)
        value = slot_value.translate(all, nodigs)

        if value <= 1 and value>=50:
            dispatcher.utter_message(text=f"No way you drink that amount. I'm assuming you mis-spelled.")
            return {"water": None}
        else:
            return {"water": value}

    def validate_stress(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        print(f"Stress value = {slot_value} length = {len(slot_value)}")
        return {"stress": slot_value}
    
    def validate_sleep(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print(f"Sleep value = {slot_value} length = {len(slot_value)}")

        import string
        #Removing unnecessary cahracters from string
        all=string.maketrans('','')
        nodigs=all.translate(all, string.digits)
        value = slot_value.translate(all, nodigs)

        return {"sleep": value}
    
    def validate_relation(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:

        print(f"Relation = {slot_value} length = {len(slot_value)}")
        
        return {"relation": slot_value}
        
    def validate_history(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        print(f"User History given = {slot_value} length = {len(slot_value)}")
        return {"history": slot_value}


class ActionSubmitHealthDataForm(Action):
    def name(self) -> Text:
        return "action_submit_health_data_form"

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
        print("Strart")
        if tracker.get_slot('confirm_health_intake') == "True":
            print(tracker.get_slot('confirm_health_intake'))
            exercise = tracker.get_slot("exercise")
            #print(exercise)
            sleep = tracker.get_slot("sleep")
            water = tracker.get_slot("water")
            stress = tracker.get_slot("stress")
            problems = tracker.get_slot("problems")
            date = datetime.datetime.now().strftime("%d/%m/%Y")

            #sales_form_config = domain.get("forms", {}).get("personal_data_form", {})
            #sales_form_required_slots = list(sales_form_config.keys())
        
            #user_name = domain.get("forms", {}).get("personal_data_form", {"person_name"})
        
            dispatcher.utter_message("Thanks for the information!")
        
        
        health_info = [date, exercise, sleep, water, stress, problems]
        print(health_info)
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
        return health_info





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

        
        name = tracker.get_slot("disease_name")
        name = name.lower()
        if name in disease_data:
            data_file = disease_data[name]
            dispatcher.utter_message(
                        text=f"Disease/Problem: {data_file['key']}")
            overview = "".join(data_file['overview'])
            dispatcher.utter_message(
                        text=f"Overview: {overview}")
            # Continue with further information
            ask=[{"title":"Yes",
                                 "payload":"yes"},
                         {"title":"No",
                                 "payload":"no"}]
            #message={"payload":"buttons","response":ask}
            dispatcher.utter_message(text=f"Would you like to know further about {name} ?",buttons=ask)
                    #dispatcher.utter_button_template(buttons=ask)
            enquiry_value = tracker.get_slot("enquire_name")

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
            dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")

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




class ActionTreatmentMedicationRemedies(Action):
    def name(self) -> Text:
        return "action_treatment_medication_remedies"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        #cure = [{"label":"Treatments","value":"/personal_data{'cure':'Treatment'}"},
        #                  {"label":"Medications","value":"/personal_data{'cure':'Medications'}"},
        #                  {"label":"Home Remedies","value":"/personal_data{'cure':'Home Remedies'}"}]
        #    
        #cure_value = {"payload":"dropDown","data":cure}
        #dispatcher.utter_message(text="What should i Tell you about ?",json_message = cure_value)
        

        #payload = "/cure"
        #buttons = [{"title":"Treatments","payload":"/cure{'name':'Treatment'}"},
        #                  {"title":"Medications","payload":"/cure{'name':'Medications'}"},
        #                  {"title":"Home Remedies","payload":"/cure{'name':'Home Remedies'}"}]

        name = tracker.get_slot('disease_name')
        value = tracker.get_slot('confirm_cure_intake')
        if value!="None":
            if name in disease_data:
                data_file = disease_data[name]
                dispatcher.utter_message(data_file[value])
            else:
                dispatcher.utter_message(text="Invalid Name")

        return []


class ActionSymptomsCauses(Action):
    def name(self) -> Text:
        return "action_symptoms_causes"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[EventType]:

        #problems = [{"title":"Symptoms",
        #                    "payload":"/personal_data{'cure':'Treatment'}"},
        #                  {"title":"Causes","payload":"/personal_data{'cure':'Medications'}"}]
        
        value = tracker.get_slot('confirm_cause_intake')
        
        name = tracker.get_slot('disease_name')
        if value!="None":
            if name in disease_data:
                data_file = disease_data[name]
                dispatcher.utter_message(data_file[value])
            else:
                dispatcher.utter_message(text="Invalid Name")

        return []




class ActionResetValues(Action):
    def name(self) -> Text:
        return "action_reset_values"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[EventType]:

        dispatcher.utter_message("Resetting defined values...")

        return [AllSlotsReset()]


class ActionRename(Action):
    def name(self) -> Text:
        return "action_rename"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[EventType]:

        SlotSet("person_name", None)
        dispatcher.utter_message("Enter your name: ")

        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'person_name':
                name = blob['value']
                return [SlotSet("person_name", name)]


