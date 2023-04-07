from Stack import Stack

def Main():
    expression = input("Enter a postfix expression: ").strip()
    expression = insertBlanks(expression)
    try:
        print(expression, "=", postfix(expression))
    except:
        print("Wrong expression: ", expression)
    
    

def postfix(expression):
    operand = Stack()
    for symbol in expression.split(" "):
        if len(symbol) == 0:
            continue
        elif symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            processOperator(operand, symbol)
        else:
            operand.push(float(symbol))
    return operand.pop()
            
            
        
def processOperator(operandStack, operator):
    op1 = operandStack.pop()
    op2 = operandStack.pop()
    if operator == '+': 
        operandStack.push(op2 + op1)
    elif operator == '-':
        operandStack.push(op2 - op1)
    elif operator == '*': 
        operandStack.push(op2 * op1)
    elif operator == '/':
        operandStack.push(op2 / op1)
    
    
def insertBlanks(s):
    result = ""

    for ch in s:
        if ch == '+' or ch == '-' or ch == '*' or ch == '/':
            result += " " + ch + " "
        else:
            result += ch
    
    return result


Main()