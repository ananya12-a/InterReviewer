from flask import Flask, request
from flask_cors import CORS
import os

 

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes
 

@app.route('/')

def hello():

    return 'Hello from Flask!'


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
        return 'File uploaded successfully', 200


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5001)   