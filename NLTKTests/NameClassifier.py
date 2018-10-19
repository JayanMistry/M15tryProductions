#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:04:26 2018

@author: jay
"""
import nltk


import pyphen
from nltk.corpus import names
import random
from sklearn.ensemble import VotingClassifier

def gender_features(word):
    return {'last_letter': word[-2]+word[-1]}

def full_features(word):
    mid = int(len(word)/2) 
    return {'full_name': word[:mid]}

def getSyllables(word):
    dic = pyphen.Pyphen(lang='nl_NL')
    res = (dic.inserted('lettergrepen'))
    return {'no_of_syllables': (res.count('-')+1) }

labelled = ([(name, "male") for name in names.words('male.txt')] + [(name, "female") for name in names.words('female.txt')])

#print(labelled)

random.shuffle(labelled)

train = labelled[:int(len(labelled)/2)]

test = labelled[int(len(labelled)/2):]

featuresets = [(gender_features(n), gender) for (n, gender) in labelled]

NEWfeaturesets = [(getSyllables(n), gender) for (n, gender) in labelled]


Newtrain = NEWfeaturesets[:int(len(NEWfeaturesets)/2)]

Newtest = NEWfeaturesets[int(len(NEWfeaturesets)/2):]


train = featuresets[:int(len(featuresets)/2)]

test = featuresets[int(len(featuresets)/2):]

#print(train)
Newclassifier = nltk.NaiveBayesClassifier.train(Newtrain)

classifier = nltk.NaiveBayesClassifier.train(train)

prediction = nltk.classify.accuracy(classifier, test) + nltk.classify.accuracy(Newclassifier, test)

prediction = prediction/2

train_x = ["mark","John","bob","amy","jenna"]
train_y = [0,0,0,1,1]

eclf1 = VotingClassifier(estimators=[('cl',classifier), ('NewCL', Newclassifier)], voting='hard')
eclf1 = eclf1.fit(train_x, train_y)

print(nltk.classify.accuracy(classifier, test))

print(nltk.classify.accuracy(Newclassifier, test))
