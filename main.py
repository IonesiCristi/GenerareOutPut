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

    randIncurajare = random.randint(0,1)

    randAlter = random.randint(0,3)

    if randIncurajare == 1:
        newSentence = incurajatori.creeazaSintagmaMagulire(newSentence)

    for i in range(0,randAlter):
       newSentence = alter.alter(newSentence)

    newSentence = informal.useContractions(newSentence)

    return newSentence

#print generateOutPut("Daniel talks to some of the most powerful and influential people in poker about issues that matter to you.")