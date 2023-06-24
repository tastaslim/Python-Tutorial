"""[@summary]
break is used to break out of the loop
continue is used to skip the current iteration and continue with the next_element_address iteration
Say we have some kind of function/body/class which we are still thinking about it and want to come back to it after sometime.
    You can use pass. Meanwhile, you can test other features and then comeback to it and remove pass, implement functionality.
"""
for i in range(0, 5):
    if i == 3:
        break
    print(i)

for i in range(1, 5):
    if i == 3:
        continue
    print(i)


def print_name():
    pass  # if pass not used, it will give error as function at least need one statement inside it
