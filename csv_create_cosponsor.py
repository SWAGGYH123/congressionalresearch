import pandas as pd
import json
import os

path = '/Users/Hugo/Desktop/Research/Research/Cosponsor'
dirs = os.listdir(path)


js_folder_path=os.path.join('/Users', 'Hugo', 'Desktop', 'Research', 'Research', 'Cosponsor')

js = [x for x in dirs if x.endswith('.json')]
for js in js:
  js_path = os.path.join(js_folder_path, js)
  with open(js_path,'r') as f: 
    data = json.loads(f.read())
    multiple_level_data = pd.json_normalize(data, record_path='cosponsors', meta=[['request','billUrl'],['pagination','count']], errors='ignore', meta_prefix='record_', record_prefix='cosponsor_')
    multiple_level_data.to_excel(f'{path}/{js}converted.xlsx', index=True)

df = pd.DataFrame()
for file in dirs:
     if file.endswith('.xlsx'):
         df = df.append(pd.read_excel(file, engine='openpyxl'), ignore_index=True) 
df.to_excel("AllCosponsorsInOneExcel.xlsx")
