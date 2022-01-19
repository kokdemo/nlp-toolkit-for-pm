import jieba
import jieba.posseg as pseg
# jieba.load_userdict("dict.txt")
import csv
import pandas as pd

origin_data = pd.read_csv("origin.csv",sep=",")
for index,row in origin_data.iterrows():
    words = pseg.cut(row['text'])
    names = []
    for word, flag in words:
        if flag == "nr" or flag == "nrfg" or flag == "nrt":
            names.append(word)
    origin_data.iloc[index,1] = ",".join(names)
print(origin_data)
origin_data.to_csv("detect-name.csv")