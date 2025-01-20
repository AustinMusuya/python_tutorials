"""
Exercise 1: Local vs Global Scope Instruction:

Define a variable with the same name in both global and local scopes within a function.
Print the variable from inside the function and outside the function, 
observing how Python accesses each variable based on its scope (local vs global).

"""

numbers = [5, 4, 8, 9, 7, 5]


def work():
    # global numbers
    numbers = [5, 4, 8, 9]

    def play():
        global numbers
        numbers = 'numbers'
        print(numbers)
    play()
    print(numbers)


work()
print(numbers)
