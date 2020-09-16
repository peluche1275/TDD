class descendingOrder:
    def __init__(self):
        pass

    def descending(self,stringToConvertToInteger):

        stringConvertedToIntegerList = self.convertStringListToIntegerList(self.splitStringToList(stringToConvertToInteger))

        self.putInReverseOrder(stringConvertedToIntegerList)

        integerListConvertedToStringList = [str(integer) for integer in stringConvertedToIntegerList]

        stringListConvertedToString = "".join(integerListConvertedToStringList)

        stringConvertedToInteger = int(stringListConvertedToString)

        return stringConvertedToInteger

    def putInReverseOrder(self,integerList):
        
        return integerList.sort(reverse=True)

    def splitStringToList(self, stringToSplitIntoList):

        return [char for char in stringToSplitIntoList]

    def convertStringListToIntegerList(self,stringConvertedToList):

        return list(map(int, stringConvertedToList))