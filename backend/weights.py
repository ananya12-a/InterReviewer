import openai
import pandas as pd
import numpy as np
import os
import json


# os.environ["OPENAI_API_KEY"] = "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"
# # write code to connect each header1 with header2

# client = openai.OpenAI()
# def get_relevance(role, criteria, emotion):
    
#     response_text = client.chat.completions.create(
#       model="gpt-3.5-turbo",
#       messages=[
#           {"role": "user", "content": f"Rate the importance of {emotion} during a job interview for the {role} on a scale from -1 to 1. Only give me the decimal value. For example, 0.5."}
#           ],
#       max_tokens=60,
#       # temperature=0.0
#     )
#     response_text = str(response_text)


#     return response_text

# def parse(response_text):
#    # Find the index of "content='"
#     start_index = response_text.find("content='") + len("content='")

#     # Find the index of the closing single quote after the content
#     end_index = response_text.find("'", start_index)

#     # Extract the numeric value as a substring
#     content_numeric = response_text[start_index:end_index]

#     return content_numeric

# emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']
# interviewer_categories = [
#     "Candidate Perception",
#     "Emotional Responsiveness",
#     "Interviewer Bias",
#     "Engagement Level",
#     "Stress Induction",
#     "Patience and Tolerance",
#     "Encouragement and Support",
#     "Openness to Interaction",
#     "Empathy and Understanding"
# ]

# interviewee_categories = [
#     "Stress and Anxiety",
#     "Confidence and Self-assurance",
#     "Engagement with the Interviewer",
#     "Adaptability and Reactiveness",
#     "Passion and Motivation",
#     "Professionalism and Maturity",
#     "Empathy and Social Skills",
# ]


# data_interviewer = np.zeros((len(emotions), len(interviewer_categories)))
# data_interviewee = np.zeros((len(emotions), len(interviewee_categories)))
# for indx1, emot in enumerate(emotions):
#     for indx2, crit in enumerate(interviewer_categories):
#         print(emot, crit)
#         response = get_relevance("interviewer", crit, emot)
#         parsed = parse(response)
#         try:
#           data_interviewer[indx1, indx2] = parsed
#         except:
#           data_interviewer[indx1, indx2] = -1
#           print(response, parsed)
#     for indx2, crit in enumerate(interviewee_categories):
#         print(emot, crit)
#         response = get_relevance("interviewee", crit, emot)
#         parsed = parse(response)
#         try:
#           data_interviewee[indx1, indx2] = parsed
#         except:
#           data_interviewee[indx1, indx2] = -1
#           print(response, parsed)

# # np.save('disease_measure_weights.npy', data)

# # data = np.load('disease_measure_weights.npy')
# np.savetxt("weights/interviewer.csv", data_interviewer, delimiter=",")
# np.savetxt("weights/interviewee.csv", data_interviewee, delimiter=",")

def weights_anal(filename, spokeFirst, onLeft):
    if(onLeft == "Interviewee"):
        interviewer_index_face = 1
    else:
        interviewer_index_face = 0
    
    if(spokeFirst == "Interviewee"):
        interviewer_index_pros = 1
    else:
        interviewer_index_pros = 0

    interviewee = np.loadtxt("weights/interviewee.csv",delimiter=",", dtype=np.float64)
    interviewer = np.loadtxt("weights/interviewer.csv",delimiter=",", dtype=np.float64)

    emotions = ['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Concentration', 'Contemplation', 'Confusion', 'Contempt', 'Contentment', 'Craving', 'Determination', 'Disappointment', 'Disgust', 'Distress', 'Doubt', 'Ecstasy', 'Embarrassment', 'Empathic Pain', 'Entrancement', 'Envy', 'Excitement', 'Fear', 'Guilt', 'Horror', 'Interest', 'Joy', 'Love', 'Nostalgia', 'Pain', 'Pride', 'Realization', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Desire', 'Shame', 'Surprise (negative)', 'Surprise (positive)', 'Sympathy', 'Tiredness', 'Triumph']
    interviewer_cat = ['Candidate Perception',	'Engagement Level',	'Patience and Tolerance']
    interviewee_cat = [	'Stress and Anxiety',	'Confidence and Self-assurance',	'Passion and Motivation',	'Professionalism and Maturity']
    interviewer_cat = np.array(interviewer_cat)
    interviewee_cat = np.array(interviewee_cat)

    dir = "job_output/file-0-"+filename+"/csv/"+filename+"/"

    # Read the CSV files
    face = pd.read_csv(dir + "face.csv")
    prosody = pd.read_csv(dir + "prosody.csv")

    def save_json(face, modelName, id_names, interviewer_index):
        # Filter and transpose the data
        assert(len(id_names) == 2)
        face_0 = face[face["Id"] == id_names[0]]
        face_0_emotions = face_0[emotions].T
        face_1 = face[face["Id"] == id_names[1]]
        face_1_emotions = face_1[emotions].T

        # Convert to numpy arrays and ensure numeric types
        face_0_emotions = face_0_emotions.apply(pd.to_numeric, errors='coerce').to_numpy()
        face_1_emotions = face_1_emotions.apply(pd.to_numeric, errors='coerce').to_numpy()

        # Perform matrix multiplication
        if interviewer_index==1:
            print(face_0_emotions.shape, interviewee.shape)
            weights_interviewee = np.matmul(face_0_emotions.T, interviewee)
            weights_interviewer = np.matmul(face_1_emotions.T, interviewer)
        else:
            weights_interviewee = np.matmul(face_1_emotions.T, interviewee)
            weights_interviewer = np.matmul(face_0_emotions.T, interviewer)

        frames_interviewer = np.argmax(weights_interviewer, axis=1)
        frames_interviewee = np.argmax(weights_interviewee, axis=1)

        unique_numbers_interviewer, count_interviewer = np.unique(frames_interviewer, return_counts=True)
        unique_numbers_interviewee, count_interviewee = np.unique(frames_interviewee, return_counts=True)

        interviewer_weights = {}
        interviewee_weights = {}

        for number, count in zip(unique_numbers_interviewer, count_interviewer):
            print(f"The interviewer displayed {interviewer_cat[number]} for {count/len(frames_interviewer) * 100}% of the time")
            interviewer_weights[interviewer_cat[number]]=(count/len(frames_interviewer)).round(2)
        print("\n")
        for number, count in zip(unique_numbers_interviewee, count_interviewee):
            print(f"The interviewee displayed {interviewee_cat[number]} for {count/len(frames_interviewee) * 100}% of the time")
            interviewee_weights[interviewee_cat[number]]=(count/len(frames_interviewee)).round(2)
        print("\n")
        print("\n")
        with open(f'user_weights/interviewer_weight_analysis_{str(modelName)}.json', 'w') as json_file:
            json.dump(interviewer_weights, json_file, indent=4)

        with open(f'user_weights/interviewee_weight_analysis_{str(modelName)}.json', 'w') as json_file:
            json.dump(interviewee_weights, json_file, indent=4)

    save_json(face, "face", ["face_0", "face_1"], interviewer_index_face)
    save_json(prosody, "prosody", ["spk_0", "spk_1"], interviewer_index_pros)