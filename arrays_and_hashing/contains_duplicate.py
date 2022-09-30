#checking duplicate function


def checkDuplicates(self, nums: list[int]) -> bool:
    
    #create a hashset - basically a list of empty non-repetitive values

    hashset = set()

    #for all the values in the num list check whether they exist in the hashset
    for num in nums:
        if num in hashset: #if the value is in hashset then this list has duplicates
            return True #we return true to mean that the list has duplicates
        hashset.add(num) #otherwise we add the number to the hashnet
    return False #if after looping through all the values, we didnt find any duplicates, then we return false.
