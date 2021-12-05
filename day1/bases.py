"""
Binary to other bases and vice versa.
"""

num = int(input("Enter number: "))
binaryNum = bin(num)
print(bin(num))  # Gives binary of number
print(oct(num))  # Gives octal of number
print(hex(num))  # Gives hexadecimal of number

"""
 Since we have base 2 in binary, we can use 2 as the base to convert binary to int. It is 
 similar for octal and hexadecimal.
 print(int("0b101", 2))
 print(int("0o101", 8))
 print(int("0x101", 16))
"""
print(int(binaryNum, 2))

"""
In Python None is there which is similar to null in CPP and JS.
"""
