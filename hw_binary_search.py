import random

numbers = [random.randint(1, 50) for i in range(100)]
numbers.sort()
print(numbers)

key = int(input("Enter the value you are looking for "))


def binary_search(low, high):
    while low <= high:
        mid = (high + low) // 2
        if numbers[mid] == key:
            return mid
        elif numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
    return -1


print(binary_search(0, len(numbers) - 1))
