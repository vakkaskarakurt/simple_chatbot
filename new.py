import random
import json
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemmatizer.lemmatize("running")

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignoreLetters = ['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent ['patterns']:
        wordList = nltk.word_tokenize
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) 
         for word in words 
         if word not in ignoreLetters]

words = sorted(set(classes))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
