import alter
import incurajatori
import informal
import rawWords
import replaceWordsWithSyn
import generateSynonims
import random
import flattery


flatteryGenerate =0

def generateOutPut(sentence):
    global flatteryGenerate

    newSentence = sentence[0].lower() + sentence[1:]
    sentence = newSentence

    wordsToBeReplaced = rawWords.extractEligibleWords(sentence)

    synonims = generateSynonims.generateSynonims(wordsToBeReplaced)

    newSentence = replaceWordsWithSyn.replaceWordsWithSyn(synonims,wordsToBeReplaced,sentence)

    if flatteryGenerate<3:
        flatteryGenerate = flatteryGenerate +1
        randIncurajare = 0
    else:
        randIncurajare = random.randint(0,1)


    if randIncurajare == 1:
        newSentence = incurajatori.creeazaSintagmaMagulire(newSentence)

    '''
    Momentan se altereaza o data la 45-55 caracatere.
    Daca vi se pare prea des, puteti schimba apeland
    alter.alter(newSentence, altaFrecventa), cu altaFrecventa de tip int
    '''
    oldSentence = alter.alter(newSentence)
    newSentence = oldSentence

    #print newSentence
    newSentence = informal.useContractions(newSentence)

    return newSentence

#print(generateOutPut("A carrot is a delicious and nutritious edible orange tuber that can be eaten raw, juiced, or cooked. Apple s are nice.  If humans eat enough of them, you turn orange, I hear. It's ability to make the sight better is adorable. account me please. accident  "))

