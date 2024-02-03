import pandas as pd 
import numpy as np
import scipy.stats as stats

def superlatives(filename, spokeFirst):
    
    if(spokeFirst == "Interviewee"):
        viewee_index_pros = "0"
    else:
        viewee_index_pros = "1"

    interviewee = np.loadtxt("weights/interviewee.csv",delimiter=",", dtype=np.float64)

    emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']
    interviewee_cat = [	'Stress and Anxiety',	'Confidence and Self-assurance',	'Passion and Motivation',	'Professionalism and Maturity']
    interviewee_cat = np.array(interviewee_cat)

    dir = "job_output/file-0-"+filename+"/csv/"+filename+"/"

    # Read the CSV files
    prosody = pd.read_csv(dir + "prosody.csv")

    pros_interviewee = prosody[prosody["Id"] == "spk_"+viewee_index_pros]

    pros_interviewee_emotions = pros_interviewee[emotions]
    pros_ee_emo = pros_interviewee_emotions.apply(pd.to_numeric, errors='coerce').to_numpy()

    weights_interviewee = np.matmul(pros_ee_emo, interviewee)

    WI_z_row = stats.zscore(weights_interviewee, axis=0)
    WI_z_col = stats.zscore(WI_z_row, axis=1)

    df = pd.DataFrame(WI_z_col, columns=interviewee_cat, index=pros_interviewee["Text"])
    print(df.iloc[:, 0:2])


superlatives("video1318490298.mp4", "Interviewer")

