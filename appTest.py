from assertEquals import *

from StrConvertor import *

from romanNumeralsDecoder import *

from descendingOrder import *

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


def testRomanNumeralsDecoder():
    rND = romanNumeralsDecoder()
    print(assertEquals(rND.decode("I"),1))
    print(assertEquals(rND.decode("V"),5))
    print(assertEquals(rND.decode("XX"),20))
    print(assertEquals(rND.decode("XXI"),21))
    print(assertEquals(rND.decode("IV"),4))
    print(assertEquals(rND.decode("IX"),9))
    print(assertEquals(rND.decode("Test"),"Erreur"))

def testDescendingOrder():
    dO = descendingOrder()
    print(assertEquals(dO.descending("42145"),['4','2','1','4','5']))
    print(assertEquals(dO.descending("42145"),[4,2,1,4,5]))
    print(assertEquals(dO.descending("42145"),54421))

testDescendingOrder()