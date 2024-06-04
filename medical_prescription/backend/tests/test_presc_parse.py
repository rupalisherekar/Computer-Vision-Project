from  backend.src.presc_parse import Prescription_Parser
import pytest

@pytest.fixture()
def doc_1_Virat():
    doc_text='''Dr John >mith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    | Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times'''
    return Prescription_Parser(doc_text)

@pytest.fixture()
def doc_2_Marta():
    doc_text='''Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    K
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mig every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month
    Refill: 2 times'''
    return Prescription_Parser(doc_text)

def test_get_name(doc_1_Virat,doc_2_Marta):
    assert doc_1_Virat.parse('Name')=='Virat Kohli'
    assert doc_2_Marta.parse('Name') == 'Marta Sharapova'

def test_get_Address(doc_1_Virat,doc_2_Marta):
    assert doc_1_Virat.parse('Address')=='2 cricket blvd, New Delhi'
    assert doc_2_Marta.parse('Address') == '9 tennis court, new Russia, DC'

def test_get_Medicines(doc_1_Virat,doc_2_Marta):
    assert doc_1_Virat.parse('Medicines')=='| Omeprazole 40 mg'
    assert doc_2_Marta.parse('Medicines') == '''K\n    Prednisone 20 mg\n    Lialda 2.4 gram'''

def test_get_Directions(doc_1_Virat,doc_2_Marta):
    assert doc_1_Virat.parse('Directions')=='Use two tablets daily for three months'
    assert doc_2_Marta.parse('Directions') == '''Prednisone, Taper 5 mig every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take 2 pill everyday for 1 month'''

def test_get_Refill(doc_1_Virat,doc_2_Marta):
    assert doc_1_Virat.parse('Refill')=='3'
    assert doc_2_Marta.parse('Refill') == '2'


