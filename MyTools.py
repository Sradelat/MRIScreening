from datetime import date


def current_age_calculator(dob):  # uses datetime for real time age calculation
    dob_month = int(dob.split("/")[0])  # splitting days months years correctly for calculation below
    dob_day = int(dob.split("/")[1])
    dob_year = int(dob.split("/")[2])
    current_date = str(date.today())  # pull current date and convert to str
    current_month = int(current_date.split("-")[1])
    current_day = int(current_date.split("-")[2])
    current_year = int(current_date.split("-")[0])
    if (dob_month + dob_day) > (current_month + current_day):  # checks to see if birthday has happened yet this year
        current_age = current_year - dob_year - 1  # if birthday hasn't happened then subtract a year
    else:
        current_age = current_year - dob_year  # if birthday happened this year
    return current_age


def appt_age_calculator(appt, dob):  # Calculates patient's age at appointment date to see if patient needs labs
    dob_month = int(dob.split("/")[0])  # splitting days months years correctly for calculation below
    dob_day = int(dob.split("/")[1])
    dob_year = int(dob.split("/")[2])
    appt_month = int(appt.split("/")[0])
    appt_day = int(appt.split("/")[1])
    appt_year = int(appt.split("/")[2])
    if (dob_month + dob_day) > (appt_month + appt_day):  # checks to see if birthday has happened yet this year
        appt_age = appt_year - dob_year - 1  # if birthday hasn't happened then subtract a year
    else:
        appt_age = appt_year - dob_year  # if birthday happened this year
    return appt_age


def metric_uscs_height(height):  # Converts Metric cm to USCS ft/in
    uscs_feet = int((int(height) * .393701) / 12)  # dropping the remainder with int
    uscs_inches = round((int(height) * .393701) % 12)  # rounding the remainder
    str_uscs_height = f"{uscs_feet}'{uscs_inches}"  # makes it pretty
    return str_uscs_height


def metric_uscs_weight(weight):  # Converts Metric KG to USCS lbs
    uscs_weight = round(int(weight) * 2.2)  # round the decimal off
    str_uscs_weight = f"{uscs_weight}lbs"  # makes it pretty
    return str_uscs_weight


def valid_answer():  # checking to see if answer to question was y or n - otherwise throw error
    while True:  # loop until satisfied
        answer = input(">").lower()  # not case-sensitive
        if answer == "y" or answer == "n":  # asking for y or n
            break  # satisfied
        else:
            print("Invalid entry. Please enter 'y' or 'n'.")  # if any other input happens they get this error
    return answer

# Don't want to combine valid_answer and check_card because it could force useless input on patient :(


def check_card():  # if the patient has an implant card they can input the info here
    print("Please enter card information if available. If you do not have a card describe the implant: ")
    card_info = input(">")  # this input will be sent to technologist for further research
    return card_info
