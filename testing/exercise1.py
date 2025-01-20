def calculate_square(number):
    try:
        return number * number
    except TypeError as e:
        # return None
        print(e)
