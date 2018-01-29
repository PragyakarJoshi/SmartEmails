#!/usr/bin/python
# -*- coding: utf-8 -*-

from emailGrabber import categoryListWords
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util
import pickle
from emailFilter import cleanEmail, toDict

primary_emails = []
promotion_emails = []
social_emails = []
update_emails = []
spam_emails = []

def category_tagger(category_list, category_name):
	for item in categoryListWords(category_name):
		category_list.append((toDict((cleanEmail(item))),category_name))

# Tagging with respective Category
category_tagger(primary_emails, 'primary')
category_tagger(social_emails, 'social')
category_tagger(promotion_emails, 'promotion')
category_tagger(update_emails, 'update')
category_tagger(spam_emails, 'spam')

# DATASET DETAILS
# ADD TOTAL FILES
# ADD TOTAL SIZE OF FILES
print("Primary Emails: " , len(primary_emails))
print("Social Emails: " ,len(social_emails))
print("Promotion Emails: " ,len(promotion_emails))
print("Update Emails: " ,len(update_emails))
print("Spam Emails: " ,len(spam_emails))
print()
# Training Process
training_list = primary_emails + promotion_emails + social_emails + update_emails + spam_emails
classifier = NaiveBayesClassifier.train(training_list)
print("Classifier Trained!")

#Testing
# print(classifier.classify(toDict(cleanEmail('email Section'))))

#Saving into a pickle file
f = open('data/trained_data.pickle', 'wb')
pickle.dump(classifier, f)
f.close()
print("Saved in Pickle!")

# Claculating the Accuracy
# accuracy = nltk.classify.util.accuracy(classifier, testing_list)
# print("Classifier Accuracy:", accuracy*100)
