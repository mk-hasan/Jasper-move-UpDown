import re

WORDS = ["DESK","UP","DOWN","STOP","MOVE"]

def handle(text, mic, profile):

    mic.say("Desk Should be move up or down")
    textinput = mic.activeListen()
    if(textinput == "UP"):
        mic.say("Moving Up")



def isValid(text):

    return bool(re.search(r'\bdesk\b',text,re.IGNORECASE))
    mic.say("Text is vali")
