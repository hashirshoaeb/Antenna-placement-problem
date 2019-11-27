import random as r
from chromosome import chromosome

# main file example code:

print ("///////   Generating list of 20 random chormosomes   ///////")
list_of_20Rand = []
for i in range(0, 20):
    list_of_20Rand = list_of_20Rand + [chromosome()]

print ("///////   Sorting list of 20 random chromosomes      ////////")

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is lesser
            # than the next element
            if arr[j].fitnessValue < arr[j + 1].fitnessValue:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubbleSort(list_of_20Rand)
# for i in list_of_20Rand:
    # print(i.fitnessValue)