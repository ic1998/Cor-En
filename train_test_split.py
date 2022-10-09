import re
import os
import xml.etree.ElementTree as ET
import numpy as np
import random

train_percent = 0.05
dev_percent = 0.01

raw_dir = "raw_datasets"
tmx_dir = "TMX_datasets"

def read_raw(base_dir):
    eng_data = []
    cor_data = []
    for x in range(1,9):
        with open(f"{base_dir}{ ('/' if base_dir and len(base_dir) > 0 else '') }{x}_ENG.txt","r") as f:
            for line in f:
                eng_data.append(line.strip())
        with open(f"{base_dir}{ ('/' if base_dir and len(base_dir) > 0 else '') }{x}_COR.txt","r") as f:
            for line in f:
                cor_data.append(line.strip())

    return cor_data,eng_data


def read_tmx(base_dir):
    eng_data = []
    cor_data = []
    for f in os.listdir(base_dir):
        try:
            tree = ET.parse(f"{base_dir}/{f}")
        except:
            continue
        root = tree.getroot()
        nodes = root.findall(".//tu")
        for node in nodes:
            if node[0][0].text:
                eng_data.append(node[0][0].text.strip())
            if node[1][0].text:
                cor_data.append(node[1][0].text.strip())

    return cor_data, eng_data

def create_buckets(eng_text,cor_text):
    lens = []
    for x in eng_text:
        lens.append(len(x.split()))
    idxs = np.argsort(lens)

    eng_buckets = [[]]
    cor_buckets = [[]]

    last_len = lens[idxs[0]]

    for index in idxs:
        if lens[index] != last_len:
            eng_buckets.append([eng_text[index]])
            cor_buckets.append([cor_text[index]])
            last_len = lens[index]
        else:
            eng_buckets[-1].append(eng_text[index])
            cor_buckets[-1].append(cor_text[index])
    return cor_buckets, eng_buckets

def merge_buckets(eng_buckets, cor_buckets, min_bucket_len=200):
    e_b = [eng_buckets[0]]
    c_b = [cor_buckets[0]]

    id = 1
    while id < len(eng_buckets):
        if len(e_b[-1]) < min_bucket_len:
            e_b[-1].extend(eng_buckets[id])
            c_b[-1].extend(cor_buckets[id])

        else:
            e_b.append(eng_buckets[id])
            c_b.append(cor_buckets[id])
        id += 1

    if len(e_b[-1]) < min_bucket_len:
        e_b[-2].extend(e_b[-1])
        c_b[-2].extend(c_b[-1])

    del e_b[-1]
    del c_b[-1]

    return c_b,e_b

def split_train_and_validate(cor_buckets,eng_buckets,base_dir="split_datasets"):
    
    for b in range(len(cor_buckets)):            
        test = random.sample(list(enumerate(cor_buckets[b])),int(len(cor_buckets[b]) * 0.05))
        with open(f"{base_dir}/test_data_cor.txt","a") as f:
            print(test,len(cor_buckets[b]))
            for x,t in test:
                f.write(cor_buckets[b][x] + "\n")

        with open(f"{base_dir}/test_data_eng.txt","a") as f:
            for x,t in test:
                f.write(eng_buckets[b][x] + "\n")
        to_delete = set()
        for x,t in test:
            to_delete.add(x)

        new_bucket = []
        for x,text in enumerate(cor_buckets[b]):
            if x not in to_delete:
                new_bucket.append(text)

        cor_buckets[b] = new_bucket

        new_bucket = []
        for x,text in enumerate(eng_buckets[b]):
            if x not in to_delete:
                new_bucket.append(text)

        eng_buckets[b] = new_bucket


    for b in range(len(cor_buckets)):            
        test = random.sample(list(enumerate(cor_buckets[b])),int(len(cor_buckets[b]) * 0.01))
        with open(f"{base_dir}/dev_data_cor.txt","a") as f:
            for x,t in test:
                f.write(cor_buckets[b][x] + "\n")

        with open(f"{base_dir}/dev_data_eng.txt","a") as f:
            for x,t in test:
                f.write(eng_buckets[b][x] + "\n")


        to_delete = set()
        for x,t in test:
            to_delete.add(x)

        new_bucket = []
        for x,text in enumerate(cor_buckets[b]):
            if x not in to_delete:
                new_bucket.append(text)

        cor_buckets[b] = new_bucket

        new_bucket = []
        for x,text in enumerate(eng_buckets[b]):
            if x not in to_delete:
                new_bucket.append(text)

        eng_buckets[b] = new_bucket

    for b in range(len(cor_buckets)):            
        with open(f"{base_dir}/train_data_cor.txt","a") as f:
            for t in cor_buckets[b]:
                f.write(t + "\n")

        with open(f"{base_dir}/train_data_eng.txt","a") as f:
            for t in eng_buckets[b]:
                f.write(t + "\n")

c_tmx,e_tmx = read_tmx("TMX_datasets")
c_raw,e_raw = read_raw("raw_datasets")

cor = c_raw + c_tmx
eng = e_raw + e_tmx

cor_bucks, eng_bucks = create_buckets(eng,cor)
cor_bucks, eng_bucks = merge_buckets(eng_bucks,cor_bucks)

print(len(cor))

# split_train_and_validate(cor_bucks,eng_bucks)
