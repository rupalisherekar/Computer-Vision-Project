from fastapi import FastAPI,File,UploadFile,Form
import uvicorn
from extractor import extract
from enum import Enum
import uuid
import os

app=FastAPI()

# @app.get("/hello/{name}")
# async def hello(name):
#     return f'welcome {name}'



# food_items={'Indian':{'paneer','wada','puranpoli','dosa'},
#             'Italian':{'pasta','pizza','ravioli'}}
#
# class AvailableCuisines(str,Enum):
#     Indian='Indian'
#     Italian='Italian'



disc_types={1:'10%',
     2:'20%',
     3:'30%'}



@app.post('/extract_from_doc')
def extract_from_doc(file:UploadFile=File(...)
                     ,file_format:str=Form(...)
                     ):
    try:
        content=file.file.read()
        file_path='../tests/uploads/'+str(uuid.uuid4())+'.pdf'
        with open(file_path,'wb') as f:
            f.write(content)
        data=extract(file_path,file_format)
        if os.path.exists(file_path):
            os.remove(file_path)
        return data
    except Exception as e:
        return {'error':str(e)}






   # return disc_types[code]



if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

