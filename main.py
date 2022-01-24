from datetime import date
import MyTools

# If Q = yes - prompt technologist with each instance
# If no go - prompt staff
# Dictionary to pull specifics?
# age can determine if minor or not
# make pt confirm demographics are correct
# ask for phone number for tech to reach or pull it from their file?

appt = "07/20/2022"  # going to pull from file
while True:
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (MM/DD/YYYY): ")  # need to check correct format
    # SEX
    while True:
        sex = input("Were you male or female at birth? ").lower()
        if sex == "male" or sex == "female":
            break
        else:
            print("Invalid answer. Please enter male or female.")
    # HEIGHT WEIGHT
    while True:
        m_units = input("Would you like to use the metric system for measurements? (height in cm and weight in kg) "
                        "[y/n] ")
        # Metric system
        if m_units == "y":
            while True:
                height = input("Enter your height in centimeters: ")
                if height.isdigit():
                    break
                else:
                    print("Please enter numbers only.")
            while True:
                weight = input("Enter your weight in kilograms: ")
                if weight.isdigit():
                    break
                else:
                    print("Please enter numbers only.")
        # USCS
        elif m_units == "n":
            while True:
                height = input("Enter your height (Example for 5ft 0in: 5'0): ")
                if "'" not in height:
                    print("Please format correctly. Try again.")
                    continue
                else:
                    break
            while True:
                weight = input("Enter your weight in pounds: ")
                if weight.isdigit():
                    break
                else:
                    print("Please enter numbers only.")
                    continue
            break
        else:
            print("Invalid command.")

    # VERIFY DEMOGRAPHICS

    # FORMAT NAME
    name = name.title()

    # CURRENT AGE
    current_age = MyTools.current_age_calculator(dob)  # convert to Month Day, Year format?

    # APPT AGE
    appt_age = MyTools.appt_age_calculator(appt, dob)

    # METRIC HEIGHT AND WEIGHT CONVERTER
    if m_units == "y":  # metric units to USCS units
        height = MyTools.metric_uscs_height(height)
        weight = MyTools.metric_uscs_weight(weight)
        demographics = f"Name: {name}\nAge: {current_age}\nHeight: {height} Weight: {weight}"
    else:
        demographics = f"Name: {name}\nAge: {current_age}\nHeight: {height}  Weight: {weight}"
    print(f"Please verify that this information is correct:\n{demographics}")
    correct = input("[y/n]")
    if correct == "y":
        break
    else:
        continue

# pregnant = input("Is there ANY chance you could be pregnant? [y/n] ")
# pacemaker = input("Do you currently have a pacemaker/defibrillator? [y/n] ")
# past_pacemaker = input("Have you ever had a pacemaker/defibrillator? [y/n] ")
# clip = input("Do you have a brain aneurysm clip? [y/n] ")
# stimulator = input("Do you have a nerve or bone growth stimulator? [y/n] ")
# stents = input("Do you have any stents? [y/n] ")
# coils = input("Do you have any intravascular coils? [y/n] ")
# filters = input("Do you have any vascular filters? [y/n] ")
# valves = input("Do you have an artificial heart valve? [y/n] ")
# shunt = input("Do you have a shunt? [y/n] ")
# eyes = input("Do you have any eye implants? [y/n] ")
# metal_in_eyes = input("Do you now or have you ever had an injury involving metal to your eye? [y/n] ")
# eyes_occupation = input("Have you ever worked as a welder or metal shaver? [y/n] ")
# foreign_body = input("Do you have any shrapnel, BB's, or gunshot wounds? [y/n] ")
# ears = input("Do you have any ear implants? [y/n] ")
# hearing_aids = input("Do you wear hearing aids? [y/n] ")
# drug_pump = input("Do you have an implanted drug pump? [y/n] ")
# insulin_pump = input("Do you have an insulin pump? [y/n] ")
# metallic_implants = input("Any other metallic implants in your body? [y/n] ")
# # Is exam with contrast?
# contrast = input("Have you ever had MRI contrast before? [y/n] ")  # have you had a reaction?
# diabetic = input("Are you diabetic? [y/n] ")
# blood_pressure = input("Do you have a history of high blood pressure? [y/n] ")
# kidneys = input("Do you have a history of kidney failure? [y/n] ")
# dialysis = input("Are you on dialysis? [y/n] ")
# liver_disease = input("Do you have any liver disease? [y/n] ")
# multiple_myeloma = input("Do you have multiple myeloma? [y/n] ")

