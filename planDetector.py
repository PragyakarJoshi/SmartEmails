#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from emailFilter import sentenceTokenizer
from wordLists import dayWordsList, eventWordsList


day_words = dayWordsList()
event_words = eventWordsList()


def detectPlan(email):
    email_day_word = " "
    email_event_word = " "
    noun_list = []
    sentences = sentenceTokenizer(email)

    for sent in sentences:
        words = nltk.word_tokenize(sent)
        tagged_words = nltk.pos_tag(words)
        noun_word = [item[0] for item in tagged_words if item[1] == 'NN' or item[1] == 'NNS' or item[1] == 'NNP' or item[1] == 'NNPS']
        noun_list.append(noun_word)

    for sent in noun_list:
        for word in sent:
            for day_word in day_words:
                if word == day_word:
                    email_day_word = word
            for event_word in event_words:
                if word == event_word:
                    email_event_word = word

    if email_event_word == " " or email_day_word == " ":
        return 
    else:
        plan = "Seems like you have a " + email_event_word + " " + email_day_word + ". Set a reminder?"
        return plan
