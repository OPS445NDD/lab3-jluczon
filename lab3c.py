#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate'''
# Author ID: jluczon

def operate(number1, number2, operator):
    result = 'Error: function operator can be "add", "subtract", or "multiply"'
    if str(operator) == 'add':
        result = int(number1) + int(number2)
    elif str(operator) == 'subtract':
        result = int(number1) - int(number2)
    elif str(operator) == 'multiply':
        result = int(number1) * int(number2)
    
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
