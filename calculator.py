#!/usr/bin/env python3

def check_valid_operand(operand):
    
    """
    Check user enters valid operand

    Args: 
        operand (str) A string representing whether addition, subtraction, multiplication, or division is the desired function
    """

    valid_operands = ["+","-","*","/"]
    while operand not in valid_operands:
        operand = input("please enter valid operand - one of + - * or /\n")
    return operand

def check_user_ans(user_ans):

    """
    Check whether user answers Yes or No in response to performing another calculation. 

    Args: 
        user_ans: (str) A string indicating whether the user would lke to perform another calculation, or exit the program
    """

    valid_user_ans = ["yes","no"]
    while user_ans not in valid_user_ans:
        user_ans = input("Please enter Yes or No \n").lower()
    return user_ans

def addition(x,y):

    """
    Perform addition function

    Args: 
        x: (float) Number representing the first addend
        y: (float) Number representing the second addend
    """

    return x + y

def subtraction(x,y):

    """
    Perform subtraction function

    Args: 
        x: (float) Number representing the first minuend
        y: (float) Number representing the second subtrahend
    """

    return x - y

def multiplication(x,y):

    """
    Perform multiplication function

    Args: 
        x: (float) Number representing the first multiplicand
        y: (float) Number representing the second multiplier
    """

    return x * y

def division(x,y):

    """
    Perform division function

    Args: 
        x: (float) Number representing the first dividend
        y: (float) Number representing the second divisor
    """

    return x/y


def main():

    print("##########################################\n######## Simple Python Calculator ########\n##########################################\n\n") 


    while True: 

        operand = input("Specify the operand as one of + - / *\n")
        operand = check_valid_operand(operand)
            
        num1 = float(input("Specify the first number: "))
        num2 = float(input("Specify the second number: "))

        if (operand == "+"):
            print(f"The answer is {addition(num1,num2):g}")
        elif (operand == "-"):
            print(f"The answer is {subtraction(num1,num2):g}")
        elif (operand == "*"):
            print(f"The answer is {multiplication(num1,num2):g}")
        elif (operand == "/"):
            print(f"The answer is {division(num1,num2):g}")
        
        user_ans = input("Would you like to perform another calculation? Enter Yes or No\n").lower()
        user_ans = check_user_ans(user_ans)

        if (user_ans.lower()=="no"):
            print("Thank you for using Simple Calculator!")
            break

if __name__ == "__main__":
    main()