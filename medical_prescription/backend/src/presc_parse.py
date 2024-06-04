import backend.src.Generic_extractor as ge
import re
import backend.src.util

class Prescription_Parser(ge.Medical_Doc_Parser):
    def __init__(self,text):
        ge.Medical_Doc_Parser.__init__(self,text)

    def parse_all_fields(self):
        return{'Patient Name':self.parse('Name'),
               'Patient Address': self.parse('Address'),
               'Patient Medicines': self.parse('Medicines'),
               'Patient Directions': self.parse('Directions'),
               'Patient Refill': self.parse('Refill'),
               }

    def parse(self,field):
        field=field.capitalize()
        data={'Name':{'pattern':'Name:(.*)Date','flags':0},
                  'Date':{'pattern':'Date:(.*)\n','flags':0},
                  'Address':{'pattern':'Address:(.*)\n','flags':0},
                  'Medicines':{'pattern':'Address:[^\n]*(.*)Directions','flags':re.DOTALL},
                  'Directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
                  'Refill': {'pattern': 'Refill:(.*)times', 'flags': 0},
            }
        pattern_object=data[field]
        if pattern_object:
            match=re.findall(pattern_object['pattern'],self.text,flags=pattern_object['flags'])
            if len(match)>0:
                return match[0].strip()




