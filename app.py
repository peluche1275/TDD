class StrConvertor:
    def convert(string):
        dictio = {
            "Zero": 0,
            "Un": 1,
            "Deux": 2,
            "Trois": 3,
            "Quatre": 4,
            "Cinq": 5,
            "Six": 6,
            "Sept": 7,
            "Huit": 8,
            "Neuf": 9,
            "Plus": "+",
            "Moins": "-"
        }
        return dictio.get(string)

#  TEST #


def assertEquals(firstComparing, secondComparing):
    if firstComparing == secondComparing:
        return True
    else:
        return False


def testStringConvertorToInt():
    StringConvertor = StrConvertor
    print(assertEquals(StringConvertor.convert('Deux'), 2))
    print(assertEquals(StringConvertor.convert('Trois'), 3))
    print(assertEquals(StringConvertor.convert('Plus'), "+"))
    print(assertEquals(StringConvertor.convert('Moins'), "-"))
    print(assertEquals(StringConvertor.convert('DeuxPlusDeux'), 4))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeux'), 1))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeuxPlusCinqMoinsSix'), 0))


testStringConvertorToInt()
