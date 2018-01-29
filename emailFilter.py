#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk.classify.util
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords

def sentenceTokenizer(email):
    sent_tokenizer = PunktSentenceTokenizer()
    sentences = sent_tokenizer.tokenize(email)
    return sentences

def punctuationFilter(email_tokens):
    no_punctuations = [word for word in email_tokens if word.isalpha()]
    return no_punctuations

def stopWordsFilter(punctuation_rem_words):
    stop_words = set(stopwords.words('english'))
    no_stop_words = [word for word in punctuation_rem_words if not word in stop_words]
    return no_stop_words

def cleanEmail(email):
    email_tokens = email.lower().split()
    filtered_email = stopWordsFilter(punctuationFilter(email_tokens))
    return filtered_email

def toDict(email_list):
    email_dict = dict([(word, True) for word in email_list])
    return email_dict

# email = "In addition to my extensive retail experience, I have excellent communication skills. I always maintain a gracious and professional manner when communicating with people, including customers and store staff. My broad experience and range of skills make me a superior candidate for this position.My resume, which is below, provides additional information on my background and qualifications. I look forward to hearing from you as soon as possible to arrange a time for an interview."
# print(cleanEmail(primary))
# print(sentenceTokenizer(email))
