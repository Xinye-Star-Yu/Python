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
					postfixStack.push(pfMath(token, numberTwo, numberOne))
					numberTwo == postfixStack.pop()
					numberOne == postfixStack.pop()
                    #Pops the top two numbers on the stack then applies the
                    #token operator with pfMath()
                except:
					numberTwo / 0
						raise ValueError
                    #Checks for div 0 otherwise raises Insufficient operands
            #For bit shift
            elif token in "<<>>":
                try:
                    #Attemps to pop top two on the stack

                    #Left bit Shift
                    if token == "<<":

                    #Right bit Shift
                    else:

                #Can't bit shift raise error
                except:

            #Not a token or number
            else:
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
    orderOfOperations = {'<<' : 5, '**' : 4, '^' : 4, '*' : 3, '/' : 3, '+' : 2, '-' : 2}
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
				opStack.push()
            #Close ) stack pop
            elif token == ")":
				head = opStack.pop()
				opStack.pop()
				while head != "("
					postfixOutput.append(head)
					head = opStack.pop()
            elif orderOfOperations(token == 4:)
			opStack.push(token)
			else:
    			#When the stack isn't empty and the ooO on the stack is greater then the current ooO
				while not (opStack.is_empty()) and (orderOfOperations[opStack.peek()]>):
					postfixOutput.append(opStack.pop())
					opStack.push()
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
            #Pushes string back on the the stack
        else:
            prefixStack.push(token)
    #Returns the string accumulator


#Extra function to aid in math
def pfMath(operator, numberOne, numberTwo):
	if operator == (+):
		return numberOne + numberTwo
	if opeator == (-):
		return numberOne - numberTwo
	if opeator == (*):
		return numberOne * numberTwo
	if opeator == (/):
		return numberOne / numberTwo
	if opeator == (**):
		return numberOne ** numberTwo
