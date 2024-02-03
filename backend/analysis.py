import pandas as pd
import numpy as np
import zipfile
import os

with zipfile.ZipFile("job_output/artifacts.zip", 'r') as zip_ref:
    zip_ref.extractall("job_output")

dir = "backend/job_output/file-0-video1124829211.mp4/csv/video1124829211.mp4"
os.chdir(dir)

