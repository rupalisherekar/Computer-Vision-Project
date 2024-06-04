import pytest
import backend.src.patientt_parser as pp

@pytest.fixture()
def doc1_Kathy():
    doc_text='''17/12/2020

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
    aa'''
    return pp.Patient_Parser(doc_text)

@pytest.fixture()
def doc2_Jerry():
    doc_text='''Patient Medical Record

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
    return pp.Patient_Parser(doc_text)


def test_get_Name(doc1_Kathy,doc2_Jerry):
    assert doc1_Kathy.parse('Name')=='Kathy Crawford'
    assert doc2_Jerry.parse('Name') == 'Jerry Lucas'

def test_get_Vaccine(doc1_Kathy,doc2_Jerry):
    assert doc1_Kathy.parse('Vaccine')=='No'
    assert doc2_Jerry.parse('Vaccine') == "‘Yes"

def test_get_Phone(doc1_Kathy,doc2_Jerry):
    assert doc1_Kathy.parse('Phone')=='(737) 988-0851'
    assert doc2_Jerry.parse('Phone') == "(279) 920-8204"

def test_get_Phone(doc1_Kathy,doc2_Jerry):
    assert doc1_Kathy.parse('Medical_Condition')=='Migraine'
    assert doc2_Jerry.parse('Medical_Condition') == "N/A"

