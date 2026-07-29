quiz = {
    'What is 2 plus 2?: ' : 4,
    'What is the capital of Nigeria?: ' : 'Abuja',
    'How many months are in a year?: ' : 12,
    'How many weeks are in a year?: ' : 52,
    'How many days are in a month?: ' : 30
    }

running_score = 0

def ask_and_check ():
    global running_score
    for key, value in quiz.items():
            user_answer = input(key)
            if user_answer == str(value):
                print('Correct answer!')
                running_score += 1
            else:
                print("Wrong answer!")
      

def final_score():
     print(f'You scored {running_score}/{len(quiz)}!')

ask_and_check()
final_score()
     
                     