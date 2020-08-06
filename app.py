class StrConvertor:

    def __init__(self):

        self.dictionaryWordsToIntegers =  {
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
    
    def convert(self,string):

        import re

        splitStringIntoList = re.findall('[A-Z][^A-Z]*',string)

        listContainingConvertedWords = []

        for x in splitStringIntoList:
            listContainingConvertedWords.append(self.dictionaryWordsToIntegers.get(x))
        
        return eval("".join(listContainingConvertedWords))

#  TEST #

def assertEquals(firstComparing, secondComparing):
    if firstComparing == secondComparing:
        return True
    else:
        return False


def testStringConvertorToInt():
    StringConvertor = StrConvertor()
    print(assertEquals(StringConvertor.convert('Deux'), 2))
    print(assertEquals(StringConvertor.convert('Trois'), 3))
    print(assertEquals(StringConvertor.convert('DeuxPlusDeux'), 4))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeux'), 1))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeuxPlusCinqMoinsSix'), 0))


testStringConvertorToInt()
