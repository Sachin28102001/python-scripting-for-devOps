import sys

def addition(num1 , num2):
    add = num1 + num2
    return add
    
def subtraction(num1 , num2):
    sub = num1 - num2
    return sub
    
def multiplication(num1 , num2):
    mult = num1 * num2
    return mult
    
def division(num1 , num2):
    div = num1/num2
    return div
    
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    result = addition(num1, num2)
    print(result)
    
if operation == "multiplication":
    result = multiplication(num1 , num2)
    print(result)
    
if operation == "subtraction":
    result = subtraction(num1 , num2)
    print(result)
    
if operation == "division":
    result = division(num1 , num2)
    print(result)