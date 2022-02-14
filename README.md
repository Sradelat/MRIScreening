# MRI Screening Form (Under Construction!)
*Automating an existing problem in the MRI field.*


This is an ambitious first attempt to create a program that runs as a real mobile application would, excluding a GUI (for now).

### What is an MRI Screening Form?

In the MRI world, patient safety is a huge concern. Usually imaging facilities have the patient fill out screening form on a sheet of paper before their MRI.
The idea of the screening form is to find out whether or not the patient has an existing medical reason that a medical professional would deem unsafe for the
patient to undergo an MRI scan. These screening forms include questions about the patient's demographics, certain medical conditions, metallic implants
inside the body, and other relevant information that may be helpful in treating the patient.

### What does this program do in general?

This program is meant to take patient input (demographics and answers to questions), match the demographics with a schedule file, and output the entered information
to the technologist in a streamlined fashion. This will hopefully decrease technologist mistakes and increase productivity by automatically catching red flags and
bringing them to the attention of the technologist. The program has the ability to customize the list of questions such as adding, removing, sorting, and even creating 
custom questions. It will also include settings that can be tweaked, all made to suit a company's specific needs.

### What is the problem with paper?

- Limited amount of space for questions
- Confusion with scribbled out mistakes
- Difficult to change questions and format
- Technologists must sift through a wealth of information jammed onto one paper
- Technologists can easily miss red flags due to previous point

### Program Features

- Deeply customizable questions (more coming soon)
- Red flags brought to the forefront
- Ability to tweak certain settings (not implemented yet)
- Metric to USCS height and weight converter
- Age calculator based on DOB


### Finalizing Improvements

If this program were to be brought to a reality, a few minor, yet intricate improvements are intended:

- Flag height and weight based on MRI scanner restrictions 
- Calculate age of patient on appointment date instead of current date
- Detect what type of scan is being performed and flag accordingly (i.e. contrast studies, height, weight)
- Research and fine-tune questions asked on the form
- Changes made to form and settings should have permanence