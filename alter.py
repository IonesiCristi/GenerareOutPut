import random

##########################
# Functia pe care o veti folosi de aici este alter(text, freqMin = 1, freqMax = 3)
##########################

def inverse2letters(text):
    index = random.randint(1, len(text)-2)
    textNou =  text[:(index )] + text[index + 1] +text[index] +text[(index + 2):]
    return textNou

def elidateRandomLetter(text):
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


# functia asta ar trebui apelata(imo) cand avem un text ceva mai mare (>200chars?)
def add_onomatopee(text):
    onomatopee_list = ['Uhm', 'Oh yeah, and', 'Hmm']  # please add something to this list cuz i have no more ideeas
    randomOnomatopeeList = random.randint(0, len(onomatopee_list)-1)
    # caut indexul finalului de propozitie de dupa caracterul 40 si adaug un element din onomatopeeList in interior
    index = text.find('.', 40)

    if index == -1 or len(text) <200:
        # 1.in cazul in care textul are mai putin de 200 de caractere nu se modifica textul
        # cine uita ce tre sa zica daca e un raspuns scurt?
        # 2.textul ramane nemodificat si daca e format dintr-o singura propozitie
        return text

    output_text = text[:index] + '.' + onomatopee_list[randomOnomatopeeList] + '..' + text[index:]
    return output_text


#####################
#atentie! la adaugarea unei noi functii de alterare, a se adauga in lista de mai jos
listOfFunctions = [inverse2letters, elidateRandomLetter, lowerFirstLetter, upperFirst2Letters, lowerRandomLetter, add_onomatopee]
NUMBER_OF_ALTERING_FUNCTIONS = 6 # len(listOfFunctions)

ALTERATIONS_MADE = 0
#####################


def alter(text, freqMin =2, freqMax = 3):
    '''
    Functia alter urmareste sa modifice textul corect, alterandul cu o frecventa
    oarecare, pentru a sugera umanitatea
    :param text: textul de modificat
    :param freqMin: frecventa minima a alterarilor facute
    :param freqMax: frecventa maxima a alterarilor facute
    :return:
    '''
    global ALTERATIONS_MADE
    global NUMBER_OF_ALTERING_FUNCTIONS
    indexRandom = random.randint(freqMin, freqMax)
    indexAlteringFunction = random.randint(0, NUMBER_OF_ALTERING_FUNCTIONS-1)
    #print ( "Alterations_made: ", ALTERATIONS_MADE, "\nindex_random: ", indexRandom)
    if ALTERATIONS_MADE >= indexRandom :
        ALTERATIONS_MADE = 0
        textNou = listOfFunctions[indexAlteringFunction](text)
    else:
        ALTERATIONS_MADE += 1
        textNou = text
    return textNou




listOfFunctions = [inverse2letters, elidateRandomLetter, lowerFirstLetter, upperFirst2Letters, lowerRandomLetter, add_onomatopee]






