#the valid parenthesis function
def is_valid(s):
    #initiate an empty stack a string in this case
    stack = []

    #a dictionary to help us map opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    #go through all the characters in the string
    for char in s:

        #if it is an opening bracket
        if char in brackets.values():
            #add it to the stack
            stack.append(char)
            #if the character is a closing bracket
        elif char in brackets.keys():
            #confirm that the stack is not empty
            #and that the value of "brackets[char" which is
            #an opening character is the same as the most recent value on the stack
            if not stack or brackets[char] != stack.pop():
                #if the if statement is true, then our two conditions are not satisfied.
                #so we return a false
                return False
     #the final output is an empty stack as all brackets should be validated       
    return not stack
