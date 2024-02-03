import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import scipy.stats as stats

def call_chatgpt(input):
    # Load environment variables from the .env file
    load_dotenv()

    client = OpenAI(
        # This is the default and can be omitted
        #api_key=os.environ.get("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"),
        api_key=os.getenv("OPENAI_API_KEY")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content

def get_recommendations(filename, spokeFirst, onLeft):
    dir = "job_output/file-0-"+filename+"/csv/"+filename+"/"

    face = pd.read_csv(dir+"face.csv")
    prosody = pd.read_csv(dir+"prosody.csv")

    if(onLeft == "Interviewer"):
        viewer_face = "0"
    else:
        viewer_face = "1"
    
    if(spokeFirst == "Interviewer"):
        viewee_pros = "1"
    else:
        viewer_face = "1"
    
    ## dataset processing
    emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']
    neg_emotions = ['Boredom','Confusion','Disappointment','Doubt','Surprise (negative)']

    def process(df, id, sort="average"):
        new_df = df[df["Id"] == id]
        new_df = new_df[emotions]
        new_df = stats.zscore(new_df, axis=0)
        new_df = new_df[neg_emotions]
        return new_df
    
    face_viewer = process(face, "face_"+viewer_face)
    threshold = 1
    # Count the number of columns that meet the threshold condition for each row
    condition_met_count = face_viewer.gt(threshold).sum(axis=1)

    # Filter rows where at least 3 columns meet the threshold condition
    filtered_df = face_viewer[condition_met_count >= 3]
    frames_idx = filtered_df.index.to_list()

    time_stamps = face.loc[frames_idx]['Time']

    interviewee_prosody = prosody[prosody["Id"] == "spk_"+viewee_pros]
    interviewee_prosody[["Text", "BeginTime","EndTime"]]

    overlap = {}
    for index, row in interviewee_prosody.iterrows():
        overlap[index] = 0
        for time in time_stamps:
            if(time >= row["BeginTime"] and time <= row["EndTime"]): overlap[index] += 1
    
    max_overlap = max(overlap, key=overlap.get)
    return filtered_df.columns, interviewee_prosody["Text"][max_overlap]
    
def gpt_recs(filename, spokeFirst, onLeft):
    emotions_list, transcript = get_recommendations(filename, spokeFirst, onLeft)
    emotions = ', '.join(emotions_list)
    print(emotions)
    print(transcript)

    input = "I said \""+transcript+"\" in my interview and my interviewer showed "+emotions+". How can I improve?"
    return_message = call_chatgpt(input)
    print(return_message)

# gpt_recs("video1318490298.mp4","Interviewer","Interviewer")
 