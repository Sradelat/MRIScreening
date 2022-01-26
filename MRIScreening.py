import MyTools
# Decided I needed to add more specific functions to the program


def valid_answer():  # checking to see if answer to question was y or n - otherwise throw error
    while True:  # loop until satisfied
        answer = input().lower()  # not case-sensitive
        if answer == "y" or answer == "n":  # asking for y or n
            break  # satisfied
        else:
            print("Invalid entry. Please enter 'y' or 'n'.")  # if any other input happens they get this error
    return answer

# Don't want to combine valid_answer and check_card because it could force useless input on patient :(


def check_card():  # if the patient has an implant card they can input the info here
    print("Please enter card information if available. If you do not have a card describe the implant: ")
    card_info = input()  # this input will be sent to technologist for further research
    return card_info


def input_name():
    name = input("Enter your first and last name: ")
    name = name.title()  # format name correctly
    return name


def input_dob():
    dob = input("Enter your date of birth (MM/DD/YYYY): ")  # need to catch incorrect format
    return dob


def input_sex():
    while True:
        sex = input("Were you male or female at birth? ").lower()
        if sex == "male" or sex == "female":
            break
        else:
            print("Invalid answer. Please enter male or female.")
        return sex


def metric_system():
    print("Would you like to use the metric system for measurements? (height in cm and weight in kg) [y/n] ")
    metric = valid_answer()
    return metric


def input_height(metric):
    # Metric system
    if metric == "y":
        while True:
            height = input("Enter your height in centimeters: ")
            if height.isdigit():
                break
            else:
                print("Please enter numbers only.")
        return height
    # USCS
    elif metric == "n":
        while True:
            height = input("Enter your height (Example for 5ft 0in: 5'0): ")
            if "'" not in height:
                print("Please format correctly. Try again.")
                continue
            else:
                break
        return height


def input_weight(metric):
    # Metric system
    if metric == "y":
        while True:
            weight = input("Enter your weight in kilograms: ")
            if weight.isdigit():
                break
            else:
                print("Please enter numbers only.")
        return weight
    # USCS
    if metric == "n":
        while True:
            weight = input("Enter your weight in pounds: ")
            if weight.isdigit():
                break
            else:
                print("Please enter numbers only.")
                continue
        return weight


def compile_demographics(name, dob, metric, height, weight):  # could put args in list for brevity
    current_age = MyTools.current_age_calculator(dob)
    while True:
        if metric == "y":  # metric units to USCS units
            # Might be nice to return DOB as Month Day, Year (July 19, 1990) for CLARITY!
            demographics = f"Name: {name}\nAge: {current_age}  DOB: {dob}\nHeight: {height}cm  Weight: {weight}kg"
        else:
            demographics = f"Name: {name}\nAge: {current_age}  DOB: {dob}\nHeight: {height}  Weight: {weight}"
        print(f"{demographics}\nPlease verify that the information above is correct. [y/n] ")
        correct = MRIScreening.valid_answer()
        if correct == "y":
            break
        if correct == "n":
            print("Input the number of the field that is incorrect.\n1. Name\n2. DOB\n3. Height\n4. Weight")
            while True:
                edit_field = input()
                if edit_field.isdigit() and int(edit_field) <= 4:
                    break
                else:
                    print("Error. Please input one number between 1 and 4 corresponding to the field that needs to be "
                          "corrected.")
            if edit_field == "1":
                name = MRIScreening.input_name()
            elif edit_field == "2":
                dob = MRIScreening.input_dob()
            elif edit_field == "3":
                metric = MRIScreening.metric_system()
                height = MRIScreening.input_height(metric)
            else:
                metric = MRIScreening.metric_system()
                weight = MRIScreening.input_height(metric)