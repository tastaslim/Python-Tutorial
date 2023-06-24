import pdb


def add(a, b):
    pdb.set_trace()
    t = 4 * 12
    print("one two ka four. Four two ka one. My name is La khan.")
    print(t)
    return a + b


# pdb has built-in step function which helps us to go to next_element_address line of the code
# set_trace() gives information about file and function/class/anything which we are debugging.
# continue is used to continue moving in the code until we return something.
add(2, 'Easy')
