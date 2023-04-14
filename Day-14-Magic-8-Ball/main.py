#Magic 8 ball
import random

def magic_eight_ball():
    responses = ["It is certain.", "Without a doubt.", "You may rely on it.", "Yes, definitely.", "It is decidedly so.",
                 "As I see it, yes.", "Most likely.", "Yes.", "Outlook good.", "Signs point to yes.",
                 "Reply hazy, try again.", "Better not tell you now.", "Ask again later.", "Cannot predict now.", "Concentrate and ask again.",
                 "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful.", "My reply is no."]
    question = input("Ask the Magic 8 Ball a question: ")
    response = random.choice(responses)
    print(f"The Magic 8 Ball says: {response}")

magic_eight_ball()
