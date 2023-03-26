from markovBase import *


mar = markov()



def saveText(raw_text):
    data = mar.prepareData(raw_text)
    mar.addToDict(data)
    



def getRandText(n = 20):
    return mar.collectText(n)