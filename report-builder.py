import os
import glob
from datetime import datetime
import pandas as pd


input_path = r'data\input'
output_path = r'data\output'

files = glob.glob( input_path +"\*.csv");
print("Choose a file:")
for file in files:
    i = 0
    file_name = file.split("\\")
    print(f'index: {i} filename: {file_name[1:][1:]}');
    i+=1

index = int(input("Choose your file by its index\n"))
print(f'Index choosen {index} - filepath: {files[index]}')

df = pd.read_csv (files[index], sep=',')

"""
'activity', 'project', 'workers', 'duration', 'time','duration_seconds', 'keyboard_hits', 'mouse_clicks', 'screenshot_count','start_time', 'end_time'
"""

