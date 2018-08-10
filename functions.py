from course import Course

courses = Course.courses
choices = []
acronyms_input = []


def get_option():
    print("\nWhat do you want to do now?")
    print(  # TODO "full   >>> run a full analysis\n"
          "info     >>> get more information about a course\n"
          "clash    >>> check for clashes\n"
          "req      >>> check for missing requirements\n"
          "cred     >>> check for number of credits\n"
          # TODO "strand   >>> display courses for a specified strand\n"
          "add      >>> add 1+ course to my choices\n"
          "remove   >>> remove 1+ course from my choices\n"
          "reset    >>> reset your choices\n"
          "stop     >>> terminate program\n")
    return raw_input("Enter command: ").strip()


def add_choices():
    acronyms_input = raw_input("Please enter the acronyms of your courses of interests, comma separated: ").replace(" ", "").split(",")

    # GET COURSE INSTANCES
    for a in acronyms_input:
        found = False
        for course in courses:
            if a == course.acronym:
                choices.append(course)
                found = True
        if not found:
            print("\nThe acronym " + a + " doesn't seem to match any courses.")
            acronyms_input.remove(a)


def remove_choices():
    acro = raw_input("Please enter the courses you want to delete from your choices (acronyms, comma-separated): ").replace(" ", "").split(",")
    for a in acro:
        if a in acronyms_input:
            acronyms_input.remove(a)
        else:
            print(a + "isn't a correct course acronym or was not in your choices.")


def course_info():
    a = raw_input("Enter course acronym: ").strip()
    for c in courses:
        if a == c.acronym:
            print("{} {}\n"
                  "clashes with: {}\n"
                  "requires: {}\n"
                  "year, semester: {}\n"
                  "{}\n").format(c.name, c.strand, c.clashes, c.req, c.year, c.comment)


def clash():
    clashes = ""
    print("\nComputing clashes...")
    done = []

    for choice1 in choices:
        for choice2 in choices:
            # this compares acronym pairs in order not to repeat clashes
            if choice1.clashes and choice2.acronym in choice1.clashes \
                    and choice2.acronym+choice1.acronym not in done:
                clashes += str(choice1) + " and " + str(choice2) + " clash\n"
                done.append(choice1.acronym+choice2.acronym)

    if clashes:
        print(clashes)
    else:
        print("You're clash-free!")


def requires():
    print("\nComputing prerequisites...\n")
    requirements = ""

    for choice in choices:
        if choice.req:
            req_list = []
            missing = True
            for req in choice.req:
                if req not in acronyms_input:
                    req_list.append(req)
                    missing = False
            if not missing:
                requirements += "You need to take " + str(req_list) + " for " + str(choice) + "\n"

    if requirements:
        print(requirements)
    else:
        print("You fit all prerequisites for your courses!")


def get_credits():
    tc = fc = 0

    # TODO: figure out mandatory courses issue
    for c in choices:
        if c.year[0] == '34':
            tc += 10
        elif c.year[0] == '4':
            fc += 10
    if (tc == 30 or tc == 40) and (fc == 60 or fc == 70):
        print("Right amount of credits. You're all good! \n")
    else:
        print("You haven't chosen the right amount of credits.\n"
              "Here's where you stand: \n"
              "{} credits for level 3, need 30 or 40\n"
              "{} credits for level 4, need 60 or 70").format(tc, fc)


def reset():
    choices[:] = []
    acronyms_input[:] = []
    print("Choices reset. Add more courses now or consult more information! ")
