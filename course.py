# Storage structure for courses
# TODO: would a dictionary work better?
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
    return Course(name, acronym, strand, year, clashes, req, comment)


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
f.close()

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