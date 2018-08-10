# Storage structure for courses
courses = {}


def make_course(name, acronym, strand, year, clashes=None, req=None, comment=None):
    courses[acronym] = {"name": name, "strand": strand, "year": year,
                        "clashes": clashes, "req": req, "comment": comment}

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

