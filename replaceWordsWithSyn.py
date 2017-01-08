
def replaceWordsWithSyn(synonimList,wordsList,sentence):
    i=0
    newSentence = sentence
    for word in wordsList:
        if word[1] in ["CC","CD","DT","EX","FW","IN","JJR","JJS","LS","MD","NNPS","PDT","POS","PRP",
                       "PRP$","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT",
                       "WP","WP$","WRB","NNP","NN","NNS"]:
            i=i+1
            continue
        newSentence=newSentence.replace(' ' + word[0] + ' ',' ' + synonimList[i] + ' ')
        i = i+1

    return newSentence
