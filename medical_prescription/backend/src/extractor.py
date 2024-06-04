from pdf2image import  convert_from_path
import pytesseract
import util
import presc_parse as pp
import patientt_parser as ptp
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
#from PIL import Image

POPPLER_PATH=r'C:\poppler-24.02.0\Library\bin'

def extract(file_name,file_type):
        # convert pdf pages to images
        pages=convert_from_path(file_name,poppler_path=POPPLER_PATH)
        document=''
# read pdf convert to gray scale image, also use adaptive thresholding,then convert to string
        if len(pages)>0:
          page=pages[0]
          gray_scale_image = util.process_image(page)
          text=pytesseract.image_to_string(gray_scale_image,lang='eng')
          document+='\n'+text
        #parse the string , use regex to find fields in the document
        if file_type == 'prescription':
            txt = pp.Prescription_Parser(document)
            return(txt.parse_all_fields())
        elif file_type=='patient-details':
            txt = ptp.Patient_Parser(document)
            return(txt.parse_all())
        else:
            raise Exception("Invalid file format")



if __name__=='__main__':
    doc=extract('../resources/pd_2.pdf','patient-details')
    print(doc)

