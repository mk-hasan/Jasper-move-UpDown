import re

WORDS = ["DESK","UP","DOWN","STOP","MOVE"]

def handle(text, mic, profile):

    mic.say("Desk Should be move up or down")
    textinput = mic.activeListen()
    if(textinput == "UP"):
        //mic will say moving up 
        mic.say("Moving Up")



def isValid(text):
  //will check if the text valid
    return bool(re.search(r'\bdesk\b',text,re.IGNORECASE))
