number1 = int(input("Enter a number: "))
number2 = int(input("Enter a decimal number: "))
"""
Arithmetic operators: + - * / % // **
"""
print(number1 + number2, number1 - number2, number1 * number2, number1 /
      number2, number1 % number2, number1 // number2, number1 ** number2)

"""
Bitwise operators: & | ^ ~ << >>
"""
print(number1 & number2, number1 | number2, number1 ^ number2, ~number1,)

"""
Conditional operators: < > <= >= == !=
"""
print(number1 < number2, number1 > number2,
      number1 <= number2, number1 >= number2)

"""
logical operators: and or not
"""
print(number1 and number2, number1 or number2, not number1)

# and vs &
# and ==> When any of the condition is false, it will return false and doesn't check the other condition.
# & ==> When any of the condition is false, it will return false and but checks the other condition too.
if(number1 < 0 and number2/0):
    print("Number 1 is true and number 2 is false")
else:
    print("Hey there")

"""
Assignment operators: = += -= *= /= %= **= &= |= ^= >>= <<=
"""
number2 *= 2
print(number2)
