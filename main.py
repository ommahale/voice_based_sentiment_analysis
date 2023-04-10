from fastapi import FastAPI, File, UploadFile
import numpy as np
import librosa
import keras
app = FastAPI()

model=keras.models.load_model('model.h5')

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
        dict={'angry':0,'disgust':1,'fear':2,'happy':3,'neutral':4,'ps':5,'sad':6}
        value = [i for i in dict if dict[i]==res]
        output=value[0] 
    return {"result": output, "probability": probab}