#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 11:16:21 2018

@author: jay
"""

import nltk
import random
import pyphen

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

documents = documents[:1000]

#print(documents)

featureSets = [(document_features(d), c) for (d,c) in documents]

print('Got here')
train_set, test_set = featureSets[100:], featureSets[:100]

print('Got here')

classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.show_most_informative_features(5)


print('Got here')

print(nltk.classify.accuracy(classifier, test_set))
