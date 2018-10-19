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


def document_features(document):
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words)[:2000]
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

test = "stupid, pum, god"

#print(document_features(test))

print(document_features(movie_reviews.words('neg/cv000_29416.txt')))

#featureSets = [(document_features(rev), catergory) for (rev,catergory) in documents[:300]]

featureSets = []

documents = documents[0:10]
for (rev,catergory) in documents:
    featureSets += (document_features(rev), catergory)
    

print(featureSets)  