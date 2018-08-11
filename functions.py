from course import *

choices = []


def get_option():
    print("\nWhat do you want to do now?")
    print("full         >>> run a full analysis\n"
          "info         >>> get more information about a course (include acronym)\n"
          "add          >>> add 1+ course to my choices (list your choices)\n"
          "remove       >>> remove 1+ course from my choices (list your choices)\n"
          "display      >>> current list of choices\n"
          "reset        >>> reset your choices\n"
          "list         >>> list all available courses\n"
          "strand       >>> display courses for a specified strand\n"
          "clash        >>> check for clashes\n"
          "cred         >>> check for number of credits\n"
          "req          >>> check for missing requirements\n"
          "stop         >>> terminate program\n")
    return raw_input("Enter command: ").strip()


def list_courses():
    clist = []
    for i in sorted(courses):
        clist.append(courses[i]["name"] + " " + i)
    for c1, c2, c3 in zip(clist[::3], clist[1::3], clist[2::3]):
        print '{:<55}{:<55}{:<}'.format(c1, c2, c3)
    print "\nAvailable strands: ",
    for strand in strands:
        if strand != "MANDATORY": print strand,


def add_choices(acronyms):
    acronyms = acronyms.replace(" ", "").split(",")
    for a in acronyms:
        found = False
        if a in courses and a not in choices:
            choices.append(a)
            found = True
        if not found:
            print("\nThe acronym " + a + " doesn't seem to match any courses or is already in your choices.")


def remove_choices(acronyms):
    acronyms = acronyms.replace(" ", "").split(",")
    for a in acronyms:
        if a in choices:
            choices.remove(a)
        else:
            print(a + "isn't a correct course acronym or was not in your choices.")


def course_info(a):
    if a in courses:
        print("{} {}\n"
              "clashes with: {}\n"
              "requires: {}\n"
              "year, semester: {}\n"
              "# {}\n").format(courses[a]["name"], courses[a]["strand"], courses[a]["clashes"],
                               courses[a]["req"], courses[a]["year"], courses[a]["comment"])


def strand(s):
    s = s.upper()
    if s in strands:
        for c in courses:
            if s in courses[c]["strand"]:
                course_info(c)
    else:
        print "Strand {} does not exist!".format(s)


def count_strand():
    for c in choices:
        for s in courses[c]["strand"]:
            strands[s] += 1
    print "Your preferred strands seems to be {}\n".format(max(strands, key=strands.get))


def clash():
    clashes = ""
    print("\nComputing clashes...")
    done = []

    for choice1 in choices:
        for choice2 in choices:
            # this compares acronym pairs in order not to repeat clashes
            if courses[choice1]["clashes"] and choice2 in courses[choice1]["clashes"] \
                    and choice2 + choice1 not in done:
                clashes += courses[choice1]["name"] + " and " + courses[choice2]["name"] + " clash\n"
                done.append(choice1 + choice2)

    if clashes:
        print(clashes)
    else:
        print("You're clash-free!")


def requires():
    print("\nComputing prerequisites...")
    requirements = ""

    for choice in choices:
        if courses[choice]["req"]:
            req_list = []
            missing = True
            for req in courses[choice]["req"]:
                if req not in choices:
                    req_list.append(req)
                    missing = False
            if not missing:
                requirements += "You need to take " + str(req_list) + " for " + courses[choice]["name"] + "\n"

    if requirements:
        print(requirements)
    else:
        print("You fit all prerequisites for your courses!")


def get_credits():
    tc = fc = 0

    for c in choices:
        if courses[c]["year"][0] == '34' and courses[c]["year"][1] != '1':
            tc += 10
        elif courses[c]["year"][0] == '4':
            fc += 10
    if (tc == 30 or tc == 40) and (fc == 60 or fc == 70):
        print("Right amount of credits. You're all good! \n")
    else:
        print("You haven't chosen the right amount of credits.\n"
              "Here's where you stand (mandatory courses excl.): \n"
              "{} credits for level 3, need 30 or 40\n"
              "{} credits for level 4, need 60 or 70").format(tc, fc)


def display():
    print "Current choices: "
    for x in choices:
        print x,
    print "\n"


def full():
    display()
    count_strand()
    get_credits()
    clash()
    requires()


def reset():
    choices[:] = []
    print("Choices reset. Add more courses now or consult more information! ")
