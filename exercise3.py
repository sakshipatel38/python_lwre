import random 
print("welcome to mini KBC")
def question_generator():
    Basic_questions = {"What is the capital of India?": "New Delhi",
                       "What is the largest planet in our solar system?": "Jupiter",
                       "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
                       "What is the chemical symbol for water?": "H2O",
                       "How many continents are there on Earth?": "7"}
    modrated_questions = {"What is the capital of France?": "Paris",
                          "What is the smallest prime number?": "2",
                        "Who painted the Mona Lisa?": "Leonardo da Vinci"}
    hard_questions = {"What is the capital of Mongolia?": "Ulaanbaatar",
                      "What is the square root of 256?": "16"}
    
    return Basic_questions,modrated_questions,hard_questions

def price_money(level):
    if level == 0:
        return 0
    elif level == 1:
        return 1000
    elif level == 2:
        return 5000
    elif level == 3:
        return 10000
    elif level == 4:
        return 50000
    elif level == 5:
        return 100000
    elif level == 6:
        return 500000       
    elif level == 7:
        return 1000000
    elif level == 8:
        return 5000000
    elif level == 9:
        return 10000000
    elif level == 10:
        return 70000000
    else: 
        quit()

def total_money_calculator(level):
    total_money = 0
    for i in range(level):
        total_money += price_money(i)
    return total_money

def play_game(start_game=True):
    Basic_questions,modrated_questions,hard_questions = question_generator()
    level = 0
    total_money = 0

    while level <= 10:
        if level <=5 :
            question, answer = random.choice(list(Basic_questions.items()))
        elif level <=8 :
            question, answer = random.choice(list(modrated_questions.items()))
        else:
            question, answer = random.choice(list(hard_questions.items()))

        print(f"Level {level} for Rs. {price_money(level)}")
        print(question)
        user_answer = input("candidate answer: ")

        if user_answer.strip().lower() == answer.strip().lower():
            total_money += int(price_money(level))
            print(f"correct answer ! you have won Rs. {total_money}")
            level +=1
        else:
            print(f"wrong answer! The correct answer was {answer}. You won Rs. {total_money}")
            break
    print(f"Thank you for playing! You won a total of Rs. {total_money}")
    print("GoodBye!")

user = input("Enter your name: ")
print(f"Hello {user}, let's start the game!")
start_game=play_game()
