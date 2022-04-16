import MyTools
import collections
import re


def home(scan_pacemakers=True, weight_limit=0):
    print("WELCOME TO MRI SCREENING!")
    print("1. Start Questionnaire\n2. Edit Questions\n3. Settings\nEnter the number of which command you want.")
    while True:
        command = input()
        if command == "1":
            print("Starting Questionnaire..")
            name = input_name()  # begin with demographic compilation
            sex = input_sex()
            dob = input_dob()
            metric = metric_system()
            height = input_height(metric)
            weight = input_weight(metric)
            d = check_demographics(name, sex, dob, metric, height, weight)  # using named tuples
            if weight_limit > 0 and int(d.weight) > int(weight_limit):  # check weight limit before continuing
                input("The weight you entered exceeds the weight limit of our MRI scanner. Please notify staff. Press "
                      "enter to exit.")
                quit()
            # LINE BELOW FOR TESTING - TO SKIP DEMOGRAPHIC INPUTS
            # demographics(fname='John', lname='Doe', sex='Male', dob='07/27/1957', height="5'9", weight='135')
            questionnaire(scan_pacemakers)  # begin screening form
            get_flagged_answers()  # populate flagged answers list
            write_form(d)  # write to file
            return
        if command == "2":
            edit_questions()
            return
        if command == "3":
            while True:
                print(f"Which setting would you like to change?\n"
                      f"1. Scan pacemakers = {scan_pacemakers}\n"  # facility may not scan pacemakers
                      f"2. Weight limit = {weight_limit}\n"  # used to enter scanner weight limit
                      f"3. Return to home screen")
                while True:
                    command = input()
                    if command == "1":
                        if scan_pacemakers:  # if True, facility can scan pacemakers
                            scan_pacemakers = False
                            break
                        else:
                            scan_pacemakers = True
                            break
                    elif command == "2":  # Might be useful to catch weight limits before a patient hits the schedule
                        while True:
                            weight_limit = input("Please enter your scanner's weight limit in pounds. If you enter 0, "
                                                 "the patient will not receive a prompt about weight limits.\n")
                            try:
                                home(scan_pacemakers, int(weight_limit))
                                break
                            except ValueError:
                                print("Please enter a number without a decimal.")
                    elif command == "3":
                        home(scan_pacemakers, weight_limit)
                        return
                    else:
                        print(num_error())
        else:
            print(num_error())


def num_error():  # if a value was entered outside range of valid commands
    return "Invalid command. Enter a valid number in range."


def edit_questions():
    for question in form:  # show active questions
        print(question[0])
    print("\nAbove is a list of questions actively in the screening form. Would you like to:"
          "\n1. Add template question(s)\n2. Remove question(s)\n3. Sort questions\n4. Add custom question(s)\n"
          "5. Go back to home screen")
    while True:
        answer = input()
        if answer == "1":  # Add template questions
            if len(graveyard) == 0:
                input("There are no questions left in storage to add. Press enter to return to menu.")
                edit_questions()
                return
            else:
                while True:
                    for question in enumerate(graveyard):  # visual aid for user
                        print(question[0], question[1][0])
                    print("\nEnter the number of the question you would like to add: ")
                    while True:
                        add_q = input()
                        try:
                            move_q = graveyard.pop(int(add_q))  # pop indexed question from graveyard
                            break
                        except (ValueError, IndexError):  # catch invalids
                            print(num_error())
                    for question in enumerate(form):  # visual aid for user
                        print(question[0], question[1][0])
                    print(len(form))  # visual aid to add to end of form
                    print("\nEnter the number of where you would like it to go: ")
                    while True:
                        sort_add = input()  # desired index
                        try:
                            form.insert(int(sort_add), move_q)  # pop indexed question from graveyard
                            break
                        except (ValueError, IndexError):
                            print(num_error())
                    for question in enumerate(form):  # enumerate for consistency
                        print(question[0], question[1][0])
                    print("\nUpdated list above. Are you done? [y/n] ")
                    while True:
                        done = valid_answer()  # loops if not done
                        if done == "y":
                            edit_questions()
                            return
                        elif done == "n":
                            break
        elif answer == "2":  # remove questions
            while True:
                for question in enumerate(form):  # enumerate gives us index no matter where a question goes
                    print(question[0], question[1][0])  # visual aid for user
                print("\nEnter the number of the question you would like to remove: ")
                while True:
                    remove_q = input()  # desired index
                    try:
                        move_q = form.pop(int(remove_q))
                        graveyard.append(move_q)  # moved to graveyard for retrieval
                        break
                    except (ValueError, IndexError):
                        print(num_error())
                for question in enumerate(form):  # enumerate for consistency
                    print(question[0], question[1][0])
                print("\nUpdated list above. Are you done? [y/n] ")
                while True:
                    done = valid_answer()  # loops if not done
                    if done == "y":
                        edit_questions()
                        return
                    elif done == "n":
                        break
        elif answer == "3":  # sort questions
            while True:
                for question in enumerate(form):  # enumerate gives us index no matter where a question goes
                    print(question[0], question[1][0])
                    print("\nEnter the number of the question you would like to move: ")
                while True:
                    sort_remove = input()  # remove index
                    try:
                        move_q = form.pop(int(sort_remove))
                        break
                    except (ValueError, IndexError):
                        print(num_error())
                for question in enumerate(form):  # print form
                    print(question[0], question[1][0])
                print(len(form))  # provides visual aid for adding on to the end of the form
                print("\nEnter the number of where you would like it to go: ")
                while True:
                    sort_add = input()  # move to desired index
                    try:
                        form.insert(int(sort_add), move_q)  # insert using desired index and popped question
                        break
                    except (ValueError, IndexError):
                        print(num_error())
                for question in enumerate(form):  # enumerate for consistency
                    print(question[0], question[1][0])
                print("\nUpdated list above. Are you done? [y/n] ")
                done = valid_answer()  # loops if not done
                if done == "y":
                    edit_questions()
                    return
                if done == "n":
                    continue
        elif answer == "4":
            custom_question = input("Please enter the question you would like to be asked:\n")
            while True:
                input_type = input("Is it a..\n1. Yes or no question\n2. Raw input question\n")
                if input_type == "1":
                    inp = 0
                    while True:
                        answer = input("Which answer will flag the question?\n1. Yes\n2. No\n3. No flag needed\n")
                        if answer == "1":
                            flag = "y"
                            break
                        elif answer == "2":
                            flag = "n"
                            break
                        elif answer == "3":
                            flag = "NA"
                            break
                        else:
                            print(num_error())
                    break
                elif input_type == "2":
                    flag = "raw"
                    inp = "input"
                    break
                else:
                    print(num_error())
            while True:
                answer = input("Does the question need.. \n1. An implant card follow-up question?\n2. A reminder to "
                               "remove a metallic object (i.e. hearing aids)\n3. Neither")
                if answer == "1":
                    react = "card"
                    break
                elif answer == "2":
                    react = input("Please enter the object that will need to be removed: ").lower()
                    break
                elif answer == "3":
                    react = 0
                    break
                else:
                    print(num_error())
            for question in enumerate(form):  # print form
                print(question[0], question[1][0])
            custom_add = input("\nEnter the number of where you would like it to go: ")  # move to desired index
            form.insert(int(custom_add), [custom_question, flag, react, inp])
        elif answer == "5":
            home()
            return
        else:
            print(num_error())


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
            if any([int(dob_month) > 12, len(dob_month) != 2,  # date format/value check
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
        if sex == "male" or sex == "female":  # correct answers
            break
        else:  # incorrect answers
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
            if height.isdigit():  # catch non digits
                break
            else:
                print("Please enter numbers only.")
        return height
    # USCS
    elif metric == "n":
        while True:
            height = input("Enter your height (Example for 5ft 0in: 5'0): ")
            if "'" not in height:  # check correct format
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
            if weight.isdigit():  # catch non digits
                break
            else:
                print("Please enter numbers with no decimals only.")
        return weight
    # USCS
    if metric == "n":
        while True:
            weight = input("Enter your weight in pounds: ")
            if weight.isdigit():  # catch non digits
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
            demographics = f"\nFirst Name: {name.split()[0]} \nLast Name: {name.split()[1]}\n" \
                           f"Sex: {sex}\n" \
                           f"DOB: {month_conversions[dob_month]} {dob_day}, {dob_year}  " \
                           f"Age: {current_age}\n" \
                           f"Height: {height}cm  Weight: {weight}kg"
            return demographics
        else:  # changed DOB format for clarity
            demographics = f"\nFirst Name: {name.split()[0]} \nLast Name: {name.split()[1]}\n" \
                           f"Sex: {sex}\n" \
                           f"DOB: {month_conversions[dob_month]} {dob_day}, {dob_year}  " \
                           f"Age: {current_age}\n" \
                           f"Height: {height}  Weight: {weight}lbs"
            return demographics


def check_demographics(name, sex, dob, metric, height, weight):  # getting the demographics right is very important
    while True:
        demographics = compile_demographics(name, sex, dob, metric, height, weight)
        print(f"{demographics}\nPlease verify that the information above is correct. [y/n] ")  # if 'n' -  can edit
        correct = valid_answer()
        if correct == "y":
            demographics = collections.namedtuple("demographics", ["fname", "lname", "sex", "dob", "height", "weight"])
            if metric == "y":  # convert metric before final storage
                d = demographics(fname=name.split()[0], lname=name.split()[1], sex=sex, dob=dob,
                                 height=MyTools.metric_uscs_height(height), weight=MyTools.metric_uscs_weight(weight))
            else:  # demographic final storage
                d = demographics(fname=name.split()[0], lname=name.split()[1], sex=sex,
                                 dob=dob, height=height, weight=weight)
            if MyTools.current_age_calculator(dob) < 18:  # check if pt over 18 otherwise parent fills out form
                input("Patient is a minor. Please have a parent/legal guardian answer the following questions.\nPress "
                      "enter to continue.")
            return d
        if correct == "n":  # May separate into another fx? edit_demographics
            print("Input the number of the field that is incorrect.\n1. Name\n2. Sex\n3. DOB\n4. Height\n5. Weight")
            while True:
                edit_field = input()
                if edit_field.isdigit() and int(edit_field) <= 5:
                    break  # if correct input continue on
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


def removal_message(removable):
    return input(f"Before your MRI scan, you will be asked to remove your {removable}. Press enter to acknowledge.")


# index format = 0 question - printed text for user
#                1 tag - if input = tag it is flagged for tech
#                2 card or removable - if "y" asks for card info / prints removal message
#                3 input - accepts raw input instead of the default 'y', 'n', or 'back'.
#                4 special option - i.e. scan pacemakers


form = [["Is there ANY chance you could be pregnant?", "y", 0, 0],
        ["Do you currently have a pacemaker/defibrillator?", "y", "card", 0, "pacemaker"],
        ["Do you have abandoned pacemaker wires still in place?", "y", "card", 0],
        ["Do you have a brain aneurysm clip?", "y", "card", 0],
        ["Do you have a nerve or bone growth stimulator?", "y", "card", 0],
        ["Do you have any stents?", "y", "card", 0],
        ["Do you have any intravascular coils?", "y", "card", 0],
        ["Do you have any vascular filters?", "y", "card", 0],
        ["Do you have an artificial heart valve?", "y", "card", 0],
        ["Do you have a shunt?", "y", "card", 0],
        ["Do you have any eye implants?", "y", "card", 0],
        ["Have you ever worked as a welder or metal shaver?", "y", 0, 0],
        ["Do you now or have you ever had an injury involving metal to your eye?", "y", 0, 0],
        ["Is there any possibility of a metal fragment in your eye from an injury?", "y", 0, 0],
        ["Do you have any shrapnel, BB's, or gunshot wounds?", "y", 0, 0],
        ["Do you have any ear implants?", "y", "card", 0],
        ["Do you wear hearing aids?", "y", "hearing aids", 0],
        ["Do you have an implanted drug pump?", "y", "card", 0],
        ["Do you have an insulin pump?", "y", "insulin pump", 0],
        ["If you have any other metallic implants that were not asked about, please type them in now. "
        "If not, type 'n'. ", "raw", 0, "input"],  #
        ["Have you ever had MRI contrast before?", "NA", 0, 0],  #
        ["Has your body ever had a negative reaction to MRI contrast?", "y", 0, 0],
        ["Are you diabetic?", "y", 0, 0],
        ["Do you have a history of high blood pressure?", "y", 0, 0],
        ["Do you have a history of kidney failure?", "y", 0, 0],
        ["Are you on dialysis?", "y", 0, 0],
        ["Do you have any liver disease?", "y", 0, 0],
        ["Do you have multiple myeloma?", "y", 0, 0]]


graveyard = []  # where unused questions go to die and become undead again
final = []  # answers stored here


def questionnaire(scan_pacemakers):
    q_count = 0
    # Begin Questionnaire
    print("Read each question carefully and answer with either 'y' or 'n' unless otherwise stated.")  # instructions
    print("At any time you can enter 'back' to go back to the previous question.\n")
    while q_count < len(form):  # when Q count hits Q length we stop
        while True:
            if form[q_count][3] == "input":  # no [y/n] for raw input
                answer = input(form[q_count][0])
                final.append((form[q_count], answer))  # log the question, options, and answer
                q_count += 1  # count question after answer logged
                break
            else:
                answer = input(f"{form[q_count][0]} [y/n] ")  # form indexed by question count (starting 0)
            if answer == "back":
                if q_count == 0:  # if input back command at first question
                    answer = input("Exit without completing? [y/n] ")
                    if answer == "y":
                        home()
                        return
                    if answer == "n":  # ask first questions again
                        break
                q_count -= 1  # question count - 1 to go back
                del[final[-1]]  # deletes last question answered
            elif answer == "y":
                if not scan_pacemakers:  # can be changed in settings
                    try:
                        if form[q_count][4] == "pacemaker":
                            input("STOP! Our facility does not have the capability to perform MRI scans on patients "
                                  "with pacemakers.\nPlease notify staff. Press enter to exit.")
                            quit()
                    except IndexError:
                        pass
                if form[q_count][2] == "card":  # catches card option and stores card info
                    final.append((form[q_count], answer, f"Card Info: {check_card()}"))
                elif form[q_count][2] != 0:
                    removal_message(form[q_count][2])
                    final.append((form[q_count], answer))
                else:
                    final.append((form[q_count], answer))  # log the question, options, and answer
                q_count += 1  # count question after answer logged
                break
            elif answer == "n":
                final.append((form[q_count], answer))  # log the question, options, and answer
                q_count += 1  # count question after answer logged
                while form[q_count][3] == "opt":  # skips over optional follow-up questions
                    q_count += 1  # count question after answer logged
                break
            else:
                print("Invalid entry. Please enter 'y', 'n', or 'back'.")  # catches wrong entry
                continue
        if form[q_count] == form[-1]:
            break  # end questionnaire
    return final


def final_form():  # prints screen form questions with answers
    print("\n\nENTIRE SCREENING FORM:")  # header
    for entry in final:
        try:
            print(entry[0][0], entry[1].upper(), entry[2])  # question, answer, and catches card info attached
        except IndexError:
            print(entry[0][0], entry[1].upper())  # question and answer
    return


flagged_answers = []


def get_flagged_answers():
    for entry in final:
        if entry[0][2] == "raw":  # catches raw input option
            if entry[0][1] != "n":  # if == 'n' no flag
                flagged_answers.append((entry[0][0], entry[1]))  # question, answer
        elif entry[0][1] == entry[1]:  # if tag == answer
            try:  # question, answer, and catches card info attached
                flagged_answers.append((entry[0][0], entry[1].upper(), entry[2]))
            except IndexError:
                flagged_answers.append((entry[0][0], entry[1].upper()))  # question and answer
        elif entry[0][1] == "NA":  # if option is NA it will never flag no matter the answer
            pass
    return


def write_form(d):
    fhand = open("Schedule.txt", "r")
    content = fhand.readlines()  # creates list of lines in the file
    match = 0
    for line in enumerate(content):
        if re.search(f"{d.lname}, {d.fname} DOB: {d.dob}", line[1]):  # else try to merge? create new entry? lol
            match += 1
            i = line[0]  # catches index of matching line
            count = 1
            new_index = i + count  # uses current line index + how many lines to skip to get to desired index
            while True:
                if "[MRI Screening Form]" in content[new_index]:  # finds string under patient's info
                    di = new_index + 1  # desired indexed line to write to
                    break
                else:
                    count += 1  # used in a sum to parse to proper index for writing
            insert_form = f"HEIGHT: {d.height} WEIGHT: {d.weight} " \
                          f"AGE: {MyTools.current_age_calculator(d.dob)}\n"  # what will be written at index
            for question in final:
                insert_form += f"{question[0][0]} {question[1].upper()}\n"  # populate final form
            insert_form += "\nFLAGGED QUESTIONS:\n\n"
            for answer in flagged_answers:  # populate flagged questions
                try:
                    insert_form += f"{answer[0]} {answer[1]} -- {answer[2]}\n"  # with card info
                except IndexError:
                    insert_form += f"{answer[0]} {answer[1]}\n"  # without card info
            insert_form += f"\n  There are {len(flagged_answers)} flagged questions for this patient.\n"
            content[di] = f"{insert_form}\n"  # inserting form into the indexed line where it should go
            with open("Schedule.txt", "w") as file:
                file.writelines(content)  # rewrites entire file? with new form included - seems inefficient
        else:
            pass
    if match == 0:  # if name is not on file it gets appended
        insert_form = f"\n\nNAME: {d.lname}, {d.fname} DOB: {d.dob} SEX: {d.sex} PHONE: NA\n[MRI Screening Form]\n" \
                      f"HEIGHT: {d.height} WEIGHT: {d.weight} AGE: {MyTools.current_age_calculator(d.dob)}\n"
        for question in final:
            insert_form += f"{question[0][0]} {question[1].upper()}\n"  # populate final form
        insert_form += "\nFLAGGED QUESTIONS:\n\n"
        for answer in flagged_answers:  # populate flagged questions
            try:
                insert_form += f"{answer[0]} {answer[1]} -- {answer[2]}\n"  # with card info
            except IndexError:
                insert_form += f"{answer[0]} {answer[1]}\n"  # without card info
        insert_form += f"\n  There are {len(flagged_answers)} flagged questions for this patient.\n"
        with open("Schedule.txt", "a") as file:  # append
            file.writelines(insert_form)
    return
