import random

numbers = [random.randint(1,20) for i in range (10)]
print(numbers)
list = numbers

def selection_sort():
    n = len(numbers)
    count = 0 
    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if numbers[j] < numbers[min_index]:
                numbers[j],numbers[min_index] = numbers[min_index],numbers[j]
                count = count + 1

            print(numbers)
    print(count)

selection_sort()

import random

numbers = [random.randint(1,20) for i in range (10)]
print(numbers)

def selection_sort():
    n = len(numbers)
    count = 0 
    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if numbers[j] < numbers[min_index]:
                min_index = j
                count = count + 1
        numbers[i],numbers[min_index] = numbers[min_index],numbers[i]
        print(numbers)
    print(count)

selection_sort()
