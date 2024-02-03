import pandas as pd
import numpy as np
import zipfile
import os

with zipfile.ZipFile("job_output/artifacts.zip", 'r') as zip_ref:
    zip_ref.extractall("job_output")

dir = "job_output/file-0-video1318490298.mp4/csv/video1318490298.mp4"
os.chdir(dir)

