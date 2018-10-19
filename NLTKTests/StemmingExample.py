#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:46:26 2018

an example of stemming e.g. writing becomes write (the stem)
Basically normalising sentences

Using 

@author: jay
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


ps = PorterStemmer()

words = ["python", "pythoner", "pythoning", "pythonly"]

for w in words:
    print(w, ' = ', ps.stem(w))


    