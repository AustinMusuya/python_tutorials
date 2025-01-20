from customError import ValueTooHighError

while True:
    try:
        number = int(input("Enter a number: "))
        if number > 10:
            raise ValueTooHighError(number)
        else:
            print(f"Congratulations! {number} is good to go!")
            break
    except ValueTooHighError as e:
        print(e)
    except ValueError:
        print("I guess you need a number for this. Try Again?")
