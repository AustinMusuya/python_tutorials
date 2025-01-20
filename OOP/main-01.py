from dog import Person, Female, Male


def main():
    # instatiation / object creation
    person1 = Person("John", 25, "Lawyer")

    person2 = Female("Mary", 24, "Doctor")

    # person3 = Male("Bob", 30, "Muscular")

    print(person1)

    person2.speak()
    # person3.speak()


if __name__ == "__main__":
    main()
