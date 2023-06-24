def check_driver_age():
    age = int(input("Enter driver age: "))
    if age >= 18:
        print("You are eligible")
    else:
        print("Not eligible")


def check_age(age):
    print("You are eligible") if age >= 18 else print("Not eligible")
