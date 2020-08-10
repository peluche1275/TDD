class StrConvertor:

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
            listContainingConvertedWords.append(self.searchword(x))
            
        conversion = "".join(listContainingConvertedWords)

        if conversion == "Erreur":
            return "Erreur"
        else:
            try:
                return eval("".join(listContainingConvertedWords))
            except:
                return "Erreur"

    def searchword(self, x):

        if(self.dictionaryWordsToIntegers.get(x) == None):
            return "Erreur"
        else:
            return self.dictionaryWordsToIntegers.get(x)