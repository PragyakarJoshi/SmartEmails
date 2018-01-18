import pickle
from emailFilter import cleanEmail, toDict

def emailClassifier(email):
    f = open('data/trained_data.pickle','rb')
    classifier = pickle.load(f)
    f.close()
    result = classifier.classify(toDict(cleanEmail(email)))
    return result

f = open('data/email.txt','rt')
email_content = f.read()
f.close()

print(emailClassifier(email_content))
