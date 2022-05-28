from __future__ import barry_as_FLUFL

# msg = "hello world"
# print(msg)

# x = 1
# print(x)
# x_str = str(x)
# print("my fav number is", x, ".", "x=", x)
# print("My fav number is " + x_str + "." + " x = " + x_str)
 
# text = input("type something")
# print(5*text)
# text
# type(text) 

# num = int(input("Type a number: "))
# print(5*num)

# if 6<7:
#     print("Yep")

# var = 'Panda'
# if var == "panda":
#    print("Cute!")
# elif var == "Panda":
#    print("Regal!")
# else:
#    print("Ugly...")
 
# temp = 120
# if temp > 85:
#    print("Hot")
# elif temp > 100:
#    print("REALLY HOT!")
# elif temp > 60:
#    print("Comfortable") 
# else:
#    print("Cold")

# x = 5
# if x != 5:
#     print("im here")
# else:
#     print("no i am not")

# Loops 
# n = input("You are in the Lost Forest. Go left or right?")
# while (n == "right"):
#     n = input("You are in the Lost Forest. Go left or right?")
# print("You got out of the Lost Forest!")

# mySum = 0
# for i in range(5, 11, 2):
#     mySum += i

# print(mySum)

# num = 5
# if num > 2:
#     print(num)
#     num -= 1
# print(num)
# num = 0
# while num <= 5:
#     print(num)
#     num += 1

# print("Outside of loop")
# print(num) 

# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')

# num = 100
# while not False:
#     if num < 0:
#         break
# print('num is: ' + str(num)) 

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# num = 10
# for num in range(5):
#     print(num)
# print(num)

# myStr = '6.00x'

# for char in myStr:
#     print(char)

# print('done')

# greeting = 'Hello!'
# count = 0

# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)

# print('done')
# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 

# x = int(input('Enter an integer: '))
# ans = 0
# while ans**3 < x:

#     ans = ans + 1

# if ans**3 != x:
#     print(str(x) + ' is not a perfect cube')
# else:
#     print('Cube root of ' + str(x) + ' is ' + str(ans))

# cube = -8
# for guess in range (abs(cube) + 1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(cube, 'is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
#     print("Cube root of", cube, "is", guess)

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         length = len(phrase)
#         print(length)
#         break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))

# Problem Set: 1
# Q 1
# s = str(input('Enter: '))

# Nvowels = 0
# for k in s:
#     if(k == 'a' or k == 'e' or k =='i' or k == 'o' or k == 'u'):
#         Nvowels += 1

# print("Number of vowels: ", Nvowels)

# Q 2
# s = str(input('Enter: '))

# Nword = 0

# for k in range(len(s) + 1):
#     if(s[k:k+3] == 'bob'):
#         Nword += 1

# print("Number of times bob occurs is: ", Nword)

# Q 3
# s = str(input("Enter: "))

# maxlength = 0
# current = s[0]
# longest = s[0]

# for i in range(len(s) - 1):
#     if s[i+1] >= s[i]:
#         current = current + s[i+1]
#         if len(current) > maxlength:
#             maxlength = len(current)
#             longest = current
#         else:
#             current = s[i+1]
#         i += 1
#     print("The longest substring in alphabetical order is:" + longest)

# ans = 0
# neg_flag = False 
# x = int(input("Enter an integer: "))
# if x < 0:
#     neg_flag = True
# while ans**2 < x:
#     ans = ans + 1
# if ans**2 == x:
#     print("Square root of", x, "is", ans)
# else:
#     print(x, "is not a perfect square")
#     if neg_flag:
#         print("Just checking... did you mean", -x, "?")

# s = "abcdefgh"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")

# an_letters = "aefhilmnorsxAEFHILMNORSX"

# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# i = 0

# while i < len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an " + char + "!" +char)
#     else: 
#         print("Give me a " + char + "!" + char)
#     i += 1
#     print("What does that spell?")
#     for i in range(times):
#         print(word, "!!!")

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# daysConversions = {
# 	"Mon" : "Monday", 
# 	"Tue" : "Tuesday",
# 	"Wed" : "Wednesday",
# 	"Thur" : "Thursday",
# 	"Fri" : "Friday",
# 	"Sat" : "Saturday",
# 	"Sun" : "Sunday"
# }

# print(daysConversions["Thur"])
# print(daysConversions.get("Luv", "Not a valid key"))

num = 2**3
def raise_to_power(base_num, pow_num):
	result = 1
	for index in range(pow_num):
		result = result*base_num
	return result # base_num**pow_num 
print(raise_to_power(3, 3))