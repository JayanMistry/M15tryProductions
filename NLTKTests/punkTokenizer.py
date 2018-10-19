#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:56:35 2018

This example is training a tokenizer on a specific set of text

So the POS will be tuned to be allocated accoording to the training set
@author: jay
"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample = state_union.raw("2006-GWBush.txt")

cus_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = cus_tokenizer.tokenize(sample)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)        
    except Exception as e:
        print()
        
process_content()