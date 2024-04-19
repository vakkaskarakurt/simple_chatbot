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
