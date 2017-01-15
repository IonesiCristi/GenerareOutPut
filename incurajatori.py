import random

expresiiIncurajareIncepere = [
    "Give it a try.",
    "Go for it.",
    "Why not?",
    "It's worth a shot.",
    "What are you waiting for?",
    "What do you have to lose?",
    "You might as well.",
    "Just do it."
]

expresiiApreciere = [
    "I like",
    "I apreciate",
    "I adore",
    "It's interesting",
    "It's good",
    "It's allways pleasant"
]

sintagmeApreciate = [
    " what you say. ",
    " what you ask. ",
    " what you have in mind. ",
    " your imagination. ",
    " your originality. ",
    " how you came up with new ideas. ",
    " to see a question like this one. ",
    " to have a conversation like ours. ",
    " when somebody asks such a thing. ",
    " to surprise me with a tricky question. ",
    " how the conversation just flows away. ",
    " that you make me think. ",
    " how you make me think. ",
    " you make me remember lessons learnt long time ago. ",
    " you encourage me remember old ideas. "
]
expresiiIncurajareContinuare = [
    "There you go!",
    "Keep up the good work.",
    "Keep it up.",
    "Good job.",
    "I'm so proud of you!",
    "Hang in there.",
    "Don't give up.",
    "Keep pushing.",
    "Keep fighting!",
    "Stay strong.",# prea mult?
    "Never give up.",
    "Come on! You can do it.",
    "I'll support you either way.",
    "I'm behind you 100%.",
    "It's totally up to you.",
    "It's your call.",
    "Follow your dreams.",
    "Reach for the stars.",
    "Do the impossible.",
    "Believe in yourself.",
    "The sky is the limit."
]

def creeazaSintagmaMagulire(text):
    indexCumApreciaza = random.randint(0, len(expresiiApreciere)-1)
    indexCeApreciaza = random.randint(0, len(sintagmeApreciate)-1)
    indexContinuare = random.randint(0, len(expresiiIncurajareContinuare)-1)

    raspuns = ""+expresiiApreciere[indexCumApreciaza] \
              + sintagmeApreciate[indexCeApreciaza] \

    return "" + text + "\n" + raspuns
