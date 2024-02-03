from flask import Flask, request
from flask_cors import CORS
import os
import time
# import complete_analysis from main_analysis
from main_analysis import complete_analysis

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No file part', 400

    file = request.files['video']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = file.filename
        file.save(os.path.join('user_data/', filename))

        # Accessing additional form data
        whoSpokeFirst = request.form.get('whoSpokeFirst')
        whoIsOnTheLeft = request.form.get('whoIsOnTheLeft')

        # print("Who Spoke First:", whoSpokeFirst)
        # print("Interviewer Position:", whoIsOnTheLeft)

        time.sleep(3)
        # RUN COMPLETE ANALYSIS
        complete_analysis(filename, whoSpokeFirst, whoIsOnTheLeft)
        return 'File uploaded successfully', 200

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5001)
