import alter as Alter
import time

text = [
    "  Ana are mere si se plimba.", #pentru cazul in care propozitia mea incepe cu spatiu si eu vreau sa scriu cu majuscula o litera
                                    #in plus la inceputul unei propozitii, nu imi face nici o schimbare
                                    #La fel pentru cazul in care ChatBot-ul uita sa scrie cu majuscula la inceputul unei propoitii, nu schimba nimic
    "Urmaresc emisiunea 'Go There' saptamanal.",
    "aa", #Pentru cazul in care o litera random este uitata da eroare
    "IMI ESTE SOMN",
    "Cum poti sa spui ASA CEVA?",
    "a", #pentru cazul asta la o litera random este uitata imi da eroare
    "nu ma pricep la exemple", #pentru cazul in care propozitia mea incepe cu litera mica si eu vreau sa scriu cu majuscula o litera
                               #in plus la inceputul unei propozitii, acesta de fapt imi va face primele 2 litere cu majuscula
    "Nu inteleg cateva idei de-ale tale.",
    "121532243253423523",
    "Privesc in zare si ma int       reb ce e viata.",
    "De unele lucruri nu ma mai satur.",
   # " ", -pentru cazul asta da eroare atunci cand 2 litere random sunt inversate, 1 litera random este uitata si cand
           #scrie cu majuscula o litera in plus la inceputul unei propozitii
    "Roxana , Mihai si George sunt prieteni din timpul liceului.",
    "^%$#^$#^$%&%^^#$"
]

#pentru verificarea daca ChatBot scrie fara mauscula o litera random din propozitie, nu trebuia sa functioneze si pentru propozitiile
#care au in propozitie doar prima litera cu majuscula?


def verifyInversionOf2letters():
    print ("2 litere random sunt inversate: ")
    time.sleep(2)
    for i in range(len(text)):
        print ("Original text: ", text[i])
        modifyedText = Alter.inverse2letters(text[i])
        print ("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")

def verifyElidateRandomLetter():
    print ("1 litera random este 'uitata' : ")
    time.sleep(2)
    for i in range(len(text)):
        print ("Original text: ", text[i])
        modifyedText = Alter.elidateRandomLetter(text[i])
        print ("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")

def verifyLowerFirstLetter():
    print ("ChatBot uita sa scrie cu majuscula la inceputul unei propozitii: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.lowerFirstLetter(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")



def verifyUpperFirst2Letters():
    print ("ChatBot scrie cu majuscula o litera in plus la inceputul unei propozitii: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.upperFirst2Letters(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")


def verifyLowerRandomLetter():
    print ("ChatBot scrie fara majuscula o litera random din propozitie: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.lowerRandomLetter(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")

def verifyAddOnomatopee():
    print ("ChatBot adauga onomatopee: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.addOnomatopee(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")


def verifyWriteWrongLetter():
    print ("ChatBot adauga onomatopee: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.writeWrongLetter(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")



def verifyAlter():
    print ("ChatBot adauga onomatopee: ")
    time.sleep(2)
    for i in range(len(text)):
        print("Original text: ", text[i])
        modifyedText = Alter.alter(text[i])
        print("Modifyed text: ", modifyedText)
        time.sleep(2)
        print ("\n")

#verifyInversionOf2letters()
#verifyElidateRandomLetter()
#verifyLowerFirstLetter()
#verifyUpperFirst2Letters()
#verifyLowerRandomLetter()
#verifyAddOnomatopee()
verifyAlter()
#verifyWriteWrongLetter()