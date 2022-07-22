#  palindrome program
def isPalindrome(s):
	return s == s[::-1]
s = "madam"
s = isPalindrome(s)
if s:
	print("Yes")
else:
	print("No")


# # factorial program
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
num = 7;
print("Factorial of",num,"is",
factorial(num))

# fibonacci series
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))
 

#  # armstrong number program
n = int(input("Enter a number: "))
s = 0
t = n
while t > 0:
   digit = t % 10
   s += digit ** 3
   t //= 10
if n == s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")


# #calculator program
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   print(A,"+",B,"=", (A+B))
elif choice == '-':
   print(A,"-",B,"=", (A-B))
elif choice == '*':
   print(A,"*",B,"=", (A*B))
elif choice == '/':
   print(A,"/",B,"=", (A/B))
else:
     print("Invalid input")

# #pattern programs 
# # square
row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# # leap year program
Year = int(input("Enter a Year: "))
if Year % 4 == 0 and Year % 100 != 0:
    print("it is a Leap Year")
elif Year % 100 == 0:
    print("it is not a Leap Year")
elif Year % 400 ==0:
    print("it is a Leap Year")
else:
    print("it is not a Leap Year")

# # prime number
number = int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, "is not prime number")
            break
    else:
            print(number, "is prime number")


# # area of rectangle
def AreaofRectangle(width, height):
    Area = width * height
    print("Area of a Rectangle is: %.2f" %Area)
AreaofRectangle(12,9)


# # reverse a list 
a = [8,5,4,2,9]
a.reverse()
print(a)


# #sum of elements in a list
l1 = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    l1.append(numbers)
print("Sum of elements in given list is :", sum(l1))


# Find average, max, min of list elements"""
list = [1,2,3]
minimum = min(list)
maximum = max(list)
sum = sum(list)
length = len(list)
average = sum/length
print(average)

#Write a Python program to create a dictionary grouping a sequence of key value pairs into a dictionary of lists.
# a. Original list:[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}"""
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))


# Write a Python program to convert more than one list to nested 
# dictionary.
# a. Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary: [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': 
# {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]"""
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))


# Python program to check if a set is a subset of another set.
a = {1,2,3}
b = {1,2,3,4,5}
print(a.issubset(b))

# Write a Python program to create a symmetric difference and set  difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
result = A.symmetric_difference(B)
print(result)

# Write a Python program to remove an empty tuple(s) from a list of tuples.
# a. Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
#  a. Original Tuple: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
#  Average value of the numbers of the said tuple of tuples:[30.5, 34.25, 27.0, 23.25]
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))


# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters"""
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")

