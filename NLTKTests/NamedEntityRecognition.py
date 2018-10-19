#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:05:12 2018

Named entity recognition - use nltk.ne_chunk to get named entity 
binary = True is used to 

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
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            namedEnt =  nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
            
    except Exception as e:
        print()
        #namedEnt.draw()
    
    
############
process_content()
