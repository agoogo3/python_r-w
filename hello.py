import random, glob,re


list_quest = [ "How old are you: ",
    "What is your Favorite color: ",
    "What is your Favorite Soccer team: ",
    "Which high school did you attend: ",
    "What is your Favorite food: ",
    "Which city do you live in: ",
    "What is your Favorite game: ",
    "Who is your Favorite actor: ",
    "Who is your Favorite musician: "
   
]

list_answers= []
answer_statement = []
def questions():
    questions_index = random.sample(range(len(list_quest)),3)
    return questions_index

def choices():
    list_answers.clear()
    answer_statement.clear()
    while True:
        name = input("What is your name: ")
        if re.fullmatch("[A-Za-z]+",name):
            break
        print("Only First name with letters")
    list_answers.append(name)
    answer_statement.append(f"Hello {name}!")
    for question in questions():
        print(list_quest[question])
        answer_input = input()
        list_answers.append(answer_input)
        answers_statement(question,answer_input)
    print("Do you want to save user?\n 1. Yes 2. No")
    save_input = input("")
    if save_input == "1":
        save_info(name,answer_statement)
        options()
    elif save_input == "2":
        options()
        
        

def answers_statement(index, answer):
    statements = [
        f"You are {answer} years old",
        f"You love the color {answer}",
        f"Your favorite soccer team is {answer}",
        f"You attended {answer}",
        f"Your favorite food is {answer}",
        f"You live in {answer}",
        f"You love playing {answer}",
        f"Your favorite actor is {answer}",
        f"Your favorite musician is {answer}"
    ]
    if 0 <= index < len(statements):
        answer_statement.append(statements[index])

def save_info(firstname, statement):
    try:
        with open(f"{firstname}.txt", 'x') as f:
            state = "\n".join(statement)
            f.write(f"{state}")
            print(state)
    except FileExistsError:
        print("Error: User already exists. Please try again ")

def read_user(name):
    try:
        with(open(f"{name}.txt",'r',encoding='utf-8')) as file:
            content = file.read()
            response = [True,content]
    except FileNotFoundError:
        response = [False,"Error: Name not found."]
    return response

def view_users():
    files = glob.glob("*.txt")
    print("\n".join(files))
    print("Do you want to view user details?")
    detail_choice = input("1.Yes \n 2. No \n")
    if detail_choice == '1':
        while True:
            name_input = input("Type the user's name(without .txt): ")
            stat = read_user(name_input)
            if not stat[0]:
                print(stat[1])

            else: print(stat[1] + "\n")
            break

    elif detail_choice == "2":
        return
    else:
        print("Incorrect choice")
            





def options():
    print("Hello there, How can we help you? ")
    while True:
        print("\n 1. Add a user \n 2. View users \n 3. Exit")
        opt_input = input("")
        if opt_input == "1":
            choices()
        elif opt_input == "2":
            view_users()
        elif opt_input == "3":
            break
        else:
            print("Incorrect choice. Please try again")
    


options()

# print("\n".join(answer_statement))




