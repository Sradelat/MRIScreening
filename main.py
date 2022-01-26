from datetime import date
import MyTools

# If Q = yes - prompt technologist with each instance
# If no go - prompt staff
# Dictionary to pull specifics? -> can't use input fx in dict
# age can determine if minor or not
# ask for phone number for tech to reach or pull it from their file?
# create schedule file next?

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
    while True:  # might use valid_answer fx to simplify these loops
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

# SETTINGS - need a hub to customize settings such as this
scan_pacemakers = True

# QUESTIONS - not sure if questions should be added to a list to iterate through. I want questions to be customizable.
# Perhaps add a clause at the end for custom questions the admin user wants to add in
print("Is there ANY chance you could be pregnant? [y/n] ")
pregnant = MyTools.valid_answer()

print("Do you currently have a pacemaker/defibrillator? [y/n] ")
pacemaker = MyTools.valid_answer()
if pacemaker == "y":
    if scan_pacemakers:
        pacemaker_info = MyTools.check_card()
    if not scan_pacemakers:
        input("We can not scan pacemakers at this location. Please inform staff. Press enter to exit.")
        quit()

print("Have you ever had a pacemaker/defibrillator? [y/n] ")
past_pacemaker = MyTools.valid_answer()
if past_pacemaker == "y":
    wires = input("Do you have abandoned pacemaker wires still in place?")
    if wires == "y":
        wires_info = MyTools.check_card()

print("Do you have a brain aneurysm clip? [y/n] ")
clip = MyTools.valid_answer()
if clip == "y":
    clip_info = MyTools.check_card()

print("Do you have a nerve or bone growth stimulator? [y/n] ")
stimulator = MyTools.valid_answer()
if stimulator == "y":
    stimulator_info = MyTools.check_card()

print("Do you have any stents? [y/n] ")
stents = MyTools.valid_answer()
if stents == "y":
    stents_info = MyTools.check_card()

print("Do you have any intravascular coils? [y/n] ")
coils = MyTools.valid_answer()
if coils == "y":
    coils_info = MyTools.check_card()

print("Do you have any vascular filters? [y/n] ")
filters = MyTools.valid_answer()
if filters == "y":
    filters_info = MyTools.check_card()

print("Do you have an artificial heart valve? [y/n] ")
valves = MyTools.valid_answer()
if valves == "y":
    valves_info = MyTools.check_card()

print("Do you have a shunt? [y/n] ")
shunt = MyTools.valid_answer()
if shunt == "y":
    shunt_info = MyTools.check_card()

print("Do you have any eye implants? [y/n] ")
eyes = MyTools.valid_answer()
if eyes == "y":
    eyes_info = MyTools.check_card()

print("Have you ever worked as a welder or metal shaver? [y/n] ")
eyes_occupation = MyTools.valid_answer()

print("Do you now or have you ever had an injury involving metal to your eye? [y/n] ")
metal_in_eyes = MyTools.valid_answer()
if metal_in_eyes == "y":
    print("Did you have the metal removed from your eye by a doctor? [y/n] ")
    metal_in_eyes_removed = MyTools.valid_answer()

print("Do you have any shrapnel, BB's, or gunshot wounds? [y/n] ")
foreign_body = MyTools.valid_answer()

print("Do you have any ear implants? [y/n] ")
ears = MyTools.valid_answer()
if ears == "y":
    ears_info = MyTools.check_card()

print("Do you wear hearing aids? [y/n] ")
hearing_aids = MyTools.valid_answer()
if hearing_aids == "y":
    print("Your hearing aids will need to be removed for your MRI.")

print("Do you have an implanted drug pump? [y/n] ")
drug_pump = MyTools.valid_answer()
if drug_pump == "y":
    drug_pump_info = MyTools.check_card()

print("Do you have an insulin pump? [y/n] ")
insulin_pump = MyTools.valid_answer()
if insulin_pump == "y":
    print("Your insulin pump will need to be removed for your MRI. Please plan accordingly.")

print("Any other metallic implants in your body? [y/n] ")
metallic_implants = MyTools.valid_answer()
if metallic_implants == "y":
    print("Please type in any metallic implants in your body that we have not asked about: ")
    metallic_implants_info = input(">")

# Is exam with contrast?
print("Have you ever had MRI contrast before? [y/n] ")  # have you had a reaction?
contrast = MyTools.valid_answer()
if contrast == "y":
    print("Did your body have a negative reaction to the MRI contrast?")
    reaction = MyTools.valid_answer()

print("Are you diabetic? [y/n] ")
diabetic = MyTools.valid_answer()

print("Do you have a history of high blood pressure? [y/n] ")
blood_pressure = MyTools.valid_answer()

print("Do you have a history of kidney failure? [y/n] ")
kidneys = MyTools.valid_answer()

print("Are you on dialysis? [y/n] ")
dialysis = MyTools.valid_answer()

print("Do you have any liver disease? [y/n] ")
liver_disease = MyTools.valid_answer()

print("Do you have multiple myeloma? [y/n] ")
multiple_myeloma = MyTools.valid_answer()






# # COPY
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