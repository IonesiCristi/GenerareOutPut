import random

###########################
# Functia pe care o veti folosi de aici este alter(text, freqMin = 1, freqMax = 3)
###########################

def inverse2letters(text):
    if len(text) <=1 :
        return text
    if len(text) == 2 :
        return text[1]+text[0]
    index = random.randint(0, len(text)-2)
    textNou =  text[:(index )] + text[index + 1] +text[index] +text[(index + 2):]
    return textNou

def elidateRandomLetter(text):
    if len(text) <=2 :
        return text
    index = random.randint(1, len(text)-2)
    textNou =  text[:(index )] + text[index + 1] +text[(index + 2):]
    return textNou

def lowerFirstLetter(text):
    textNou = text[0].lower() + text[1:]
    return textNou

def upperFirst2Letters(text):
    textNou = text[0].upper() + text[1].upper() + text[2:]
    return textNou

def lowerRandomLetter(text):
    indexi = []
    for i in range(1, len(text)) :
        if text[i].isupper() :
            indexi += [i]
    if len(indexi) > 0:
        random.shuffle(indexi)
        index = indexi[0]
        textNou = text[:(index)] + text[index].lower()+ text[index + 1] + text[(index + 2):]
        return textNou


# cum traduci onomatopee in engleza?
# functia asta ar trebui apelata(imo) cand avem un text ceva mai mare (>200chars?)
def addOnomatopee(text):
    onomatopeeList = ['Uhm', 'Oh yeah, and', 'Hmm']  # please add something to this list cuz i have no more ideeas
    randomOnomatopeeIndex = random.randint(0, len(onomatopeeList)-1)
    # caut indexul finalului de propozitie de dupa caracterul 40 si adaug un element din onomatopeeList in interior
    index = text.find('.', 40)
    output_text = text[:index] + '.' + onomatopeeList[randomOnomatopeeIndex] + '..' + text[index:]
    return output_text


#####################
#atentie! la adaugarea unei noi functii de alterare, a se adauga in lista de mai jos
listOfFunctions = [inverse2letters, elidateRandomLetter, lowerFirstLetter, upperFirst2Letters, lowerRandomLetter]
NUMBER_OF_ALTERING_FUNCTIONS = 5 # len(listOfFunctions)

ALTERATIONS_MADE = 0
#####################


def alter(text, freqMin = 1, freqMax = 3):
    '''
    Functia alter urmareste sa modifice textul corect, alterandul cu o frecventa
    oarecare, pentru a sugera umanitatea

    :param text: textul de modificat
    :param freqMin: frecventa minima a alterarilor facute pe unitCharcters caractere prezente
    :param freqMax: frecventa maxima a alterarilor facute pe unitCharcters caractere prezente
    :return:
    '''
    try:
        global ALTERATIONS_MADE
        global NUMBER_OF_ALTERING_FUNCTIONS
        unitCharcters = 30
        numberErrorsToBeDone = int(len(text)/unitCharcters)+1
        print numberErrorsToBeDone
        for i in xrange(numberErrorsToBeDone):
            indexRandom = random.randint(freqMin, freqMax)
            indexAlteringFunction = random.randint(0, NUMBER_OF_ALTERING_FUNCTIONS-1)
            print ( "Alterations_made: ", ALTERATIONS_MADE, "\nindex_random: ", indexRandom)
            if ALTERATIONS_MADE >= indexRandom :
                ALTERATIONS_MADE = 0
                textNou = listOfFunctions[indexAlteringFunction](text)
            else:
                ALTERATIONS_MADE += 1
                textNou = text
        return textNou
    except:
        print ("Avem probleme in functia alter/alter.py")
    return text





