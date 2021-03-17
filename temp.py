data={
    "acanthosis nigricans": 
        {
            "key": "Acanthosis nigricans",
            "link": "https://www.mayoclinic.org/diseases-conditions/acanthosis-nigricans/symptoms-causes/syc-20368983",
            "symptoms": [
                "\"Skin changes are the only signs of acanthosis nigricans. You'll notice dark",
                "thickened",
                "velvety skin in body folds and creases \u2014 typically in your armpits",
                "groin and back of the neck. The skin changes usually appear slowly. The affected skin may also have an odor or itch.\"",
                "'Consult your doctor if you notice changes in your skin \u2014 especially if the changes appear suddenly. You may have an underlying condition that needs treatment.'"
            ],
            "causes": [
                "'Acanthosis nigricans has been associated with:'",
                "'Insulin resistance. Most people who have acanthosis nigricans have also become resistant to insulin. Insulin is a hormone secreted by the pancreas that allows your body to process sugar. Insulin resistance is what eventually causes type 2 diabetes.'",
                "'Hormonal disorders. Acanthosis nigricans often occurs in people who have disorders such as ovarian cysts",
                "underactive thyroids or problems with the adrenal glands.'",
                "'Certain drugs and supplements. High-dose niacin",
                "birth control pills",
                "prednisone and other corticosteroids may cause acanthosis nigricans.'",
                "'Cancer. Acanthosis nigricans also sometimes occurs with lymphoma or when a cancerous tumor begins growing in an internal organ",
                "such as the stomach",
                "colon or liver.'"
            ],
            "risk_factor": [
                "'Acanthosis nigricans risk factors include:'",
                "'Obesity. The heavier you are",
                "the higher your risk of acanthosis nigricans.'",
                "'Race. Studies show that in the United States",
                "acanthosis nigricans is more common among Native Americans.'",
                "'Family history. Some types of acanthosis nigricans appear to be hereditary.'"
            ],
            "overview": [
                "'Acanthosis nigricans is a skin condition that causes a dark discoloration in body folds and creases. It typically affects the armpits",
                "groin and neck.'",
                "'Acanthosis nigricans is a skin condition characterized by areas of dark",
                "velvety discoloration in body folds and creases. The affected skin can become thickened. Most often",
                "acanthosis nigricans affects your armpits",
                "groin and neck.'",
                "'The skin changes of acanthosis nigricans (ak-an-THOE-sis NIE-grih-kuns) typically occur in people who are obese or have diabetes. Children who develop the condition are at higher risk of developing type 2 diabetes. Rarely",
                "acanthosis nigricans can be a warning sign of a cancerous tumor in an internal organ",
                "such as the stomach or liver.'",
                "'No specific treatment is available for acanthosis nigricans. Treatment of underlying conditions may restore some of the normal color and texture to affected areas of skin.'",
                "'\\n Acanthosis nigricansAcanthosis nigricansAcanthosis nigricans is a skin condition that causes a dark discoloration in body folds and creases. It typically affects the armpits",
                "groin and neck.\\n  '"
            ],
            "treatment": [
                "'In many situations",
                "treating the underlying problem can help fade the discoloration. Examples may include:'",
                "'If you are concerned about the appearance of your skin or if the lesions become uncomfortable or start to smell bad",
                "your doctor may suggest:'",
                "\"You're likely to start by seeing your family doctor. He or she may refer you to a doctor who specializes in skin disorders (dermatologist) or hormone problems (endocrinologist). Because appointments can be brief and there's often a lot of ground to cover",
                "it's a good idea to be well-prepared for your appointment.\"",
                "'Losing weight. If your acanthosis nigricans is caused by obesity",
                "losing weight may help.'",
                "'Stopping medications or supplements. If your condition seems to be related to a medication or supplement that you use",
                "your doctor may suggest that you stop using that substance.'",
                "'Having surgery. If acanthosis nigricans was triggered by a cancerous tumor",
                "surgically removing the tumor often clears up the skin discoloration.'",
                "'Prescription creams to lighten or soften the affected areas'",
                "'Antibacterial soaps",
                "used gently",
                "as scrubbing could worsen the condition'",
                "'Topical antibiotic'",
                "'Oral acne medications'",
                "\"Laser therapy to reduce the skin's thickness\"",
                "'Losing weight.'",
                "'Stopping medications or supplements.'",
                "'Having surgery.'"
            ],
            "medication": [
                ""
            ],
            "home_remedies": [
                ""
            ]
        },
    "achalasia": 
        {
            "key": "Achalasia",
            "link": "https://www.mayoclinic.org/diseases-conditions/achalasia/symptoms-causes/syc-20352850",
            "symptoms": [
                ""
            ],
            "causes": [
                ""
            ],
            "risk_factor": [
                ""
            ],
            "overview": [
                "\"Achalasia is a rare disorder that makes it difficult for food and liquid to pass into your stomach. Achalasia occurs when nerves in the tube connecting your mouth and stomach (esophagus) become damaged. As a result",
                "the esophagus loses the ability to squeeze food down",
                "and the muscular valve between the esophagus and stomach (lower esophageal sphincter) doesn't fully relax \u2014 making it difficult for food to pass into your stomach.\"",
                "\"There's no cure for achalasia. But symptoms can usually be managed with minimally invasive therapy or surgery.\""
            ],
            "treatment": [
                "'Achalasia treatment focuses on relaxing or forcing open the lower esophageal sphincter so that food and liquid can move more easily through your digestive tract.'",
                "'Specific treatment depends on your age and the severity of the condition.'"
            ],
            "medication": [
                ""
            ],
            "home_remedies": [
                ""
            ]
        }
    
}

import json
import sys

json_str = json.dumps(data)

resp = json.loads(json_str)

#print (resp)

#print (resp['disease'])

x= (resp['acanthosis nigricans'])
print("".join(resp['acanthosis nigricans']["treatment"]))
if 'acanthosis ' in resp:
    print("HELLO")
else:
    print("sdfgh")








