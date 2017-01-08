#Tirpescu Cosmin - modul generare-text-output
#Generare sinonime pentru refrazare, utilizand lista de cuvinte eligibile.
#pip install PyDictionary sau easy_install -U PyDictionary

import os
import random
try:
        import PyDictionary
except:
        print(" Instaleaza PyDictionary Module.")
        print("-> 'pip install pydictionary'")

from PyDictionary import PyDictionary

def generateSynonims(words):
        synonims = list()
        dictionary = PyDictionary()
        aux = random.randrange(4)
        i=0

        for w in words:
                dictionarySynonims = dictionary.synonym(w[0])
                if not dictionarySynonims:
                        synonims.append(w[0])
                else:
                        aux = random.randrange(len(dictionarySynonims))
                        syn = dictionarySynonims[aux]
                        synonims.append(syn)

        return synonims

