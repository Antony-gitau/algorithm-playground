
#recursion problem
#code inspired by grokking algorithm book

# let have sum and countdown functions that uses recursion
def sum(arr):
    """
    this function uses recursion to find the sum of the array
    """
    #base case
    if arr == []:
        #if the array is empty, return 0
        return 0
        #if the array is not empty, 
        # return the first element of the array
        #  plus the sum of the rest of the array
    else:
        return arr[0] + sum(arr[1:])

#test the function
print(sum([10,10]))


# a recursive function that prints a count down from n
def countdown(n):
    #base case
    if n == 0:
        print("we finish!")
        #recursive case
    else:
        #print the current value of n
        print(n)
        #call the countdown function with n-1
        countdown(n-1)
#test the function
print(countdown(5))

# another recursive function that prints factorial of n
def factorial(n):
    #base case
    if n == 1:
        return 1
    #recursive case
    else:
        print(n)
        return n * factorial(n-1)
#test the function
print(factorial(5))
