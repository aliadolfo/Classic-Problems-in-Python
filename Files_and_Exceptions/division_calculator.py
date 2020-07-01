def division_error():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")

def division_calculator():
    print("Give me two numbers, and I'll divide them")
    print("enter 'q' to quit ")

    while True:
        first_number = input("\n First number: ")
        if first_number == 'q':
            break
        second_number = input("\n Second number: ")
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            raise "You can divide by zero"
        else:
            print(answer)

if '__main__'==__name__:
    print("#Devision error >>> ")
    print(division_error())
    print("---------------")
    print(division_calculator())
