import os
import glob
import datetime
from dateutil.parser import *
from numpy import rint
import pandas as pd
import locale

locale.setlocale(locale.LC_TIME, "pt_BR")

def total_time(start_time, end_time, dia_da_semana):
    if (dia_da_semana >= 5 or (start_time.hour >= 18 and start_time.minute >= 0) or (start_time.hour <= 9)):
       return str(datetime.timedelta(seconds = (end_time-start_time).total_seconds()))
    else:
        if (start_time.hour < 18):
            start_time.replace(hour=18, minutes=00, seconds=00)
            return str(datetime.timedelta(seconds = (end_time-start_time).total_seconds()))  

input_path = r'data\input'
output_path = r'data\output'

files = glob.glob( input_path +"\*.csv");
print("Choose a file:")
i = 0
for file in files:
    file_name = file.split("\\")
    print(f'index: {i} filename: {file_name[1:][1:]}');
    i+=1

index = int(input("Choose your file by its index\n"))
print(f'Index choosen {index} - filepath: {files[index]}')

df = pd.read_csv (files[index], sep=',')

"""
'activity', 'project', 'workers', 'duration', 'time','duration_seconds', 'keyboard_hits', 'mouse_clicks', 'screenshot_count','start_time', 'end_time'
"""

intervals = []
for index, row in df.iterrows():
    start_time = parse(row['start_time'])
    end_time = parse(row['end_time'])
    if (start_time.hour >= 18 and start_time.minute >= 0) or (start_time.hour <= 9) or start_time.weekday() >= 5:
        intervals.append({'iníco':df.loc[index]['start_time'], 'fim':df.loc[index]['end_time'],'total_em_horas':total_time(start_time,end_time,end_time.weekday()) ,'dia_da_semana':end_time.strftime('%A')})
    elif (end_time.hour >= 18 and end_time.minute >= 0) or end_time.hour <= 9  or start_time.weekday() >= 5:
        intervals.append({'iníco':df.loc[index]['start_time'], 'fim':df.loc[index]['end_time'],'total_em_horas':total_time(start_time,end_time,end_time.weekday()) ,'dia_da_semana':end_time.strftime('%A')})

df_ii = pd.DataFrame(intervals)
filename = r'data/output/horasExtras_' +  datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.xlsx'
df_ii.to_excel(filename, index=False)