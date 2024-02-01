# voice_based_sentiment_analysis
Deep Learning project for predicting emotions from voice using Tensorflow and Liberosa
## Introduction
This project is backend for a voice based sentiment analysis application. The application is built using Tensorflow and Librosa. The model is trained on the Toronto Emotional Speech Set (TESS) dataset from Kaggle. The model is trained to predict 8 emotions namely angry, calm, fearful, happy, sad, surprised, neutral and disgust. The model is trained using a LTSM architecture. The model is trained on 5600 audio files. The model is trained for 100 epochs. The model is trained on a Local GPU Nvidia GForce 1660 Ti. The model is saved in the form of h5 file. The api is simply created using fast api
## Installation
Create a virtual environment using the following command
```bash
virtualenv venv
```
Activate the virtual environment
Windows:
```bash
venv\Scripts\activate
```
Linux:
```bash
source venv/bin/activate
```
MacOS:
```bash
source venv/bin/activate
```
Install the dependencies
```bash
pip install -r requirements.txt
```
## Usage
Run the following command to start the server
```bash
uvicorn main:app --reload
```
The server will start on port 8000. The api can be accessed using the following url
http://localhost:8000/swagger. This will open the swagger ui. The api can be tested using the 
