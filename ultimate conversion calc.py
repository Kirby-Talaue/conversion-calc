def statement_generator(statement, decor):
    print(f"\n{decor * 5} {statement} {decor * 5} \n")


def instructions():
    statement_generator("Instructions", "-")
    print('''To use this program, simply enter a category of time, distance or mass.
Then enter the amount of more than 0 and what unit to convert from and to convert to.
This program converts the units in certain categories.

The following units are:

- Time: ms, s, min, h, days, years
- Distance: mm, cm, m, km
- Mass: mg, g, kg, t   
    
To exit the program type 'xxx' on the category question.
    ''')


def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = float(response)

            if 0 < response:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def unit_checker(question, valid_units):

    unit_list = list(valid_units.keys())

    while True:

        # ask the user for a unit
        response = input(question)

        if response in valid_units:
            return response

        else:
            print(f"Sorry, the unit is not valid, please choose from {unit_list}")


def string_checker(question, valid_responses):
    error = "Please enter a valid category\n"
    while True:

        response = input(question).lower()

        # Checks response is either in the list or the first letter of a list item
        for item in valid_responses:
            if response == item or response == item[0]:
                return item

        print(error)


# Get amount and units (assume they are valid)
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

time_dict = {
    "ms": 3600000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "days": 0.04166666666,
    "years": 0.00011407711
}

mass_dict = {
    "mg": 1000000,
    "g": 1000,
    "kg": 1,
    "t": 0.001

}

category_list = [
    "distance",
    "time",
    "mass", "xxx"
]

statement_generator("Conversion calculator", "-")
want_instructions = input("Press <enter> to read or any key to continue: ")

if want_instructions == "":
    instructions()

while True:
    # input
    category = string_checker("What category of unit? ", category_list)

    if category == "xxx":
        break

    print(f"Your category is {category}")
    amount = num_check("How much?")
    # if amount == "xxx":
    #     break

    # set up correct dictionary to be used
    if category == "distance":
        # print(distance_print())
        use_dictionary = distance_dict

    elif category == "time":
        # print(time_print())
        use_dictionary = time_dict

    elif category == "mass":
        # print(mass_print())
        use_dictionary = mass_dict

    # get units and check they are in the same domain
    from_unit = unit_checker("From unit? ", use_dictionary)
    to_unit = unit_checker("To unit? ", use_dictionary)

    # do conversion and show user result
    multiply_by = use_dictionary[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = use_dictionary[from_unit]
    answer = standard / divide_by

    print(f"There is {answer:.2f} {to_unit} in {amount} {from_unit} ")


print("Thank you for using the factors calculator")
