from datetime import date


def current_age_calculator(dob):
    dob_month = int(dob.split("/")[0])
    dob_day = int(dob.split("/")[1])
    dob_year = int(dob.split("/")[2])
    current_date = str(date.today())  # pull current date and convert to str
    current_month = int(current_date.split("-")[1])
    current_day = int(current_date.split("-")[2])
    current_year = int(current_date.split("-")[0])
    if (dob_month + dob_day) > (current_month + current_day):
        current_age = current_year - dob_year - 1
    else:
        current_age = current_year - dob_year
    return current_age


def appt_age_calculator(appt, dob):
    dob_month = int(dob.split("/")[0])
    dob_day = int(dob.split("/")[1])
    dob_year = int(dob.split("/")[2])
    appt_month = int(appt.split("/")[0])
    appt_day = int(appt.split("/")[1])
    appt_year = int(appt.split("/")[2])
    if (dob_month + dob_day) > (appt_month + appt_day):
        appt_age = appt_year - dob_year - 1
    else:
        appt_age = appt_year - dob_year
    return appt_age


def metric_uscs_height(height):
    uscs_feet = int((int(height) * .393701) / 12)  # dropping the remainder with int
    uscs_inches = round((int(height) * .393701) % 12)  # rounding the remainder
    str_uscs_height = f"{uscs_feet}'{uscs_inches}"
    return str_uscs_height


def metric_uscs_weight(weight):
    uscs_weight = round(int(weight) * 2.2)  # round the decimal off
    str_uscs_weight = f"{uscs_weight}lbs"
    return str_uscs_weight
