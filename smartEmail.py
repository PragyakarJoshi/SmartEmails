import pickle
from emailFilter import cleanEmail, toDict
from planDetector import detectPlan

def emailClassifier(email):
    f = open('data/trained_data.pickle','rb')
    classifier = pickle.load(f)
    f.close()
    result = classifier.classify(toDict(cleanEmail(email)))
    return result

def reminder(email):
    rem = detectPlan(email)
    print(rem)
    return rem
