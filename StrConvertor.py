from classMother import *

class StrConvertor(classMother):

    def __init__(self):
        
        self.dictionaryWordsToIntegers = {
            "Zero": "0",
            "Un": "1",
            "Deux": "2",
            "Trois": "3",
            "Quatre": "4",
            "Cinq": "5",
            "Six": "6",
            "Sept": "7",
            "Huit": "8",
            "Neuf": "9",
            "Plus": "+",
            "Moins": "-"
        }

    def convert(self, string):

        import re

        splitStringIntoList = re.findall('[A-Z][^A-Z]*', string)

        listContainingConvertedWords = []

        for x in splitStringIntoList:
            listContainingConvertedWords.append(classMother.searchInDictionary(self,self.dictionaryWordsToIntegers, x))
            
        conversion = "".join(listContainingConvertedWords)

        if conversion == "Erreur":
            return "Erreur"
        else:
            try:
                return eval("".join(listContainingConvertedWords))
            except:
                return "Erreur"