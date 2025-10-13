# Step 1: Create an empty list to hold quiz questions.

quiz_questions = []

# Step 2: Define a function to add a new quiz question.
# This function should prompt the user for the question, options, and the correct answer.
# Store each question as a dictionary in the list.
# hint: dictionary could have keys like 'question', 'options', 'correct_answer'
# hint: options could be stored as a list of strings

def add_question():
    question = input("Enter the question: ")
    options = []
    for i in range(4):  # Assuming 4 options
        option = input(f"Enter option {i+1}: ")
        options.append(option)
    correct_answer = input("Enter the correct answer (e.g., A, B, C, D): ")
    quiz_questions.append({
        'question': question,
        'options': options,
        'correct_answer': correct_answer
    })

# Step 3: Define a function to write the quiz questions to a file called 'quiz_questions.txt'.
# Format the questions nicely for readability, including the question text and possible answers.
# hint: loop through your list of dictionaries
# hint: use \n for formatting and spacing between questions

def write_questions():
    with open('quiz_questions.txt', 'w') as file:
        for i, q in enumerate(quiz_questions, 1):
            file.write(f"Question {i}: {q['question']}\n")
            for j, opt in enumerate(q['options']):
                file.write(f"{chr(65+j)}. {opt}\n")  # A, B, C, D
            file.write(f"Correct Answer: {q['correct_answer']}\n\n")

# Step 4: Define a function to display all current quiz questions in the console.
# hint: similar to step 3, but use print() instead of file writing

def display_questions():
    for i, q in enumerate(quiz_questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, opt in enumerate(q['options']):
            print(f"{chr(65+j)}. {opt}")
        print(f"Correct Answer: {q['correct_answer']}\n")

# Step 5: In the main part of the program:
# - Call the function to add questions in a loop until the user decides to stop.
# - After finishing, call the function to write all questions to 'quiz_questions.txt' in a nice, human-readable format
# - Optionally, display the questions on the console before writing them to the file.
# hint: use a while loop and you could ask user if they want to continue after each question

while True:
    add_question()
    cont = input("Do you want to add another question? (yes/no): ")
    if cont.lower() != 'yes':
        break

display_questions()
write_questions()