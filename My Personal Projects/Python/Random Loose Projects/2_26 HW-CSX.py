
import random

question_bank = [
    "What's your name? ",
    "What school do you go to? ",
    "What's your favorite food? ",
    "What's your age? ",
    "What time is it? ",
    "What's your most played song? "
]

question_answ = []

for _ in range(10): 
    random_quest = random.choice(question_bank) 
    answer = input(random_quest) 
    question_answ.append((random_quest, answer))
for question, answer in question_answ:
    print(f"Question: {question} Answer: {answer}")