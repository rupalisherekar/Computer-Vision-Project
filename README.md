# Computer-Vision-Project
This is an API that uses computer vision to read fields from pdf files. The language used is Python and thelearning stacks are :
* pdf_to_image: obviously for converting pdf to image
* cv2 : for image processing(grayscale, adaptive thresholding and resizing)
* pytessaract: for conversion of image to string(read contents of image)
* re: to search  for patterns using regular expressions
* FastApI,uvicorn:web framewwork
* uuid: for generation of unique file names
* Postman: for testing get and put requests
   #### This API reads fields from prescription files and patient data files. Images with black shadows are handled using adaptive thresholding.
