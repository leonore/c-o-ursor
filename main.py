# CS LEVEL 3 @ UofG -- preparing for enrolment in Honours
# Can you analyse my course choices?
# Do they clash?
# Am I suitable to take them?
# C-O-URSOR V1.0 -- with an interactive menu

from functions import *
from course import *

# command input to functions
options = {"info": course_info, "clash": clash, "req": requires,
           "cred": get_credits, "add": add_choices,
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

add_choices()
running = True

while running:
    cmd = get_option()
    if cmd in options:
        try:
            options[cmd]()
        except Exception as error:
            print(repr(error))
    elif cmd == "stop":
        running = False
    else:
        print("Wrong command: try again")