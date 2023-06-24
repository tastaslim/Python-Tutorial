Python’s collections module has specialized container datatypes that can be used to replace Python’s general-purpose
containers (dict, tuple, list, and set). We will be studying the following parts of this fun module:

- ChainMap
- counter
- defaultdict
- deque
- namedtuple
- OrderedDict

There is a submodule of collections called abc or Abstract Base Classes. This is covered in day7.

---

## ChainMap ##

A **ChainMap* is a class that provides the ability to link multiple mappings together such that they end up being a
single unit. If you look at the documentation, you will notice that it accepts maps, which means that a ChainMap will
accept any number of mappings or dictionaries and turn them into a single view that you can update.

```python
from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing)
```

## Counter ##

The collections module also provides us with a neat little tool that supports convenient and fast tallies. This tool is
called **Counter**. You can run it against most iterables.

```python
from collections import Counter

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
```

## defaultdict ##

The collections module has a handy tool called defaultdict. The defaultdict is a subclass of Python’s dict that accepts
a default_factory as its primary argument. The default_factory is usually a Python type, such as int or list, but you
can also use a function or a lambda too.

```python
from collections import defaultdict

animal = defaultdict(int)  # dictionary with default value as 0
lst = [1, 2, 3, 5, 2, 5, 1, 2, 6, 2, 8, 9]
for i in lst:
    animal[i] += 1

# use lambda as default factory

animal = defaultdict(lambda: "Monkey")  # for each key the default value will be Monkey
animal['Sam'] = 'Tiger'
print(animal['Nick'])

print(animal)
```

## deque ##

According to the Python documentation, deques are a generalization of stacks and queues. They are pronounced **deck**
which is short for **double-ended queue**. They are a replacement container for the Python list. Deques are thread-safe
and support memory efficient appends and pops from either side of the deque. A list is optimized for fast fixed-length
operations. A deque accepts a maxlen argument which sets the bounds for the deque, Otherwise the deque will grow to an
arbitrary size. When a bounded deque is full, any new items added will cause the same number of items to be popped off
the other end.

As a general rule, if you need fast appends or fast pops, use a deque. If you need fast random access, use a list. Let’s
take a few moments to look at how you might create and use a deque.

```python
from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
```

## namedtuple ##

**namedtuple** returns a class (that's a child of the built-in class tuple). The first argument you pass to namedtuple
becomes the name of the class, while the list of strings becomes the attributes (data fields). You can then call the
constructor to make objects. Like dictionaries, they contain keys that are hashed to a particular value. But on
contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

```python
from collections import namedtuple

animal = namedtuple('animal', 'name age type')
perry = animal("Lion", 31, "cat")  # perry is an object of animal class
# perry = animal(name="perry", age=31, type="cat") # perry is an object of animal class. This is same as above line
print(perry)
print(perry.name)  # Lion
print(perry.age)  # 31  # perry[1] = 31
```

## OrderedDict ##

- Python’s collections module has another great subclass of dict known as OrderedDict. As the name implies, this
  dictionary keeps track of the order of the keys as they are added. If you create a regular dict, you will note that it
  is an unordered data collection:
- Note that if you add new keys, they will be added to the end of the OrderedDict instead of being automatically sorted.
- Something else to note about OrderDicts is that when you go to compare two OrderedDicts, they will not only test the
  items for equality, but also that the order is correct. A regular dictionary only looks at the contents of the
  dictionary and does not care about its order.

```python
from collections import OrderedDict

scores = [('Sam', 100), ('Nick', 90), ('John', 80), ('Bob', 70)]
ordered_dict = OrderedDict(scores)
print(ordered_dict)  # OrderedDict([('Sam', 100), ('Nick', 90), ('John', 80), ('Bob', 70)])
```