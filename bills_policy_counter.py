import pandas as pd
import json
import os
from collections import Counter

path = 'null'
dirs = os.listdir(path)


js_folder_path=os.path.join('null')
counter111 = Counter()
counter112=Counter()
counter113=Counter()
counter114=Counter()
counter115=Counter()
counter116=Counter()
js = [x for x in dirs if x.endswith('.json')]
for js in js:
  js_path = os.path.join(js_folder_path, js)
  with open(js_path,'r') as f: 
    data = json.loads(f.read())
    if data['request']['congress']=='111':
      try:
        counter111[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)
    if data['request']['congress']=='112':
      try:
        counter112[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)
    if data['request']['congress']=='113':
      try:
        counter113[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)
    if data['request']['congress']=='114':
      try:
        counter114[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)
    if data['request']['congress']=='115':
      try:
        counter115[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)
    if data['request']['congress']=='116':
      try:
        counter116[(data['bill']['policyArea']['name'])] += 1
      except KeyError:
        print(js_path)

print('Congress 111:')
print(counter111)
print("Congress 112:") 
print(counter112)
print("Congress 113:")
print(counter113)
print("Congress 114:")
print(counter114)
print("Congress 115:")
print(counter115)
print("Congress 116:")
print(counter116)
