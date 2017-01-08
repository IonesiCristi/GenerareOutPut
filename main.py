import alter
import incurajatori
import informal
import rawWords
import replaceWordsWithSyn
import generateSynonims
import random
#import flattery

def generateOutPut(sentence):

    wordsToBeReplaced = rawWords.extractEligibleWords(sentence)

    synonims = generateSynonims.generateSynonims(wordsToBeReplaced)

    newSentence = replaceWordsWithSyn.replaceWordsWithSyn(synonims,wordsToBeReplaced,sentence)

    randIncurajare = random.randint(0,2)

    #randAlter = random.randint(5,7)

    if randIncurajare == 1:
        newSentence = incurajatori.creeazaSintagmaMagulire(newSentence)

    for i in range(0,3):
       oldSentence = alter.alter(newSentence, 1, 2)
       newSentence = oldSentence
       #print newSentence
    newSentence = informal.useContractions(newSentence)

    return newSentence

print(generateOutPut("You seem to be a very interesting person. Tell me more about yourself. What animal best represents you and why? "))