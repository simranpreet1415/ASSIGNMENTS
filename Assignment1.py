#1.) write a python program to calculate the length of string.
name ='simran'
a= len(name)
print(a)


#2.) Write a Python program to count the number of characters (character frequency) in a string. 
str1 = input("enter the string")
d1 = dict()
for c in str1:
    if c in d1:
        d1[c] = d1[c]+1
    else:
        d1[c]=1
        print (d1)
 

#3.) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))


#4.) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('restart'))


#5.) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


#6.) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
v1="trimming"
if len(v1)>=3:
    if v1[-3:]=="ing":
       v1=v1+"ly"
    else:
        v1=v1+"ing"
    print (v1)
else:
        print (v1)


#7.) Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
# Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def not_poor(str1):
  pos_not = str1.find('not')
  pos_poor = str1.find('poor')
  if pos_poor > pos_not and pos_not>0 and pos_poor>0:
    str1 = str1.replace(str1[pos_not:(pos_poor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#8.)Write a Python function that takes a list of words and return the longest word and the length of the longest one. 
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
 

# 9.) Write a Python program to remove the nth index character from a nonempty string. 
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('simran', 0))
print(remove_char('simran', 3))
print(remove_char('simran', 5))


# 10) Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
print(change_sring('abcd'))
print(change_sring('121415'))


# 11) Write a Python program to remove the characters which have odd index values of a given string. 
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
print(odd_values_string('abcdef'))
print(odd_values_string('simran'))


# 12)Write a Python program to count the occurrences of each word in a given sentence. 
string= input("Enter string:")
word= input("Enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)


# 13) Write a Python script that takes input from the user and displays that input back in upper and lower cases. 
user_input = input("Who is your favourite teacher? ")
print("My favourite teacher is ", user_input.upper())
print("My favourite teacher is ", user_input.lower())


# 14) Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


# 15.) Write a Python function to create the HTML string with tags around the word(s)
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


# 16) Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]
print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))


# 17) Write a Python function to get a string made of 4 copies of the last two characters of a specified string 
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4
print(insert_end('Python'))
print(insert_end('Exercises'))


# 18) Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
def first_three(str):
	return str[:3] if len(str) > 3 else str
print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))


# 19) Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])


# 20) Write a Python function to reverses a string if it's length is a multiple of 4
name=input("enter a name: ")
if (len(name)%4==0):
    print(name[::-1]) 
else:
    print("can't")


# 21) Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1
print(to_uppercase('Python'))
print(to_uppercase('PyThon'))


# 22.) Write a Python program to remove a newline in Python
str1='Python Exercises\n'
print(str1)
print(str1.rstrip())


# 23) Write a Python program to check whether a string starts with specified characters
string = "w3resource.com"
print(string.startswith("w3r"))

