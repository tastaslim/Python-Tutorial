import string
from collections import ChainMap, Counter, deque, namedtuple, defaultdict, OrderedDict

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)

# print(car_pricing.maps)  # List of dictionaries
# print(car_pricing['hood'])  # 500
# print(list(car_pricing.keys()))  # List of keys
# print(type(car_pricing))  # <class 'collections.ChainMap'>
# print(type(car_pricing.keys()))  # <class 'collections.abc.KeysView'>
# print(type(car_pricing.values()))  # <class 'collections.abc.ValuesView'>
# print(list(car_pricing.values()))  # List of values
# print(list(car_pricing.items()))  # List of tuples


# Counter #
counter = Counter('superfluous')  # <class 'collections.Counter'>

# print(counter) # Counter({'u': 3, 's': 2, 'p': 1, 'e': 1, 'r': 1, 'f': 1, 'l': 1, 'o': 1})
# print(counter['u'])  # count of character u in string ==> 3
# print(
#     counter.items())  # # List of tuples ==> dict_items([('s', 2), ('u', 3), ('p', 1), ('e', 1), ('r', 1), ('f', 1), ('l', 1), ('o', 1)])
# print(counter.most_common(2))  # First 2 most frequent elements [('u', 3), ('s', 2)]
# print(counter.most_common(2)[0][
#           0])  # First most frequent element u ==> counter.most_common(2) =  [('u', 3), ('s', 2)] ==> counter.most_common(2)[0] = ('u', 3) ==> counter.most_common(2)[0][0] = u

# print(counter.keys())  # ==> dict_keys(['s', 'u', 'p', 'e', 'r', 'f', 'l', 'o'])
# print(list(counter.keys()))  # list of keys ==> ['s', 'u', 'p', 'e', 'r', 'f', 'l', 'o']
# print(type(counter.keys()))  # <class 'dict_keys'>
# print(counter.values())  # ==> dict_values([2, 3, 1, 1, 1, 1, 1, 1])
# print(list(counter.values()))  # list of values ==> [2, 3, 1, 1, 1, 1, 1, 1]

# print(counter.elements())  # <itertools.chain object at 0x7f8b8c0b7a90>
# print(list(counter.elements()))  # ['s', 's', 'u', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']
#
# counter2 = Counter('super')
# counter.subtract(counter2)  # Removes the count of elements in counter2 from counter
# print(list(counter.elements()))  # ['s', 'u', 'u', 'f', 'l', 'o']
#
# counter.update(counter2)  # Adds the count of elements in counter2 to counter
# print(list(counter.elements()))  # ['s', 's', 'u', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']


# defaultdict #
animal = defaultdict(int)  # dictionary with default value as 0
# lst = [1, 2, 3, 5, 2, 5, 1, 2, 6, 2, 8, 9]
# for i in lst:
#     animal[i] += 1
#
# print(list(animal.keys()))  # [1, 2, 3, 5, 6, 8, 9]
# print(list(animal.values()))  # [2, 4, 1, 2, 1, 1, 1]
# animal = defaultdict(lambda: "Monkey")  # for each key the default value will be Monkey
# animal['Sam'] = 'Tiger'
# print(animal['Nick'])
#
# print(animal)


# deque #

d = deque(string.ascii_uppercase)
# for letter in d:
#     print(letter), end=" ")

# d = deque(string.ascii_lowercase)
# for letter in d:
#     print(letter, end=" ")
# print()
# d.append('bork')
# print(d)
#
# d.appendleft('test')
# print(d)
#
# d.rotate(1)
# print(d)

"""
This code works in much the same way as Linux’s tail program does. Here we pass in a filename to our script along with 
the n number of lines we want to return. The deque is bounded to whatever number we pass in as n. This means that once 
the deque is full, when new lines are read in and added to the deque, older lines are popped off the other end and discarded. 
We also wrapped the file opening with statement in a simple exception handler because it’s really easy to pass in a malformed 
path. This will catch files that don’t exist for example.
"""

# def get_last(filename, n=5):
#     """
#     Returns the last n lines from the file
#     """
#     try:
#         with open(filename) as f:
#             # read file content ==> f.read()
#             return deque(f, n)
#     except OSError:
#         print("Error opening file: {}".format(filename))
#         raise
#
#
# get_last('collections_module.md', 5)


# namedtuple #
Animal = namedtuple('Animal',
                    'name age type')  # create a namedtuple where class name is Animal and properties are name, age and type
object1 = Animal('Dog', 2, 'Mammal')  # create an object of Animal class
# object1.name = 'Cat'  # cannot change the value of name property as namedtuple is immutable
# print(object1.name)  # Dog ===> object1[0]


# OrderedDict #
scores = [('Sam', 100), ('Nick', 90), ('John', 80), ('Bob', 70)]
normal_dictionary = {}
for key, value in scores:
    normal_dictionary[key] = value

# order of keys can be anything as normal dictionary is not ordered
# print(normal_dictionary)

# To create an ordered dictionary we can use OrderedDict
new_d = OrderedDict(scores)  # under the hood implements doubly linked list
# print(
#     new_d)  # OrderedDict([('Sam', 100), ('Nick', 90), ('John', 80), ('Bob', 70)]) ==> type is <class 'collections.OrderedDict'>
#
# print(new_d.keys())  # odict_keys(['Sam', 'Nick', 'John', 'Bob'])
# print(new_d.values())  # odict_values([100, 90, 80, 70])
# print(list(new_d.items()))  # [('Sam', 100), ('Nick', 90), ('John', 80), ('Bob', 70)]
# print(list(new_d.keys()))  # ['Sam', 'Nick', 'John', 'Bob']
# print(list(new_d.values()))  # [100, 90, 80, 70]

# dict_1 = new_d.popitem()  # removes and returns the last item from the dictionary
# dict_2 = new_d.popitem(last=False)  # removes and returns the first item from the dictionary
# print(dict_2)
# move_to_end   ==> moves the key to either end of the dictionary
# new_d.move_to_end('Sam')  # moves the key to the end of the dictionary
# new_d.move_to_end('Sam', last=False)  # moves the key to the beginning of the dictionary

new_d_1 = reversed(new_d)  # returns a reversed iterator over the keys of the dictionary
print(list(new_d_1))  # ['Bob', 'John', 'Nick', 'Sam']

with open('') as f:
    f.write('')
