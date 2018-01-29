import os
from nltk.tokenize import word_tokenize
from emailFilter import cleanEmail

def categoryListWords(category_name):
    the_list = []
    files = os.listdir('data/emails/' + category_name)

    for filename in files:
        f = open('data/emails/' + category_name + '/' + filename, 'rt')
        content = f.read()
        the_list.append(content)
        f.close()
    return the_list

# categoryListWords('spam')
