import os
import json

#written with the help of Joel Osher

DIR = os.curdir + "/Cosponsor/"

path = os.listdir(DIR)

def filter_jsons(x):
    return x[-5:] == ".json"


def filter_congress(x, i):
    return x[:3] == i


def bipartisan(p):
    if (("D" in p) or ("ID" in p) or ("I" in p)) and (("R" in p) or ("L" in p)):
        return True

jsons = list(filter(filter_jsons, path))
only_111 = list(filter(lambda x: filter_congress(x, "111"), jsons))
only_112 = list(filter(lambda x: filter_congress(x, "112"), jsons))
only_113 = list(filter(lambda x: filter_congress(x, "113"), jsons))
only_114 = list(filter(lambda x: filter_congress(x, "114"), jsons))
only_115 = list(filter(lambda x: filter_congress(x, "115"), jsons))
only_116 = list(filter(lambda x: filter_congress(x, "116"), jsons))

def check_congress(n):
    counter = 0
    for i in n:
        with open(DIR + i, 'r') as x:
            x_parsed = json.load(x)
            parties = []
            for j in x_parsed['cosponsors']:
                parties.append(j['party'])
            if bipartisan(parties):
                counter += 1
    return counter

print("Congress 111: " + str(check_congress(only_111)))
print("Congress 112: " + str(check_congress(only_112)))
print("Congress 113: " + str(check_congress(only_113)))
print("Congress 114: " + str(check_congress(only_114)))
print("Congress 115: " + str(check_congress(only_115)))
print("Congress 116: " + str(check_congress(only_116)))
