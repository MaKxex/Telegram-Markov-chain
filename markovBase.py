import numpy as np
import random
import re


raw = open('text.txt', encoding='utf8').read()


class markov:
    def __init__(self):
        self.word_dict = {}
        self.TextBase = []



    def prepareData(self,text: str) -> list:
        text = re.sub(r'[^\w]', ' ', text)
        data = text.split()
        self.TextBase = self.TextBase + data
        return data



    def __make_pairs(self,preparedData):
        for i in range(len(preparedData) - 1):
            yield (preparedData[i], preparedData[i + 1])




    def addToDict(self,preparedData):
        pairGen = self.__make_pairs(preparedData)
        for word_1, word_2 in pairGen:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

        print(self.word_dict)



    def collectText(self, n: int):

        first_word = np.random.choice(self.TextBase)
        k = 0
        while first_word.islower():
            chain = [first_word]
            first_word = np.random.choice(self.TextBase)
            n_words = 20
            
            for i in range(n_words):
                try:
                    chain.append(np.random.choice(self.word_dict[chain[-1]]))
                except KeyError:
                    pass
            k += 1
        return chain
        # print(self.TextBase)
        # first_word = numpy.random.choice(self.TextBase)

        # while first_word.islower():
        #     chain = [first_word]
        #     n_words = n
        #     first_word = numpy.random.choice(self.TextBase)
            
        #     print(n_words)

        #     for i in range(n_words):
        #         print( chain[-1])

        #         try:
        #             chain.append(numpy.random.choice(self.word_dict[chain[-1]]))
        #         except KeyError:
        #             pass
        
