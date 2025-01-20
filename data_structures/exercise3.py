"""
Exercise 3: Write a program to generate a random set of numbers between 1 and ten. 
Use set operations to remove duplicates and display the unique numbers.

"""
import random


def generate_set(set_size):
    numbers = []
    while len(numbers) < set_size:
        random_number = random.randint(1,10)
        numbers.append(random_number)

    return numbers


def remove_duplicates(array):
    new_numbers = []

    right = len(array) - 1

    left = 0

    while right > left:
        if array[left] not in new_numbers:      
            new_numbers.append(array[left])
        if array[right] not in new_numbers:
            new_numbers.append(array[right])            
        right -= 1
        left += 1


    new_numbers = set(new_numbers)

    print(f"Unique Numbers are {new_numbers}")


numbers = generate_set(6)

print(numbers)
remove_duplicates(numbers)

