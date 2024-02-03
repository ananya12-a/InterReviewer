import pandas as pd
import numpy as np
import zipfile
import os

# with zipfile.ZipFile("job_output/artifacts.zip", 'r') as zip_ref:
#     zip_ref.extractall("job_output")

dir = "job_output/file-0-video1318490298.mp4/csv/video1318490298.mp4"
os.chdir(dir)

face = pd.read_csv("face.csv")
prosody = pd.read_csv("prosody.csv")


## face dataset processing
emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']

face_0 = face[face["Id"] == "face_0"]
face_0_emotions = face_0[emotions].T
face_1 = face[face["Id"] == "face_1"]
face_1_emotions = face_1[emotions].T

face_0_emotions['average'] = face_0_emotions.mean(numeric_only=True, axis=1)
face_0_emotions['std'] = face_0_emotions.std(numeric_only=True, axis=1)
face_0_emotions.sort_values(by=['average'], inplace=True, ascending=False)

face_1_emotions['average'] = face_1_emotions.mean(numeric_only=True, axis=1)
face_1_emotions['std'] = face_1_emotions.std(numeric_only=True, axis=1)
face_1_emotions.sort_values(by=['average'], inplace=True, ascending=False)

# print(face_0_emotions.head())

print(prosody.columns)

def process(df, id):
    new_df = df[df["Id"] == id]
    new_df = new_df[emotions].T
    new_df['average'] = new_df.mean(numeric_only=True, axis=1)
    new_df['std'] = new_df.std(numeric_only=True, axis=1)
    new_df.sort_values(by=['average'], inplace=True, ascending=False)
    return new_df