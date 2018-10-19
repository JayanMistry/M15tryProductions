#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:44:32 2018

@author: jay
"""

import nltk
import random

from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])

#print(type(movie_reviews))

all_words =[]
for w in movie_reviews.words():
    all_words.append(w.lower())
    
    
    
all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))