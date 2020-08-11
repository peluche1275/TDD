class romanNumeralsDecoder:

    def __init__(self):
        self.dictionaryRomanNumerals = {
            "I": "1",
            "V": "5",
            "X": "10",
            "L": "50",
            "C": "100",
            "D": "500",
            "M": "1000",
            "Menos": "-1"
        }

    def split(self, romanNumerals):

        return [char for char in romanNumerals]

    def searchword(self, x):

        if(self.dictionaryRomanNumerals.get(x) == None):
            return "Erreur"
        else:
            return self.dictionaryRomanNumerals.get(x)

    def decode(self, romanNumerals):

        splitRomanNumeralsIntoList = self.split(romanNumerals)

        listContainingConvertedWords = []
        
        for x in splitRomanNumeralsIntoList:

            i = splitRomanNumeralsIntoList.index(x)

            if x == "I":
                try:
                   if splitRomanNumeralsIntoList[i+1] == "V" or splitRomanNumeralsIntoList[i+1] == "X":
                       x = "Menos"
                except:
                    pass

            listContainingConvertedWords.append(self.searchword(x))

        try:
            return eval("+".join(listContainingConvertedWords))
        except:
            return("Erreur")
        
