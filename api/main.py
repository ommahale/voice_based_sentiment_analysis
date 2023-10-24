from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import librosa
import keras
import uvicorn
import sys

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:3000"
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model=keras.models.load_model('model.h5')
print("Model loaded")

def extract_mfcc(filename):
    y,sr=librosa.load(filename,duration=3,offset=0.5)
    mfcc=np.mean(librosa.feature.mfcc(y=y,sr=sr,n_mfcc=40).T,axis=0)
    return mfcc.reshape(1,40,1)

@app.get("/")
def init():
    return {"Hello": "World"}

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    mfcc=extract_mfcc(file.file)
    for i in model.predict(mfcc):
        probab=max(i.tolist())
        res=np.argmax(i)
        dict={'angry😠':0,'disgust🤮':1,'fear😓':2,'happy😄':3,'neutral🙂':4,'ps😇':5,'sad😞':6}
        value = [i for i in dict if dict[i]==res]
        output=value[0] 
    return {"result": output, "probability": probab}

if __name__ == "__main__":
    print(sys.argv)
    host, port  = sys.argv[1:]
    uvicorn.run(app, host=host, port=int(port))