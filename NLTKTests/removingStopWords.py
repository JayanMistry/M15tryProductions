# -*- coding: utf-8 -*-
"""
Spyder Editor

This script is an example of removing stop words
Stop words such as "that'll", 'am', 'each', 'wouldn', 'few', "hasn't", 'through', 'll', 'very', 'too', 'has', 'now', 'below', 'above', 'only', 'own', 'they', 'how', 'when', 'o', 'with', 'such', 'at', 'over', 'on',
are not very useful in language analysis as they usually refers to the most common words in a language.


"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Define a list of stop words that need to be discarded
stop_words = set(stopwords.words("english"))

#Example text to be parsed
text = "this is an example showing off stop word filteration"

#tokenize text
words = word_tokenize(text)

#Result

"""
filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
"""
        
filtered_sentence = [w for w in words if w not in stop_words]        
        
print(filtered_sentence)
