# Selecting Substrings : Writing a Python Procedure

# Let p and q each be strings containing two words separated by a space.

# Examples:
#    "bell hooks"
#    "grace hopper"
#    "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q. Return False otherwise.

def myfirst_yoursecond(p, q):
    first = get_first(p)
    second = get_second(q)
    return first == second


def get_first(w):
    space_index = find_space(w)
    return w[0:space_index]


def get_second(w):
    space_index = find_space(w)
    return w[space_index + 1:]


def find_space(w):
    return w.find(" ")


print(myfirst_yoursecond("bell hooks", "curer bell"))
# >>> True

# re=r"[0-9]+(?:-[0-9]+)*"
