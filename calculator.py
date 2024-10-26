#!/usr/bin/env python3

def check_valid_operand(operand):
        valid_operands = ["+","-","*","/"]
        while operand not in valid_operands:
            operand = input("please enter valid operand - one of + - * or /\n")
        return operand
        
def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x/y


def main():

    print("##########################################\n######## Simple Python Calculator ########\n##########################################\n\n") 


    operand = input("Specify the operand as one of + - / *\n")
    operand = check_valid_operand(operand)
        
    num1 = float(input("Specify the first number: "))
    num2 = float(input("specify the second number: "))

    if (operand == "+"):
        print(f"The answer is {addition(num1,num2):g}")
    elif (operand == "-"):
        print(f"The answer is {subtraction(num1,num2):g}")
    elif (operand == "*"):
        print(f"The answer is {multiplication(num1,num2):g}")
    elif (operand == "/"):
        print(f"The answer is {division(num1,num2):g}")

 

if __name__ == "__main__":
    main()