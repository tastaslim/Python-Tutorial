number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
"""
Arithmetic operators: + - * / % // **

/  -> gives float
//  -> gives absolute value / int
%  -> gives remainder
**  -> gives power
*  -> gives product
+  -> gives output
-  -> gives difference
"""
print(number1 + number2, number1 - number2, number1 * number2, number1 /
      number2, number1 % number2, number1 // number2, number1 ** number2)
"""
Bitwise operators: & | ^ ~ << >>

&  -> bitwise and           -> 1 if both bits are 1 else 0
|  -> bitwise or            -> 1 if any bit is 1 else 0
^  -> bitwise xor           -> 1 if both bits are different else 0
~  -> bitwise not           -> 1 if bit is 0 else 0
<<  -> bitwise left shift   -> shift bits to left by n places
>>  -> bitwise right shift  -> shift bits to right by n places
"""
print(number1 & number2, number1 | number2, number1 ^ number2,
      ~number1, number1 << number2, number1 >> number2)

"""
Conditional operators: < > <= >= == !=

<  -> less than
>  -> greater than
<=  -> less than or equal to
>=  -> greater than or equal to
==  -> equal to
!=  -> not equal to

"""
print(number1 < number2, number1 > number2,
      number1 <= number2, number1 >= number2, number1 == number2, number1 != number2)

"""
logical operators: and or not

and  -> if both are true then true else false
or  -> if any one is true then true else false
"""
print(number1 and number2, number1 or number2, not number1)

if number1 < 0 and number2 / 0:
    print("Number 1 is true and number 2 is false")
else:
    print("Hey there")

"""
Assignment operators: = += -= *= /= %= **= &= |= ^= >>= <<=

=  -> assign value
+=  -> add and assign
-=  -> subtract and assign
*=  -> multiply and assign
/=  -> divide and assign
%=  -> modulus and assign
**=  -> power and assign
&=  -> bitwise and and assign
|=  -> bitwise or and assign
^=  -> bitwise xor and assign
>>=  -> bitwise right shift and assign
<<=  -> bitwise left shift and assign

"""

number1 += number2
print(number1)
number1 -= number2
print(number1)
number1 *= number2
print(number1)
number1 /= number2
print(number1)
number1 %= number2
print(number1)
number1 **= number2
print(number1)
number1 &= number2
print(number1)
number1 |= number2
print(number1)
number1 ^= number2
print(number1)
number1 >>= number2
print(number1)
number1 <<= number2
print(number1)

"""
and vs &
and ==> When any of the condition is false, it will return false and doesn't check the other condition.
& ==> When any of the condition is false, it will return false but checks the other condition too.

or vs |
or ==> When any of the condition is true, it will return true and doesn't check the other condition.
| ==> When any of the condition is true, it will return true but checks the other condition too.
"""
