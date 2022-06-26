# Magic 8 Ball

import sys
import random

#  Magic 8 Ball answers
answers = {
    "a": {"Yes"},
    "b": {"It is certain."},
    "c": {"It is decidedly so."},
    "d": {"Without a doubt."},
    "e": {"Yes definitely."},
    "f": {"You may rely on it."},
    "g": {"As I see it, yes."},
    "h": {"Most likely."},
    "i": {"Outlook good."},
    "j": {"Yes."},
    "k": {"Signs point to yes."},
    "l": {"Reply hazy, try again."},
    "m": {"Ask again later."},
    "n": {"Better not tell you now."},
    "o": {"Cannot predict now."},
    "p": {"Concentrate and ask again."},
    "q": {"Don't count on it."},
    "r": {"My reply is no."},
    "s": {"My sources say no."},
    "t": {"Outlook not so good."},
    "u": {"Very doubtful."}
}

"""""
Function to provide a random responses
Convert dict to list
Choice a random item from list
Output random phrase
"""""

def response():
    answer_list = list(answers.values())
    random_answer = random.choice(answer_list)
    print(''.join(random_answer))

#  Loop to enter a question or exit system
while True:
    global user_question
    user_question = input("\nAsk me a question and I will tell you your fate or type 'exit' to exit:\n").lower()
    if user_question == "exit":
        print("Thanks for playing!")
        sys.exit()
    else:
        response()
