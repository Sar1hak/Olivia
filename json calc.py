
import pandas as pd
import json


df = pd.read_excel("Chicheck_Tongue_Chatbot.xlsx", sheet_name='Symptom', na_filter=False)
#df = df.replace(r'^\s*$', "qqq", regex=True)

data={}
rows = df.shape[0]
print( df["name"][0].lower())

for i in range(rows):
    #data[df["name"][i].lower()] = []
    data[df["name"][i].lower()]={
        "key": df["name"][i],
        "link": df["link"][i],
        "symptoms": df["symptoms"][i].strip('][').split(', '),
        "causes": df["causes"][i].strip('][').split(', '),
        "risk_factor": df["risk_factor"][i].strip('][').split(', '),
        "overview": df["overview"][i].strip('][').split(', '),
        "treatment": df["treatment"][i].strip('][').split(', '),
        "medication": df["medication"][i].strip('][').split(', '),
        "home_remedies": df["home_remedies"][i].strip('][').split(', ')
    }

with open('diseasesdb.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)



'''
import pandas as pd
import json

df = pd.read_excel("Chicheck_Tongue_Chatbot.xlsx", sheet_name='Symptom', na_filter=False)
#df = df.replace(r'^\s*$', "qqq", regex=True)
data={}
data['disease'] = []
rows = df.shape[0]
#symptoms=df["symptoms"][1]
#print(symptoms)
#a=symptoms.strip('][').split(', ')
#print(a)
for i in range(rows):
    
    data['disease'].append({
        "key": df["name"][i],
        "link": df["link"][i],
        "symptoms": df["symptoms"][i].strip('][').split(', '),
        "causes": df["causes"][i].strip('][').split(', '),
        "risk_factor": df["risk_factor"][i].strip('][').split(', '),
        "overview": df["overview"][i].strip('][').split(', '),
        "treatment": df["treatment"][i].strip('][').split(', '),
        "medication": df["medication"][i].strip('][').split(', '),
        "home_remedies": df["home_remedies"][i].strip('][').split(', ')
    })

with open('diseasesdb.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
'''
'''
# find a key
if any(tag['key'] == 'ecs_scaling' for tag in data['Tags']):
    #code
'''
