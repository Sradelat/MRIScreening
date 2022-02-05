import MyTools


def home(scan_pacemakers=True):
    print("1. Start Questionnaire\n2. Edit Questions\n3. Open Settings\nEnter the number of which command you want.")
    command = input()
    if command == "1":
        print("Starting Questionnaire..")
        # name = input_name()  # SKIPPING TO TEST QUESTIONNAIRE
        # sex = input_sex()
        # dob = input_dob()
        # metric = metric_system()
        # height = input_height(metric)
        # weight = input_weight(metric)
        # check_demographics(name, sex, dob, metric, height, weight)
        questionnaire()
        # questionnaire(scan_pacemakers) # BACK UP
    if command == "2":
        edit_questions()
        home()
    if command == "3":  # not currently implemented
        while True:
            print(f"Which setting would you like to change?\n1. Scan pacemakers = {scan_pacemakers}")  # need labs?
            while True:
                command = input()
                if command == "1":
                    if scan_pacemakers:
                        scan_pacemakers = False
                        break
                    else:
                        scan_pacemakers = True
                        break
                if command == "home":
                    home(scan_pacemakers)


def edit_questions():
    for question in form:
        print(question[0])
    print("\nAbove is a list of questions actively in the screening form. Would you like to:"
          "\n1. Add template question(s)\n2. Remove question(s)\n3. Sort questions")
    answer = input()
    if answer == "1":  # Add template questions
        while True:
            for question in enumerate(graveyard):
                print(question[0], question[1][0])
            add_q = input("\nEnter the number of the question you would like to add: ")
            move_q = graveyard.pop(int(add_q))  # pop indexed question from graveyard
            for question in enumerate(form):
                print(question[0], question[1][0])
            sort_add = input("\nEnter the number of where you would like it to go: ")  # desired index position
            form.insert(int(sort_add), move_q)  # insert desired question into desired index
            for question in enumerate(form):  # enumerate for consistency
                print(question[0], question[1][0])
            done = input("\nUpdated list above. Are you done? [y/n] ")  # loops if not done
            if done == "y":
                break
            if done == "n":
                continue
    if answer == "2":  # remove questions
        while True:
            for question in enumerate(form):  # enumerate gives us index no matter where a question goes
                print(question[0], question[1][0])
            remove_q = input("\nEnter the number of the question you would like to remove: ")  # desired index
            move_q = form.pop(int(remove_q))
            graveyard.append(move_q)  # moved to graveyard for retrieval
            for question in enumerate(form):  # enumerate for consistency
                print(question[0], question[1][0])
            done = input("\nUpdated list above. Are you done? [y/n] ")  # loops if not done
            if done == "y":
                break
            if done == "n":
                continue
    if answer == "3":  # sort questions
        while True:
            for question in enumerate(form):  # enumerate gives us index no matter where a question goes
                print(question[0], question[1][0])
            sort_remove = input("\nEnter the number of the question you would like to move: ")  # remove desired index
            move_q = form.pop(int(sort_remove))
            for question in enumerate(form):  # print form
                print(question[0], question[1][0])
            sort_add = input("\nEnter the number of where you would like it to go: ")  # move to desired index
            form.insert(int(sort_add), move_q)  # insert using desired index and popped question
            for question in enumerate(form):  # enumerate for consistency
                print(question[0], question[1][0])
            done = input("\nUpdated list above. Are you done? [y/n] ")  # loops if not done
            if done == "y":
                break
            if done == "n":
                continue
    # print("DEBUG", questions)
    # print("DEBUG", graveyard)


def valid_answer():  # checking to see if answer to question was y or n - otherwise throw error
    while True:  # loop until satisfied
        answer = input().lower()  # not case-sensitive
        if answer == "y" or answer == "n":  # asking for y or n
            break  # satisfied
        else:
            print("Invalid entry. Please enter 'y' or 'n'.")  # if any other input happens they get this error
    return answer


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


# index format = 0 question - printed text for user
#                1 title - used to add to dict
#                2 card - if "y" asks for card info
#                3 optional - follow-up questions; helps back command be accurate
#                4 input - accepts raw input instead of the default 'y', 'n', or 'back'.


form = [("Is there ANY chance you could be pregnant? [y/n] ", "pregnant", 0, 0, 0),
        ("Do you currently have a pacemaker/defibrillator? [y/n] ", "pacemaker", "card", 0, 0),
        ("Have you ever had a pacemaker/defibrillator? [y/n] ", "past pacemaker", 0, 0, 0),
        ("Do you have abandoned pacemaker wires still in place?", "wires", "card", "opt", 0),
        ("Do you have a brain aneurysm clip? [y/n] ", "clip", "card", 0, 0),
        ("Do you have a nerve or bone growth stimulator? [y/n] ", "stimulator", "card", 0, 0),
        ("Do you have any stents? [y/n] ", "stent", "card", 0, 0),
        ("Do you have any intravascular coils? [y/n] ", "coil", "card", 0, 0),
        ("Do you have any vascular filters? [y/n] ", "filter", "card", 0, 0),
        ("Do you have an artificial heart valve? [y/n] ", "valve", "card", 0, 0),
        ("Do you have a shunt? [y/n] ", "shunt", "card", 0, 0),
        ("Do you have any eye implants? [y/n] ", "eye", "card", 0, 0),
        ("Do you now or have you ever had an injury involving metal to your eye? [y/n] ", "metal in eyes", 0, 0, 0),
        ("Did you have the metal removed from your eye by a doctor? [y/n] ", "metal in eyes removed", 0, "opt", 0),
        ("Have you ever worked as a welder or metal shaver? [y/n] ", "eyes occupation", 0, 0, 0),
        ("Do you have any shrapnel, BB's, or gunshot wounds? [y/n] ", "foreign body", 0, 0, 0),
        ("Do you have any ear implants? [y/n] ", "ear", "card", 0, 0),
        ("Do you wear hearing aids? [y/n] ", "hearing aids", 0, 0, 0),
        ("Do you have an implanted drug pump? [y/n] ", "drug pump", "card", 0, 0),
        ("Do you have an insulin pump? [y/n] ", "insulin pump", "card", 0, 0),
        ("If you have any other metallic implants that were not asked about, please type them in now. "
        "If not, type 'n'. ", "metallic implants", 0, 0, "input"),
        ("Have you ever had MRI contrast before? [y/n] ", "contrast", 0, 0, 0),
        ("Did your body have a negative reaction to the MRI contrast?", "reaction", 0, "opt", 0),
        ("Are you diabetic? [y/n] ", "diabetic", 0, 0, 0),
        ("Do you have a history of high blood pressure? [y/n] ", "blood pressure", 0, 0, 0),
        ("Do you have a history of kidney failure? [y/n] ", "kidneys", 0, 0, 0),
        ("Are you on dialysis? [y/n] ", "dialysis", 0, 0, 0),
        ("Do you have any liver disease? [y/n] ", "liver disease", 0, 0, 0),
        ("Do you have multiple myeloma? [y/n] ", "multiple myeloma", 0, 0, 0)]


graveyard = []  # where unused questions go to die and become undead again
final = {}  # answers stored here
# need to check card on implants


def questionnaire():
    q_count = 0
    # Begin Questionnaire
    print("Read each question carefully and answer with either 'y' or 'n' unless otherwise stated.")
    print("At any time you can enter 'back' to go back to the previous question.")
    while q_count < len(form):  # when Q count hits Q length we stop
        while True:
            answer = input(form[q_count][0])  # questions indexed by question count (starting 0)
            if form[q_count][4] == "input":  # allow raw input answer
                final[form[q_count][1]] = answer  # answer logged
                q_count += 1  # count question after answer logged
                break
            if answer == "back":
                while True:
                    if q_count == 0:  # back command at first question
                        answer = input("Exit without completing? [y/n] ")
                        if answer == "y":
                            quit()
                        if answer == "n":  # ask first questions again
                            break
                    q_count -= 1  # question count - 1 to go back
                    if form[q_count][1] in final:  # remove answer from dict
                        final.pop(form[q_count][1])
                    if form[q_count][1] + " card" in final:     #!!!!!!!!!!!
                        final.pop(form[q_count][1] + " card")   #!!!!!!!!!!!
                    # skips optional questions for a true "back" function instead of hitting question previously skipped
                    skips = 0  # number of questions to skip going backwards
                    copy_count = q_count  # copy so the variable doesn't change and have to fix it later
                    while form[copy_count][3] == "opt":
                        copy_count -= 1  # if True back up and check again
                        skips += 1  # if True skip optional question
                    # if main question is "n" we execute the optional questions skip
                    if final[form[q_count - skips][1]] == "n":
                        q_count -= skips  # execute optional questions skip
                    answer = input(form[q_count][0])
                    if answer != "back":  # if answer is valid push forward
                        final[form[q_count][1]] = answer  # log the answer in a dictionary by tuple[1]
                        q_count += 1  # count question after answer logged
                        break
            elif answer == "y":
                final[form[q_count][1]] = answer  # log the answer in a dictionary by tuple[1] (tag)
                if form[q_count][2] == "card":                             #!!!!!!!!!!!!
                    final[form[q_count][1] + " card"] = check_card()  #!!!!!!!!!!!!
                q_count += 1  # count question after answer logged
                break
            elif answer == "n":
                final[form[q_count][1]] = answer  # log the answer in a dictionary by tuple[1] (tag)
                q_count += 1  # count question after answer logged
                while form[q_count][3] == "opt":  # skips over optional follow-up questions
                    q_count += 1
                break
            else:
                print("Invalid entry. Please enter 'y', 'n', or 'back'.")
                continue
        if form[q_count] == form[-1]:
            break  # end questionnaire
    print("DONE!")
    print(final)  # END HERE 1














# BACK UP
# completed_form = {}
# questions = []
#
#
# def questionnaire(scan_pacemakers):  # can check in between questions for a custom question?
#     print("Is there ANY chance you could be pregnant? [y/n] ")
#     completed_form["pregnant"] = valid_answer()
#
#     print("Do you currently have a pacemaker/defibrillator? [y/n] ")
#     completed_form["pacemaker"] = valid_answer()
#     if completed_form["pacemaker"] == "y":
#         if scan_pacemakers:
#             completed_form["pacemaker info"] = check_card()
#         if not scan_pacemakers:
#             input("We can not scan pacemakers at this location. Please inform staff. Press enter to exit.")
#             quit()
#
#     print("Have you ever had a pacemaker/defibrillator removed? [y/n] ")
#     completed_form["past pacemaker"] = valid_answer()
#     if completed_form["past pacemaker"] == "y":
#         print("Do you have abandoned pacemaker wires still in place?")
#         completed_form["wires"] = valid_answer()
#         if completed_form["wires"] == "y":
#             completed_form["wires info"] = check_card()
#
#     print("Do you have a brain aneurysm clip? [y/n] ")
#     completed_form["clip"] = valid_answer()
#     if completed_form["clip"] == "y":
#         completed_form["clip info"] = check_card()
#
#     print("Do you have a nerve or bone growth stimulator? [y/n] ")
#     completed_form["stimulator"] = valid_answer()
#     if completed_form["stimulator"] == "y":
#         completed_form["stimulator info"] = check_card()
#
#     print("Do you have any stents? [y/n] ")
#     completed_form["stents"] = valid_answer()
#     if completed_form["stents"] == "y":
#         completed_form["stents info"] = check_card()
#
#     print("Do you have any intravascular coils? [y/n] ")
#     completed_form["coils"] = valid_answer()
#     if completed_form["coils"] == "y":
#         completed_form["coils info"] = check_card()
#
#     print("Do you have any vascular filters? [y/n] ")
#     completed_form["filters"] = valid_answer()
#     if completed_form["filters"] == "y":
#         completed_form["filters info"] = check_card()
#
#     print("Do you have an artificial heart valve? [y/n] ")
#     completed_form["valves"] = valid_answer()
#     if completed_form["valves"] == "y":
#         completed_form["valves info"] = check_card()
#
#     print("Do you have a shunt? [y/n] ")
#     completed_form["shunt"] = valid_answer()
#     if completed_form["shunt"] == "y":
#         completed_form["shunt info"] = check_card()
#
#     print("Do you have any eye implants? [y/n] ")
#     completed_form["eyes"] = valid_answer()
#     if completed_form["eyes"] == "y":
#         completed_form["eyes info"] = check_card()
#
#     print("Have you ever worked as a welder or metal shaver? [y/n] ")
#     completed_form["eyes occupation"] = valid_answer()
#
#     print("Do you now or have you ever had an injury involving metal to your eye? [y/n] ")
#     completed_form["metal in eyes"] = valid_answer()
#     if completed_form["metal in eyes"] == "y":
#         print("Did you have the metal removed from your eye by a doctor? [y/n] ")
#         completed_form["metal in eyes removed"] = valid_answer()
#
#     print("Do you have any shrapnel, BB's, or gunshot wounds? [y/n] ")
#     completed_form["foreign_body"] = valid_answer()
#
#     print("Do you have any ear implants? [y/n] ")
#     completed_form["ears"] = valid_answer()
#     if completed_form["ears"] == "y":
#         completed_form["ears info"] = check_card()
#
#     print("Do you wear hearing aids? [y/n] ")
#     completed_form["hearing aids"] = valid_answer()
#     if completed_form["hearing aids"] == "y":
#         print("Your hearing aids will need to be removed for your MRI.")
#
#     print("Do you have an implanted drug pump? [y/n] ")
#     completed_form["drug pump"] = valid_answer()
#     if completed_form["drug pump"] == "y":
#         completed_form["drug pump info"] = check_card()
#
#     print("Do you have an insulin pump? [y/n] ")
#     completed_form["insulin pump"] = valid_answer()
#     if completed_form["insulin pump"] == "y":
#         print("Your insulin pump will need to be removed for your MRI. Please plan accordingly.")
#
#     print("Any other metallic implants in your body? [y/n] ")
#     completed_form["metallic implants"] = valid_answer()
#     if completed_form["metallic implants"] == "y":
#         print("Please type in any metallic implants in your body that we have not asked about: ")
#         completed_form["metallic implants info"] = input()
#
#     print("Have you ever had MRI contrast before? [y/n] ")  # have you had a reaction?
#     completed_form["contrast"] = valid_answer()
#     if completed_form["contrast"] == "y":
#         print("Did your body have a negative reaction to the MRI contrast?")
#         completed_form["reaction"] = valid_answer()
#
#     print("Are you diabetic? [y/n] ")
#     completed_form["diabetic"] = valid_answer()
#
#     print("Do you have a history of high blood pressure? [y/n] ")
#     completed_form["blood_pressure"] = valid_answer()
#
#     print("Do you have a history of kidney failure? [y/n] ")
#     completed_form["kidneys"] = valid_answer()
#
#     print("Are you on dialysis? [y/n] ")
#     completed_form["dialysis"] = valid_answer()
#
#     print("Do you have any liver disease? [y/n] ")
#     completed_form["liver_disease"] = valid_answer()
#
#     print("Do you have multiple myeloma? [y/n] ")
#     completed_form["multiple_myeloma"] = valid_answer()
#
#
# def get_flagged_answers():
#     for k, v in completed_form.items():
#         if v == "y":
#             print(k, v)
#             continue
#         if v == "n":
#             continue
#         if "info" in k:
#             print(k, v)
#         else:
#             continue
