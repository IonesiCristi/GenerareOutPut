
def replaceWordsWithSyn(synonimList,wordsList,sentence):
    i=0
    newSentence = sentence
    for word in wordsList:
        if word[1] in ["DT","TO","CC","IN","WDT","VBZ","FW","EX","UH"]:
            i=i+1
            continue
        newSentence=newSentence.replace(' ' + word[0] + ' ',' ' + synonimList[i] + ' ')
        i = i+1

    return newSentence
