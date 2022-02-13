import MRIScreening

# If Q = yes - prompt technologist with each instance
# If no go - prompt staff
# Dictionary to pull specifics? -> can't use input fx in dict
# age can determine if minor or not
# ask for phone number for tech to reach or pull it from their file?
# Set up a start menu (Questionnaire, settings, blah blah)

# HOME
MRIScreening.home()

# appt = "07/20/2022"  # going to pull from file
# name = MRIScreening.input_name()
# sex = MRIScreening.input_sex()
# dob = MRIScreening.input_dob()
# metric = MRIScreening.metric_system()
# height = MRIScreening.input_height(metric)
# weight = MRIScreening.input_weight(metric)
#
# # CURRENT AGE
# current_age = MyTools.current_age_calculator(dob)
#
# # APPT AGE
# appt_age = MyTools.appt_age_calculator(appt, dob)
#
# # DEMOGRAPHICS INPUT CHECKER
# MRIScreening.check_demographics(name, sex, dob, metric, height, weight)
#
# # DEMOGRAPHICS COMPILER - can use for file input later
# demographics = MRIScreening.compile_demographics(name, sex, dob, metric, height, weight)
#
#
# # METRIC HEIGHT AND WEIGHT CONVERTER CHECK - for now
# if metric == "y":  # metric units to USCS units
#     height = MyTools.metric_uscs_height(height)
#     weight = MyTools.metric_uscs_weight(weight)
#     demographics = f"Name: {name}\nDOB: {dob}  Age: {current_age}\nHeight: {height}  Weight: {weight}lbs"
# print(f"DEBUG: METRIC CONVERTER\n{demographics}")


# EXTRACTING "YES" ANSWERS AND RELATED INFO
# MRIScreening.get_flagged_answers()
