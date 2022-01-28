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
    while True:
        name = input("Enter your first and last name: ")
        if " " not in name:  # checking for last name
            print("ERROR. Did not detect last name.")
        else:
            break
    name = name.title()  # format name correctly
    return name


def input_dob():
    while True:
        dob = input("Enter your date of birth (MM/DD/YYYY): ")
        try:
            dob_month = dob.split("/")[0]  # splitting and defining each element for format check
            dob_day = dob.split("/")[1]
            dob_year = dob.split("/")[2]
            if any([int(dob_month) > 12, len(dob_month) != 2,  # date format check
                    int(dob_day) > 31, len(dob_day) != 2,
                    int(dob_year) < 1900, len(dob_year) != 4]):
                print("ERROR. Incorrect format. Try again.")
            else:
                break
        except (ValueError, IndexError):  # practice not using bare except - using two exceptions now - LEVEL UP!
            print("ERROR. Incorrect format.")  # if not number and if / not used
    return dob


def input_sex():
    while True:
        sex = input("Were you male or female at birth? ").lower()
        if sex == "male" or sex == "female":
            break
        else:
            print("INVALID ANSWER. Please enter male or female.")
    return sex.title()


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
                print("Please enter numbers with no decimals only.")
        return weight
    # USCS
    if metric == "n":
        while True:
            weight = input("Enter your weight in pounds: ")
            if weight.isdigit():
                break
            else:
                print("Please enter numbers with no decimals only.")
                continue
        return weight


def compile_demographics(name, sex, dob, metric, height, weight):  # could put args in list for brevity
    current_age = MyTools.current_age_calculator(dob)  # calculate current age for display
    month_conversions = {  # for formatting
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    dob_month = dob.split("/")[0]  # splitting and defining each element for reformatting
    dob_day = dob.split("/")[1]
    dob_year = dob.split("/")[2]
    while True:
        if metric == "y":  # metric units to USCS units, also changed DOB format for clarity
            demographics = f"Name: {name}\n" \
                           f"Sex: {sex}\n" \
                           f"DOB: {month_conversions[dob_month]} {dob_day}, {dob_year}  " \
                           f"Age: {current_age}\n" \
                           f"Height: {height}cm  Weight: {weight}kg"
            return demographics
        else:  # changed DOB format for clarity
            demographics = f"Name: {name}\n" \
                           f"Sex: {sex}\n" \
                           f"DOB: {month_conversions[dob_month]} {dob_day}, {dob_year}  " \
                           f"Age: {current_age}\n" \
                           f"Height: {height}  Weight: {weight}lbs"
            return demographics


def check_demographics(name, sex, dob, metric, height, weight):  # getting the demographics right is very important
    while True:
        demographics = compile_demographics(name, sex, dob, metric, height, weight)
        print(f"{demographics}\nPlease verify that the information above is correct. [y/n] ")  # if n can edit
        correct = valid_answer()
        if correct == "y":
            return demographics
        if correct == "n":  # May separate into another fx? edit_demographics
            print("Input the number of the field that is incorrect.\n1. Name\n2. Sex\n3. DOB\n4. Height\n5. Weight")
            while True:
                edit_field = input()
                if edit_field.isdigit() and int(edit_field) <= 5:
                    break  # if correct input continue
                else:
                    print("Error. Please input one number between 1 and 5 corresponding to the field that needs to be "
                          "corrected.")  # catch incorrect input
            if edit_field == "1":  # each field can be edited separately to avoid redundant input by user
                name = input_name()
            elif edit_field == "2":
                sex = input_sex()
            elif edit_field == "3":
                dob = input_dob()
            elif edit_field == "4":
                metric = metric_system()  # ask again in case input was incorrect
                height = input_height(metric)
            else:
                metric = metric_system()  # ask again in case input was incorrect
                weight = input_weight(metric)


