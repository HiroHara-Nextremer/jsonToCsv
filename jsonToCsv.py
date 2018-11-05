#!usr/bin/env python 

import json 
import codecs
import pprint
import csv 


"""
input_file = file(raw_input(), "r")
f = json.loads(input_file.read())
res_body = f['body']
print(pprint(res_body).decode("unicode-escape"))
"""
def load_ranking():
    with open("word_ranking.json", "r") as f:
        return json.load(f)['body']

print(load_ranking())

def convert_to_csv(load_ranking):
    load_ranking()
