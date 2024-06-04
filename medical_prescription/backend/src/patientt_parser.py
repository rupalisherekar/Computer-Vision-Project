import Generic_extractor as ge
import re

text1='''17/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight’
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Casc of Emergency
7 ee
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone

Genera! Medical History

a

a

a ea A CE i a

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?
No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

CO
aa
'''


text2='''Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020

'''

class Patient_Parser(ge.Medical_Doc_Parser):
    def __init__(self,text):
        ge.Medical_Doc_Parser.__init__(self,text)

    def parse_all(self):
        return {'Name':self.parse('Name'),
                'Phone':self.parse('Phone'),
                'Vaccine':self.parse('Vaccine'),
                'Medical_Condition':self.parse('Medical_Condition')
        }

    def parse(self,field):
        data={'Name':{'pattern':'Date\n+(.*) [Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]','flags':0},
            'Vaccine':{'pattern':'vaccination\?\n+(.*)\n', 'flags': 0},
            'Phone':{'pattern':'\(\d{3}\) \d{3}-\d{4}','flags':0},
            'Medical_Condition':{'pattern':'headaches[\)|\}]\:\n*(.*)','flags':0}
        }

        #pattern_objects=self.parse_all()
        pattern_object=data[field]
        if pattern_object:
            pattern=pattern_object['pattern']
            flag=pattern_object['flags']
            matches=re.findall(pattern,self.text,flags=flag)
            return(matches[0].strip())


p=Patient_Parser(text2)
p.parse_all()





