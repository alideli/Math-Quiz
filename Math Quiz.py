import random
import time

def number_generator():
    num1 = random.randint(1,9)
    num2 = random.randint(1,99)
    operate_list = ['+','-','*','/','**','sqrt']
    operate = random.choice(operate_list)
    if(operate == 'sqrt'):
        print("What is {0} {1} ?".format(operate, num2))
    else:
        print("What is {0} {1} {2} ?".format(num1, operate, num2))
    if(operate == '+'):
        return num1 + num2
    elif(operate == '-'):
        return num1 - num2
    elif(operate == '*'):
        return num1 * num2
    elif(operate == '/'):
        print(num1 / num2)
        return num1 / num2
    elif(operate == '**'):
        return num1 ** num2
    elif(operate == 'sqrt'):
        return num2 ** 0.5
    
print("There is 10 questions\nYou need 5 correct answers :)")
print('*'*20)
question_number = 10
right_answer = 0
time_limit = 10
while(question_number > 0):
    if(right_answer < 5):
        result = str(number_generator())
        start_time = time.time()
        user_answer = input("Your answer : ")
        end_time = time.time()
        time_diff = end_time - start_time
        if(time_diff <= time_limit):
            if(user_answer == result):
                right_answer += 1
                print("Correct!!! go for another")
                print("You answered {0} questions correctly".format(right_answer))
                print('*'*20)
            else:
                print("Wrong!!! try again")
                print('*'*20)
        else:
            print("too late for answer")
    else:
        print("You Won!!!")
        break
    if(question_number == 1):
        print("You lost!!!")
    question_number -= 1