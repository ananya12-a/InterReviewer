import pandas as pd
import numpy as np
import zipfile
import os

# with zipfile.ZipFile("job_output/artifacts.zip", 'r') as zip_ref:
#     zip_ref.extractall("job_output")

dir = "job_output/file-0-video1318490298.mp4/csv/video1318490298.mp4/"
#os.chdir(dir)

face = pd.read_csv(dir+"face.csv")
prosody = pd.read_csv(dir+"prosody.csv")

viewer_face = "0"
viewee_face = "1"
viewer_pros = "0"
viewee_pros = "1"

## dataset processing
emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']

def process(df, id, sort="average"):
    new_df = df[df["Id"] == id]
    new_df = new_df[emotions].T
    new_df['average'] = new_df.mean(numeric_only=True, axis=1)
    new_df['std'] = new_df.std(numeric_only=True, axis=1)
    if sort:
        new_df.sort_values(by=sort, inplace=True, ascending=False)
    return new_df

face_viewer = process(face, "face_"+viewer_face)
face_viewee = process(face, "face_"+viewee_face)
pros_viewer = process(prosody, "spk_"+viewer_pros)
pros_viewee = process(prosody, "spk_"+viewee_pros)


## bar plot analysis (repeat for all)
face_viewer_bar = face_viewer[["average"]][0:5]
face_viewer_bar.to_csv("plot_data/face_0_barplot.csv")


# timeline analysis
top_viewer_emos = ["Interest", "Boredom", "Admiration", "Disappointment", "Surprise (positive)", "Surprise (negative)"]
top_viewee_emos = ["Calmness", "Excitement", "Awkwardness", "Doubt","Anxiety","Triumph"]

face_viewer_tl = face_viewer.drop(labels=['average', 'std'],axis=1)
face_viewer_tl = face_viewer_tl.loc[top_viewer_emos]
face_viewer_tl.columns = face["Time"][::2]

print(face_viewer_tl)