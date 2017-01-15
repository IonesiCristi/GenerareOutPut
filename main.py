import alter
import incurajatori
import informal
import rawWords
import replaceWordsWithSyn
import generateSynonims
import random
#import flattery

flatteryGenerate =0

def generateOutPut(sentence):
    global flatteryGenerate

    wordsToBeReplaced = rawWords.extractEligibleWords(sentence)

    synonims = generateSynonims.generateSynonims(wordsToBeReplaced)

    newSentence = replaceWordsWithSyn.replaceWordsWithSyn(synonims,wordsToBeReplaced,sentence)

    if flatteryGenerate<3:
        flatteryGenerate = flatteryGenerate +1
        randIncurajare = 0
    else:
        randIncurajare = random.randint(0,1)

    randAlter = random.randint(5,7)

    if randIncurajare == 1:
        newSentence = incurajatori.creeazaSintagmaMagulire(newSentence)

    oldSentence = alter.alter(newSentence)
    newSentence = oldSentence
       #print newSentence
    newSentence = informal.useContractions(newSentence)

    return newSentence

print(generateOutPut("A carrot is a delicious and nutritious edible orange tuber that can be eaten raw, juiced, or cooked. If humans eat enough of them, you turn orange, I hear."))

