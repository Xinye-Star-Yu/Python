
def createStack(): 
    stack = [] 
    return stack 
  
# Function to check if  
# the stack is empty 
def isEmpty( stack ): 
    return len(stack) == 0
  
# Function to push an  
# item to stack 
def push( stack, item ): 
    stack.append( item ) 
  
# Function to get top  
# item of stack 
def top( stack ): 
    p = len(stack) 
    return stack[p-1] 
  
# Function to pop an  
# item from stack 
def pop( stack ): 
  
    # If stack is empty 
    # then error 
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 
  
# Function to print the stack 
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
  
# Driver Code 
stack = createStack() 
push( stack, str(3) ) 
push( stack, str(5) ) 
push( stack, str(2) ) 
push( stack, str(1) ) 
push( stack, str(4) ) 
push( stack, str(6) ) 
  
print("Sorted numbers are: ") 
sortedst = sortStack ( stack ) 
prints(sortedst) 
