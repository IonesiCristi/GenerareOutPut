def useContractions(text):
    '''It makes use of Contractions.'''
    dictionar = {
        " are": "'re",
        " will": "'ll",
        " am": "'m"
    }
    for i in dictionar.keys() :
        text = text.replace (i, dictionar[i])
    return text