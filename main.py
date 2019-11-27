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

print ("///////   Selecting best 10 chromosomes   ////////")
selected10 = list_of_20Rand[:10]
for i in selected10:
    print(i.chrom , " with fitness ", i.fitnessValue)

print ("///////   Crossing over best 10 chromosomes   ////////")
for i in range(0, 10, 2):
    selected10[i].crossover(selected10[i+1], r.choice([1,2,3,4]))
    print(selected10[i].chrom, " with fitness ", selected10[i].fitnessValue)
    print(selected10[i + 1].chrom, " with fitness ", selected10[i + 1].fitnessValue)

print( "///////   Randomly Mutating each chromosome   ///////")
for i in range(0,10):
    selected10[i].mutate()
    print(selected10[i].chrom, " with fitness ", selected10[i].fitnessValue)

print( "///////   Sorting list of 10 selected chromosomes   ///////")
bubbleSort(selected10)
for i in range(0,10):
    print(selected10[i].chrom, " with fitness ", selected10[i].fitnessValue)