# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

# l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood', 'Bible']
# f = len(max(l, key=len))


l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood', 'Bible']
f = len


def findmax(f, l):
    best_ele_sofar = None
    best_f_value_sofar = None
    for i in range(len(l)):
        elt = l[i]
        f_value = f(elt)
        if best_f_value_sofar is None or f_value > best_f_value_sofar:
            best_ele_sofar = elt
            best_f_value_sofar = f_value
    return best_f_value_sofar


print(findmax(f, l))
# Try it on your own!
