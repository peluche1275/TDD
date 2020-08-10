from assertEquals import *

from StrConvertor import *

def testStringConvertorToInt():
    StringConvertor = StrConvertor()
    print(assertEquals(StringConvertor.convert('Deux'), 2))
    print(assertEquals(StringConvertor.convert('Trois'), 3))
    print(assertEquals(StringConvertor.convert('DeuxPlusDeux'), 4))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeux'), 1))
    print(assertEquals(StringConvertor.convert('TroisMoinsDeuxPlusCinqMoinsSix'), 0))
    print(assertEquals(StringConvertor.convert('DeuxPlus'), "Erreur"))
    print(assertEquals(StringConvertor.convert('Plus'), "Erreur"))
    print(assertEquals(StringConvertor.convert('Erreur'), "Erreur"))


testStringConvertorToInt()
