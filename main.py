# CS LEVEL 3 @ UofG -- preparing for enrolment in Honours
# Can you analyse my course choices?
# Do they clash?
# Am I suitable to take them?
# C-O-URSOR V1.2 -- with an interactive menu, improved

from functions import *
from course import *

# command input to functions
options = {"info": course_info, "clash": clash, "req": requires,
           "cred": get_credits, "display": display, "add": add_choices,
           "remove": remove_choices, "reset": reset}

# print available honours courses
clist = []
for i in sorted(courses):
    clist.append(courses[i]["name"] + " " + i)
for c1,c2,c3 in zip(clist[::3], clist[1::3], clist[2::3]):
    print '{:<55}{:<55}{:<}'.format(c1,c2,c3)

# start interaction
print("\nThis program assumes you have an idea of what courses you want to take during the semester.\n"
      "Consult given course specs for more information about the available choices.\n")

first_input = raw_input("Please enter the acronyms of your courses of interests, comma separated: ")
add_choices(first_input)
running = True

while running:
    temp = get_option()
    args = []
    if len(temp.split(" ", 1)) > 1:
        temp = temp.split(" ", 1)
        for i in temp: i.strip()
        cmd = temp[0]
        args += temp[1:]
    else:
        cmd = temp
    if cmd in options:
        try:
            options[cmd](*args)
        except Exception as error:
            print(repr(error))
    elif cmd == "stop":
        running = False
    else:
        print("Wrong command: try again")