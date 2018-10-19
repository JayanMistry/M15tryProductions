#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:16:32 2018
API to Count Number of each Parts of Speech
@author: jay
"""

from nltk.stem import WordNetLemmatizer
import nltk
import nltk.tokenize
from collections import Counter
from nltk.corpus import brown

#take in a corpera, tokenize, pos tag and then return json list of pos and count



def getNumberOfPOS(corpera):
    lemmatizer = WordNetLemmatizer()
       
    brown_tagged_sents = brown.tagged_sents()
    
    #Can filter by catergory
    #brown_tagged_sents = brown.tagged_sents(categories='news')
    
    #build trigram tagger
    trigram_tagger = nltk.TrigramTagger(brown_tagged_sents) 
    
    tokened = nltk.tokenize.word_tokenize(corpera)
    
    lemmatized = [lemmatizer.lemmatize(i) for i in tokened]
    
    tagged = trigram_tagger.tag(lemmatized)
    
    counts = Counter(tag for word,tag in tagged)

    return counts


def getNormalisedNumberOfPOS(corpera):
    counts = getNumberOfPOS(corpera)
    total = sum(counts.values())
    result = dict((word, float(count)/total) for word,count in counts.items())
    return result



result = (getNormalisedNumberOfPOS("hello, my name is jay. I went to Asda. I also ate icecream yesterday"))


#print(result)


"""

Number
Tag
Description
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
"""