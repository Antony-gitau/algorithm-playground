# Algorithm Playground

This repository contains solutions to the blind 75 problems on [Neetcode.io](https://neetcode.io) site. 

My intention is to solve these problems as outlined on [this sheet](https://docs.google.com/spreadsheets/d/1MnkzzanUtLieQAnUXSDaHtDcdTwhM9GUqLqK7eUta-o/edit#gid=0) a copy from Neetcode.io. 

I intend to describe the strategy explained by Neetcode as well as my strategy or other strategies that come to my mind. 
I will focus on using python in most implementation. However, I might use C/C++ at times.

Apart from having a readme section for every solution, I will heavily comment the code to ensure that every line is understood to even a beginner.

Some implementations:

- [Quick sort](https://github.com/Antony-gitau/QuickSort_algorithm)
- [Linked lists](https://github.com/Antony-gitau/linked_list)
- [Insertion sort](https://github.com/Antony-gitau/insertion_sort_algorithm)
- [Bubble sort](https://github.com/Antony-gitau/bubble_sort_algorithm)
- [Selection sort](https://github.com/Antony-gitau/selection_sort_algorithm)


Big O notation:
This is a measure of the number of operations an algorithm has to take, in the worst case scenario, to get to the desired solution. 

For example,
if I have a list of 100 names arranged inorder and I am using a simple search algorithm (good-old fashion of going through all names one by one), then if the name I am looking for is at the end of the list, I will have to make 100 operations to get to the desired name (solution)

common Big 0 runtimes
- O(log n) this is the fastest runtime. For example the binary search algorithm has this runtime. This means that a 100 ordered list of items, this algorithms takes log 100 = 6.64 operations to find an answer. This is fast compared to 
- O(n). Big O of n means that the number of operations is equal to the length of the list. So with the 100 list of items, we talked about, we will need 100 operations in the worst case to get to a solution. However this is the second fastest operation.
- O(nlog n)
- O(n^2)
- O(2!) factorial time