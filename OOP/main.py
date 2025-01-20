from praco import Car, Subaru


def main():
    new_car = Car("Volvo", "Used", '2019')

    car_details = new_car.get_descriptive_name()

    new_car.update_odometer(10)

    new_car.increment_odometer(15)

    new_car.read_odometer()

    print(car_details)

    sub_car = Subaru('Forester', 'New', "2021")

    sub_details = sub_car.get_descriptive_name()

    sub_car.update_odometer(5)

    sub_car.increment_odometer(15)

    print(sub_details)

    sub_car.read_odometer()


if __name__ == "__main__":
    main()
