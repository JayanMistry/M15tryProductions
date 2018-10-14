#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:43:39 2018

Lemmatizing - which is the same as stemming but end result is an actual word


@author: jay
"""

from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()

# Lemmatizing the word better
print(lemmatizer.lemmatize("better"))

#lemmatizing the word better but as an adjective 
print(lemmatizer.lemmatize("better", pos="a"))

print(lemmatizer.lemmatize("run"))

print(lemmatizer.lemmatize("run", pos="v"))



test = "Today I went to the shop and then I came home and applied Olay"


tokened = nltk.tokenize.word_tokenize(test)

n = [lemmatizer.lemmatize(i) for i in tokened]

tagged = nltk.pos_tag(tokened)

lem_test = ""
for w in tokened:
    print(w)
    lem_test += " " +  (lemmatizer.lemmatize(w))


print(tokened)
print(tagged)
print(lem_test)
print(n)