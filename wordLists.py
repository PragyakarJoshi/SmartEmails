
dayList = []
eventList = []

def readFile(filename):
    file = open(filename, 'rt')
    words = file.readlines()
    file.close()
    return words

def eventWordsList():
    eventWords = readFile('data/myLib/eventWords')
    for word in eventWords:
        eventList.append(word.rstrip())
    return eventList

def dayWordsList():
    dayWords = readFile('data/myLib/dayWords')
    for word in dayWords:
        dayList.append(word.rstrip())
    return dayList

# print(eventWordsList())
# print(dayWordsList())
