import randomSintagm

def testGetRandomSintagm():
    for index in range(50):
        sintagm = randomSintagm.getRandomSintagm()
        print index," -- ", sintagm
        if sintagm == False:
            print "Now you should make something else, we already used all the expresions.."
    print "Let's see number of uses of an exxpresion and the expresion."
    for index in xrange(len(randomSintagm.conversationStarters) - 1):
        print randomSintagm.conversationStarters[index][1], " ----- ", randomSintagm.conversationStarters[index][0]


testGetRandomSintagm()
