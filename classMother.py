class classMother:
    def __init__(self):
        pass

    def searchInDictionary(self,dictionary, x):

        if(dictionary.get(x) == None):
            return "Erreur"
        else:
            return dictionary.get(x)