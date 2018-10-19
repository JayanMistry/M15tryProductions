#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:14:30 2018

@author: jay
"""

import nltk
from nltk.corpus import sentiwordnet, wordnet

print(nltk.__file__)


syns = wordnet.synsets("program")

print(syns[0])

print(syns[0].lemmas())

print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#example 
print(syns[0].examples())

synonyms = []

antonyms =[]

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print(l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
         

#  [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("--------SYNONYMS-------")
print(set(synonyms))
print("\n")
print("--------ANTONYMS-------")
print(set(antonyms))

#Comparing Word similarities 

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))