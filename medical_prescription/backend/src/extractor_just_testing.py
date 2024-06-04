from pdf2image import  convert_from_path
import util
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from PIL import Image

POPPLER_PATH=r'C:\poppler-24.02.0\Library\bin'
pages=convert_from_path('../resources/pd_2.pdf',poppler_path=POPPLER_PATH)
img=util.process_image(pages[0])

#Image.fromarray(img).show()
#print(type(img))
#doc=''
#for page in pages:
text=pytesseract.image_to_string(img)
    #doc+=text
print(text)
