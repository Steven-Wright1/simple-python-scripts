#!/usr/bin/env python3

def check_input(prompt, valid_options):
    
    """
    Check user input against valid options

    Args: 
        prompt (str): input provided by the user as a string
        valid_options (list): A list of valid options
    """

    user_input = input(prompt).lower()

    while user_input not in valid_options:
        user_input = input(f"Please enter a valid option from: {' '.join(valid_options)}\n").lower()

    return user_input


def addition(x,y):

    """
    Perform addition function

    Args: 
        x: (float): Number representing the first addend
        y: (float): Number representing the second addend
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

    if (y==0):
        print ("It is not possible to divide by 0")
        return None
    return x/y


def main():

    print("##########################################\n######## Simple Python Calculator ########\n##########################################\n\n") 


    while True: 

        operand = check_input("Specify the operand as one of + - / *\n", ["+","-","/", "*"])

            
        num1 = float(input("Specify the first number: "))
        num2 = float(input("Specify the second number: "))

        if (operand == "+"):
            print(f"The answer is {addition(num1,num2):g}")
        elif (operand == "-"):
            print(f"The answer is {subtraction(num1,num2):g}")
        elif (operand == "*"):
            print(f"The answer is {multiplication(num1,num2):g}")
        elif (operand == "/"):
            result = division(num1,num2)
            if result is not None:
                print(f"The answer is {result:g}")
        
        user_ans = check_input("Would you like to perform another calculation?\n", ["yes","no"])
        if (user_ans.lower()=="no"):
            print("Thank you for using Simple Calculator!")
            break

if __name__ == "__main__":
    main()