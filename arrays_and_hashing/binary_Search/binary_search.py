#binary function that will take a list of ordered arrays 
#and also a desired item (which could be a number, name, etc)

def Binary_Seach(ordered_list, desired_item):
    #get the location of the guess - that is the lowest and the highest number
    #starting with the first to the last element of the list

    lowest_element = 0
    highest_element = len(ordered_list) - 1

    #check whether the guessed element is smaller than the desired element(item) within the array

    while lowest_element < highest_element: #we are within the array
        #we start by guessing the middle number
        #for example if we have 100 elements, we start by guessing 50
        middle_element = (lowest_element+highest_element)/2
        return middle_element #the middle element is the guess we make

        #check whether the middle element is equal to desired element
        #if not check whether is is smaller or larger than the desired element

        if middle_element == desired_item: #if the middle element is the desired element , then we fpund it!
            return middle_element

            #if we didn't find it, check whether it is lower or higher and update the location we are at
        if middle_element <= desired_item:
            lowest_element = middle_element + 1 #add one since, the next element iafter the middle element s the now the lowest element
        else:
            highest_element = middle_element - 1 #subtract one, since the previous element before the middle element is now the highest element

    return None #if the desired element is out of the range of the elements, we output a null




