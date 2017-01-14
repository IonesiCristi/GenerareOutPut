import random

#############################
# De aici se foloseste functia   getRandomSintagm() :
# -> daca returneaza False, inseamna ca au fost folosite deja cele 101 expresii
# -> altfel, se returneaza o sintagma, reprezentand una din cele 101 intrebari existente
#############################


'''
Intrebarile au fost luate de pe site-ul http://www.conversationstarters.com/101.htm
'''
conversationStarters = [
    # Ice breakers
    ["Where did you grow up?", 0 ],
    ["Do you have any pets?", 0 ],
    ["Do you have any siblings?", 0 ],
    ["Do you know what your your name means?", 0 ],
    ["What type of phone do you have?", 0 ],
    ["What did you do this past weekend?", 0 ],
    ["What are your plans for this weekend?", 0 ],
    ["What do you like to do in your spare time?", 0 ],
    ["What is the first thing you do when you wake up?", 0 ],
    ["What is the last thing you do before you go to sleep?", 0 ],
    ["What is your middle name?", 0 ],
    ["What was the last thing you purchased?", 0 ],
    ["What is your favorite holiday?", 0 ],
    ["What is your favorite day of the week?", 0 ],
    ["If you could meet anyone in history, who would it be?", 0 ],
    ["What do you like to do to relax?", 0 ],
    ["Are you a saver or a spender?", 0 ],
    ["Do you play any instruments?", 0 ],
    # Childhood Questions
    ["What was your favorite children's book?", 0 ],
    ["What is your first childhood memory?", 0 ],
    ["What type of kid were you (e.g. spoiled, rebellious, well-behaved, quiet, obnoxious...)?", 0 ],
    ["What is one thing you miss about being a kid?", 0 ],
    ["What did you want to grow up to be when you were younger?", 0 ],
    # School/Work Topics
    ["Where did you go to school?", 0 ],
    ["What was your favorite subject at school?", 0 ],
    ["What was your least favorite subject at school?", 0 ],
    ["What's the first thing you do after school/work?", 0 ],
    ["Were you the class clown or teacher's pet?", 0 ],
    ["What do you do for a living?", 0 ],
    ["What is your dream job?", 0 ],
    ["If you had $10 million, would you still be working and going to school?", 0 ],
    ["What was your least favorite job that you've ever had?", 0 ],
    ["What is something that you have gotten in trouble for at school or work?", 0 ],
    # Relationship Questions
    ["What is the first think you notice about a guy or girl?", 0 ],
    ["Have you ever been in love?", 0 ],
    ["Do you believe in soul mates?", 0 ],
    ["What are your turn offs?", 0 ],
    ["Do you believe in love at first sight?", 0 ],
    ["Do you prefer short hair or long hair on a guy/girl?", 0 ],
    ["What do you look for in a guy/girl?", 0 ],
    ["Who was the last person you called?", 0 ],
    ["Would you rather be rich and never find true love or be poor and find true love?", 0 ],
    #Sports Conversation Starters
    ["Who is your favorite athlete?", 0 ],
    ["How often do you exercise?", 0 ],
    ["What is your favorite sports team?", 0 ],
    ["Do you play any sports?", 0 ],
    # Vacation Questions
    ["Where was the last place you went on vacation?", 0 ],
    ["Where do you plan on going for your next vacation?", 0 ],
    ["If you could live anywhere in the world, where would it be?", 0 ],
    ["What countries have you traveled to?", 0 ],
    ["What was your worst vacation experience?", 0 ],
    # Food/Drink Topics
    ["What is your favorite drink?", 0 ],
    ["What is your favorite food?", 0 ],
    ["What is your favorite meal of the day?", 0 ],
    ["Are there any foods that you dislike or will not eat?", 0 ],
    ["Are there any foods that you would like to try?", 0 ],
    ["What is your favorite restaurant?", 0 ],
    ["What is your favorite pizza topping?", 0 ],
    ["What is your favorite ice cream flavor?", 0 ],
    ["What did you have for dinner last night?", 0 ],
    ["What is the signature dish that you cook?", 0 ],
    # Entertainment Topics
    ["Who is your favorite actor?", 0 ],
    ["What is your favorite movie of all time?", 0 ],
    ["What was the worst movie you've ever seen?", 0 ],
    ["What is your favorite TV show?", 0 ],
    ["What was the last movie you've seen?", 0 ],
    ["What type of music do you like to listen to?", 0 ],
    ["Who is your favorite music artist?", 0 ],
    ["What was the last book you read?", 0 ],
    # Personal Questions
    ["Who do you look up to?", 0 ],
    ["Where do you see yourself 5 years from now?", 0 ],
    ["What are you scared of?", 0 ],
    ["What is the best piece of advice you've received?", 0 ],
    ["What do your parents do for a living?", 0 ],
    ["What is your biggest regret?", 0 ],
    ["What is your most embarrassing moment?", 0 ],
    ["What is the craziest thing you've ever done?", 0 ],
    ["What are some of your short-term goals?", 0 ],
    ["What are some of your long-term goals?", 0 ],
    # Misc. Conversation Starters
    ["Do you sleep with a stuffed animal?", 0 ],
    ["Do you drink coffee or tea?", 0 ],
    ["If you could have any super power, what would it be?", 0 ],
    ["If you were stranded on a deserted island and you could have only 1 item, what would it be?", 0 ],
    ["Do you believe in luck?", 0 ],
    ["Tell me about your first car.", 0 ],
    ["Do you play video games?", 0 ],
    ["Do you believe people are inherently good?", 0 ],
    ["How often do you shower?", 0 ],
    ["What is your favorite board game?", 0 ],
    ["What is your favorite charity?", 0 ],
    ["Have you ever gotten a speeding ticket?", 0 ],
    ["Do you prefer cats or dogs?", 0 ],
    ["Would you prefer to live in the city or a rural area?", 0 ],
    ["What is your favorite season?", 0 ],
    ["Do you speak any other languages?", 0 ],
    ["Have you ever cried because you were so happy?", 0 ],
    ["What is the best thing that happened to you during the past week?", 0 ],
    ["What is the worst thing that happened to you during the past week?", 0 ],
    ["Do you sing in the shower?", 0 ],
    ["What is the most valuable thing that you own?", 0 ],
    ["What would you do if you only had 24 hours left to live?", 0 ],
    ]

def getRandomSintagm():
    '''
    Sunt considerate intrebarile din conversationStarters
    :return: O sintagma, reprezentand o intrebare,  sau False, daca deja le-am folosit pe toate.
    '''
    global conversationStarters
    index = random.randint(0, len(conversationStarters)-1)
    print "index", index
    initialIndex = index
    while True :
        print conversationStarters[index][1]
        if conversationStarters[index][1] == 0 :
            conversationStarters[index][1] += 1
            return conversationStarters[index][0]
        index += 1
        print "index", index
        if index == len(conversationStarters):
            index = 0
        if index == initialIndex:
            print "initial index", initialIndex
            print "Au fost folosite toate intrebarile din conversationStarters aparent..."
            return False

print getRandomSintagm()