def perform_operation(num1, num2, operation):
    if(operation == 'add'):
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        if(num2 == 0): 
            return "The Devision By Zero is not Allowed"
        else:
            return num1 / num2
