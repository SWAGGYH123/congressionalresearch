import pandas as pd
import json
import os
from collections import Counter

path = 'null'
dirs = os.listdir(path)

js_folder_path=os.path.join('null')

average111 = Counter()
average112=Counter()
average113=Counter()
average114=Counter()
average115=Counter()
average116=Counter()
cntr=[0]*6
count=Counter()
js = [x for x in dirs if x.endswith('.json')]
for js in js:
  js_path = os.path.join(js_folder_path, js)
  with open(js_path,'r') as f: 
    data = json.loads(f.read())
    if 'request' not in data.keys(): continue
    if data['request']['congress']=='111':
      try:
        cntr[0]+=1
        for item in data['cosponsors']:
          average111[(item['party'])] += 1
      except KeyError as e:
        print(js_path)
    if data['request']['congress']=='112':
      try:
        cntr[1]+=1
        for item in data['cosponsors']:
          average112[(item['party'])] += 1
      except KeyError as e:
        print(js_path)
    if data['request']['congress']=='113':
      try:
        cntr[2]+=1
        for item in data['cosponsors']:
          average113[(item['party'])] += 1
      except KeyError as e:
        print(js_path)
    if data['request']['congress']=='114':
      try:
        cntr[3]+=1
        for item in data['cosponsors']:
          average114[(item['party'])] += 1
      except KeyError as e:
        print(js_path)
    if data['request']['congress']=='115':
      try:
        cntr[4]+=1
        for item in data['cosponsors']:
          average115[(item['party'])] += 1
      except KeyError as e:
        print(js_path)
    if data['request']['congress']=='116':
      try:
        cntr[5]+=1
        for item in data['cosponsors']:
          average116[(item['party'])] += 1
      except KeyError as e:
        print(js_path)

print('Congress 111:')
print(average111)
print("Congress 112:") 
print(average112)
print("Congress 113:")
print(average113)
print("Congress 114:")
print(average114)
print("Congress 115:")
print(average115)
print("Congress 116:")
print(average116)

print(cntr)   
