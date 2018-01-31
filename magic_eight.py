from random import randrange, choice

def askquestion():
    if '?' not in question:
        print("I'm sorry. I can only answer questions.")
    else:
        return(poss_answers())


def poss_answers():
    poss_ans = [
    "It is certain",  "It is decidedly so", " Without a doubt"," Yes definitely", "You may rely on it",
    "As I see it, yes", "Most likely", " Outlook good", " Yes", "Signs point to yes",
    " Reply hazy try again", "Ask again later", " Better not tell you now", "Cannot predict now", "Concentrate and ask again",
    "Don't count on it", " My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
    ]
    return print(choice(poss_ans))

question = ""
while True:
    question= input("What is your question? ")
    if question =="quit":
        break
    askquestion()
