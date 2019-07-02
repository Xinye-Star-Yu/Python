from stack_array import Stack
#Using ast for literal_eval
import ast

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    # Evaluates a postfix expression
    # Input argument:  a string containing a postfix expression where tokens
    # are space separated.  Tokens are either operators + - * / ^ or numbers
    # Returns the result of the expression evaluation.
    # Raises an PostfixFormatException if the input is not well-formed

    #Delimiter
    postfixList = input_str.split(" ")
    #Creates Stack with capacity of the lenght of the delimited list
    postfixStack = Stack(len(postfixList))

    #For each element in the pfList
    for token in postfixList:
        try:
            #Try to push to stack if it is a number
            postfixStack.push(ast.literal_eval(token))
        except:
            #If a 'normal' operator is encountered
            if token in "*/+-^**":
                try:
                    #Pops the top two numbers on the stack then applies the
                    #token operator with pfMath()
                    numberTwo = postfixStack.pop()
                    numberOne = postfixStack.pop()
                    postfixStack.push(pfMath(token, numberOne, numberTwo))
                except:
                    #Checks for div 0 otherwise raises Insufficient operands
                    if numberTwo == 0:
                        raise ValueError("Undefined: Can't Divide By 0")
                    else:
                        raise PostfixFormatException("Insufficient operands")
            #For bit shift
            elif token in "<<>>":
                try:
                    #Attemps to pop top two on the stack
                    numberShifter = postfixStack.pop()
                    numberBase = postfixStack.pop()
                    #Left bit Shift
                    if token == "<<":
                        postfixStack.push(numberBase << numberShifter)
                    #Right bit Shift
                    else:
                        postfixStack.push(numberBase >> numberShifter)
                #Can't bit shift raise error
                except:
                    raise PostfixFormatException("Illegal bit shift operand")
            #Not a token or number
            else:
                raise PostfixFormatException("Invalid token")
    #End of postfixList checks what is on the stack
    if postfixStack.size() != 1:
        raise PostfixFormatException("Too many operands")
    #Returns the evaluated postfix
    return postfixStack.pop()

def infix_to_postfix(input_str):
    # Converts an infix expression to an equivalent postfix expression
    # Input argument:  a string containing an infix expression where tokens are
    # space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    # Returns a String containing a postfix expression

    #Precedent
    orderOfOperations = {'<<': 5, '>>': 5, '^': 4, '**': 4, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    #Delimiter
    infixList = input_str.split(" ")
    #Sets up stack with capacity of the len of the delimited string
    opStack = Stack(len(infixList))
    #Output holder
    postfixOutput = []

    #For each element in the list of infix
    for token in infixList:
        try:
            #Using ast.literal_eval
            postfixOutput.append(ast.literal_eval(token))
        except:
            #Open ( push
            if token == "(":
                opStack.push(token)
            #Close ) stack pop
            elif token == ")":
                head = opStack.pop()
                while head != "(":
                    postfixOutput.append(head)
                    head = opStack.pop()
            elif orderOfOperations[token] == 4:
                opStack.push(token)
            else:
                #When the stack isn't empty and the ooO on the stack is greater then the current ooO
                while not (opStack.is_empty()) and (orderOfOperations[opStack.peek()] >= orderOfOperations[token]):
                    postfixOutput.append(opStack.pop())
                opStack.push(token)
    while not (opStack.is_empty()):
        postfixOutput.append(opStack.pop())
    #Recreate the string join together
    return " ".join(str(pfUnit) for pfUnit in postfixOutput)

def prefix_to_postfix(input_str):
    # Converts a prefix expression to an equivalent postfix expression
    # Input argument: a string containing a prefix expression where tokens are
    # space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    # Returns a String containing a postfix expression(tokens are space separated)

    #Delimiter + Reverse
    prefixString = list(reversed(input_str.split(" ")))
    #Stack setup with capacity equal to len of list
    prefixStack = Stack(len(prefixString))

    #For each element in the list
    for token in prefixString:
        #Token checker
        if token in "*/+-^**>><<":
            #Pops top 2 then assembles as postfix
            numberOne = prefixStack.pop()
            numberTwo = prefixStack.pop()
            tempString = numberOne + " " + numberTwo + " " + token
            #Pushes string back on the the stack
            prefixStack.push(tempString)
        else:
            prefixStack.push(token)
    #Returns the string accumulator
    return prefixStack.peek()


#Extra function to aid in math
def pfMath(operator, numberOne, numberTwo):
    if operator == "*":
        return numberOne * numberTwo
    elif operator == "/":
        return numberOne / numberTwo
    elif operator == "+":
        return numberOne + numberTwo
    elif operator == "-":
        return numberOne - numberTwo
    elif operator == "^" or operator == "**":
        return numberOne ** numberTwo
