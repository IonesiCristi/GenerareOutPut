import rawWords
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

def testExtractEligibleWords():
    print("Extragere cuvinte ce nu sunt substantive proprii si determinare partea de vorbire a fiecaruia:")
    for sentence in text:
        print("original: \t ", sentence)
        words = rawWords.extractEligibleWords(sentence)
        print("Tokenized si fara substantive proprii:",words,"\n\n")
        time.sleep(2)


testExtractEligibleWords()
