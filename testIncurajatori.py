import incurajatori
import time

text = [
    "Ana are mere si se plimba.",
    "Urmaresc emisiunea 'Go There' saptamanal.",
    "Cum poti sa spui ASA CEVA?"
    "Nu inteleg cateva idei de-ale tale.",
    "Privesc in zare si ma intreb ce e viata.",
    "De unele lucruri nu ma mai satur.",
    "Roxana , Mihai si George sunt prieteni din timpul liceului."
]

def verifyCreeazaSintagmaMagulire():
    print ("Adauga sintagme de apreciere si incurajare: ")
    time.sleep(2)
    for i in range(len(text)):
        print ("original \t ", text[i])
        modifyedText = incurajatori.creeazaSintagmaMagulire(text[i])
        print ("modifyed \t ", modifyedText, "\n\n")
        time.sleep(4)


verifyCreeazaSintagmaMagulire()