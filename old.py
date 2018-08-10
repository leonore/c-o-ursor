# CS LEVEL 3 @ UofG -- preparing for enrolment in Honours
# I have an idea of what courses I want to take.
# What can I pick?
# Can you report any problems with my choices?
# C-O-URSOR V0.2 -- reports any clashes and requirements, looks nicer


# Storage structure for courses
class Course:

    courses = []

    def __init__(self, name, acronym, strand, year, clashes=None, req=None, comment=None):
        self.name = name
        self.acronym = acronym
        self.strand = strand # strand of specialisation (1 or 2 of 5) or MANDATORY for CSH students
        self.clashes = clashes # any clashes with other courses
        self.req = req # any prerequisites for the course
        self.year = year # when does this course run
        self.comment = comment # reports recommended courses rather than mandatory ones (not used in V0.1)
        self.courses.append(self) # stores each course in a list for future use

    def __str__(self):
        return '{} ({})'.format(self.name, self.acronym)


def make_course(name, acronym, strand, year, clashes=None, req=None, comment=None):
    course = Course(name, acronym, strand, year, clashes, req, comment)
    return course


# COURSE FILE READING
# transcribed from the school's course list by myself
# Format:
# N Name
# A Acronym
# S STRAND
# C clashes
# R requirements
# Y semesters the course runs
# # comment
# Credits are always 10

f = open("HONOURS_COURSES.txt", "r")
lines = f.readlines()

name, acronym, strand, clashes, req, year, comment = [None] * 7  # empty value init

for line in lines:
    # if we encounter a newline, then we've finished storing course details
    # -> Create a new course instance
    if line == "\n":
        make_course(name, acronym, strand, year, clashes, req, comment)
        name, acronym, strand, year, clashes, req, comment = [None] * 7
        continue
    elif line[0] == "N":
        name = line.strip("N").strip()
    elif line[0] == "A":
        acronym = line.strip("A").strip()
    elif line[0] == "S":
        strand = line.strip("S").strip().replace(" ", "").split(",")
    elif line[0] == "C" and len(line) > 3:  # length 3 counts: signaling letter, eventual space, \n
        clashes = line.strip("C").strip().replace(" ", "").split(",")
    elif line[0] == "R" and len(line) > 3:
        req = line.strip("R").strip().replace(" ", "").split(",")
    elif line[0] == "Y":
        year = line.strip("Y").strip().replace(" ", "").split(",")
    elif line[0] == "#" and len(line) > 3:
        comment = line.strip()

f.close()


# ESSENTIAL VARIABLES
strands = { "DATASCIENCE": 0,
           "HUMANCOMPUTERINTERACTION": 0,
           "THEORY": 0,
           "SYSTEMS": 0,
           "SECURITY": 0,
           "MANDATORY": 0 }
courses = Course.courses
choices = []

for c1,c2,c3 in zip(courses[::3],courses[1::3], courses[2::3]):
    print '{:<55}{:<55}{:<}'.format(c1,c2,c3)

# USER INPUT
print("\nThis program assumes you have an idea of what courses you want to take during the semester.\n"
      "Consult given course specs for more information about the available choices.\n")
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

# DECISION MAKING: STRANDS
print("\nComputing results in relation to strands...\n")
for choice in choices:
    for s in choice.strand:
        strands[s] += 1
preferred = max(strands, key=strands.get)
print("Your preferred strand seems to be " + preferred)

# DECISION MAKING: CLASHES
print("\nComputing results in relation to clashes...\n")
done = []

for choice1 in choices:
    for choice2 in choices:
        # this compares acronym pairs in order not to repeat clashes
        if choice1.clashes and choice2.acronym in choice1.clashes \
                and choice2.acronym+choice1.acronym not in done:
            clashes = True
            print(str(choice1) + " and " + str(choice2) + " clash")
            done.append(choice1.acronym+choice2.acronym)

if not clashes:
    print("You don't have any clashes!")


# DECISION MAKING: REQUISITES
print("\nComputing results in relation to prerequisites...\n")
suitable = True
req_list = []

for choice in choices:
    if choice.req:
        req_list = []
        missing = True
        for req in choice.req:
            if req not in acronyms_input:
                req_list.append(req)
                missing = suitable = False
        if not missing:
            print("You need to take " + str(req_list) + " for " + str(choice))

if suitable:
    print("You aren't missing any courses!")