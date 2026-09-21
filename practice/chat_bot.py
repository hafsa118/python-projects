# personal chat bot assistant

'''Name = AI study buddy
Tools:
* Python core logic
* string matching -> to analyze and compare user input.
* function
* dictionary
* loops
* condition.

Discription:
* It will be mini chat bot that can interact with user
* it will understand simple massage like "hello" etc.
* And give friendly and intelligent answers
* this is rule base not using AI model but behave intelligently'''

# code
import datetime
import time
time = datetime.datetime.now().hour
if time < 12:
    print("Good morning!")
if 12 <= time < 18:
    print("Good afternoon!")
if 18 <= time < 24:
    print("Good evening!")

print("welcome to rule based Chatbot")
print("you can ask me basic question or type 'bye' to exit from here")

# Memory creation
responses = {
    "hello": "Hi welcome. How can i help you?",
    "how are you": "I am very fine. thank you",
    "Who are you": "I am smart AI study buddy",
    "motivate me": "Keep going. Every bug make you big developer",
    "happy": "great to hear that",
    "function": "I don't know"
}


def get_responsebot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I dont know"


# take user input
while True:
    userInput = input(" asked question:")
    reply = get_responsebot(userInput)
    print("Bot response", reply)


    if "bye" in userInput.lower():
        break