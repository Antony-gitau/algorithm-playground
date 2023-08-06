#revising selection sort 
#code insipred by grokking algorithm book
def findsmall(arr):
    """
    this function finds the smallest value in the array
    we take the first element and its index as the smallest
    """
    smallest = arr[0]
    smallest_index = 0

    for indx in range(1, len(arr)):
        """
        we compare the smallest index to the current index
        if the current index is smaller, then we update its value and index as smallest
        """
        if arr[indx] < smallest:
            smallest = arr[indx]
            smallest_index = indx
    return smallest_index


#now that we can find the index of the smallest value using above function,
#lets implement the selection sort

def selectionSort(arr):
    """
    This function creates a new array
    then goes through the array to be sorted from smallest to largest
    it calls the findsmall() to get the index of the smallest value
    pop that value from the given array that we are sorting
    and append that smallest value in a new array that will hopefully have a sorted list
    """
    newarr = []
    for indx in range(len(arr)):
        smallest = findsmall(arr)
        newarr.append(arr.pop(smallest))
    return newarr