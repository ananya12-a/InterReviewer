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


interviewee = pd.read_csv("weights/interviewee.csv")
interviewer = pd.read_csv("weights/interviewer.csv")

print (pd.DataFrame.head(interviewee))