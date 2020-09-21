from assertEquals import *

from StrConvertor import *

from romanNumeralsDecoder import *

from descendingOrder import *

from splitStringInPair import *

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
    print(assertEquals(dO.descending("42145"),54421))
    print(assertEquals(dO.descending("44444"),44444))
    print(assertEquals(dO.descending("123456"),654321))
    print(assertEquals(dO.descending("654321"),654321))
    print(assertEquals(dO.descending("1"),1))
    print(assertEquals(dO.descending("Test"),"Erreur"))
    print(assertEquals(dO.descending("123Test"),"Erreur"))

def testSplitStringInPair():
    sSiP = splitStringInPair()
    print(assertEquals(sSiP.split("abcdef"),['ab', 'cd', 'ef']))
    print(assertEquals(sSiP.split("abc"),['ab', 'c_']))

testSplitStringInPair()