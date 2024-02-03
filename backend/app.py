from flask import Flask, request,send_from_directory
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
        time.sleep(3)
        # RUN COMPLETE ANALYSIS
        complete_analysis(filename, whoSpokeFirst, whoIsOnTheLeft)
        return 'File uploaded successfully', 200


@app.route('/face_viewee_barplot.csv')
def serve_face_viewee_barplot():
    return send_from_directory('plot_data', 'face_viewee_barplot.csv')

@app.route('/face_viewer_barplot.csv')
def serve_face_viewer_barplot():
    return send_from_directory('plot_data', 'face_viewer_barplot.csv')

@app.route('/pros_viewee_barplot.csv')
def serve_pros_viewee_barplot():
    return send_from_directory('plot_data', 'pros_viewee_barplot.csv')

@app.route('/pros_viewer_barplot.csv')
def serve_pros_viewer_barplot():
    return send_from_directory('plot_data', 'pros_viewer_barplot.csv')

@app.route('/face_viewer_tl.csv')
def serve_face_viewer_tl():
    return send_from_directory('plot_data', 'face_viewer_tl.csv')

@app.route('/face_viewee_tl.csv')
def serve_face_viewee_tl():
    return send_from_directory('plot_data', 'face_viewee_tl.csv')


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5001)
