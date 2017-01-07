import nltk

#nltk.download("wordnet")
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer


def extractEligibleWords(sentence):
    returnList = list()
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+\,')
    tokens = tokenizer.tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    for item in tagged:
        if item[0].istitle():
            continue
        elif item[0].isdigit():
            continue
        else:
            returnList.append(item)

    return returnList
