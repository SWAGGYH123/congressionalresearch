import pandas as pd
import json
import os

path = 'null'
dirs = os.listdir(path)


js_folder_path=os.path.join('null')

js = [x for x in dirs if x.endswith('.json')]
for js in js:
  js_path = os.path.join(js_folder_path, js)
  with open(js_path,'r') as f: 
    data = json.loads(f.read())
    multiple_level_data = pd.json_normalize(data, record_path=['bill','sponsors'], meta=[['request','billUrl'],['bill','title'],['bill','congress'],['bill','number'],['bill','originChamber'],['bill','cosponsors','count'],['bill','policyArea','name']], errors='ignore', meta_prefix='record_', record_prefix='sponsor_')
    multiple_level_data.to_excel(f'{path}/{js}converted.xlsx', index=True)

df = pd.DataFrame()
for file in dirs:
     if file.endswith('.xlsx'):
         df = df.append(pd.read_excel(file, engine='openpyxl'), ignore_index=True) 
df.to_excel("AllBillsInOneExcel.xlsx")
