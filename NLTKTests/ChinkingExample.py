#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:56:35 2018

This example is chinking.
Which is removing the things that you dont want in your chunks

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
            chunkGram = r"""Chunk:{<.*>+?}
                               }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
       #     chunked.draw()
            
    except Exception as e:
        print()
        
    chunked.draw()
process_content()