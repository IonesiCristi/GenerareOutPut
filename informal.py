def useContractions(text):
    '''It makes use of Contractions.'''
    dictionar = {
        " not": "n't",
        " are": "'re",
        " is": "'s",
        " will": "'ll",
        " am": "'m"
    }
    for i in dictionar.keys() :
        text = text.replace (i, dictionar[i])
    return text