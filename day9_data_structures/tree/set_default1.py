"""
Since in python, when a key is not present, appending any value specifying that key gives us error,
dim=linkedlist()
dim[0].append(1) # gives me error as key 0 not present

-- setdefault ---
Python setdefault() method is used to set default value to the key. It returns value, if the key is present. Otherwise
it inserts key with the default value. Default value for the key is None.

mp1.setdefault(distance, []).append(head.data)

What will above code do is, it checks whether key(in our case distance) is present in dictionary or not. If not adds key
in dictionary and assigns it value None and then again for any call of same key adds values
"""

dit = {"John": 1, "Jack": 2, "Remo": 3}
# ans = dit.setdefault("Tom")  # gives None since Tom key is not present in
# print(ans)

# ans1 = dit.setdefault("Tom", 100)
# print(ans1)  # gives value 100. Although key is not present in dictionary, but we are setting its default value
# # to 100 instead of returning it None.
ans2 = dit.setdefault("John")
print(ans2)  # gives 1

ans3 = dit.setdefault("John", 111)  # we will set get 1 as key is present in dictionary
print(ans3)
