#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:05:02 2022

@author: risaluthor
"""
import pandas as pd
from sklearn.features_extraction.text import TfidfVectorizer

pd.set_option('display.max_columns', None)

#Read database fomr csv
#Analysis Text
df_full = pd.read_csv('Tweets.csv')
df_text = df_full.text 

#Return all words and tf-idf values for each row
df = pd.DataFrame(tfIdf.todense(),  columns=model.get_feature_names_out())

#Calculate top 3 words with highest tfidf score
li=[]
for index,row in df.iterrows():
    sor = row[:-1].sort_values(ascending=False)[:3]
    
    #Add to list
    li.append(list(sor.index))
    
    #Add to csv
df_full['tfidf'] = li
df_full.to_csv('Tweets_Modified_.csv')    
