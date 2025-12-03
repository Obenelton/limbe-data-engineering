print("This line will be printed.")
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
print("Goodbye, World!")
# Variables
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
a, b = 3, 4
print(a, b)
# This will not work
one = 1
two = 2
hello = "hello"
#print(one + two + hello)

# Exercise
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("string: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)
# Exercise
numbers = [1,2,3]
strings = ['hello', 'world']
names = ["John", "Eric", "Jessica"]
second_name = None

#write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append('hello')
strings.append('world')

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

number = 1 + 2 * 3 / 4.0
print(number)
remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

print([1,2,3] * 3)
# Exercise
x = object()
y = object()

#TODO
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
#string formating
name = "John"
print("Hello %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)
# Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
# Basic string operations
astring = "Hello world!"
astring2 = 'Hello world!'
print(len(astring2))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2])
print(astring[: : -1])
print(astring.upper())
print(astring.lower())
print(astring2.startswith("Hello"))
print(astring2.endswith("asdfasdfasdf"))
print( astring.split(" "))

# Exercise
s = "Strings are awesome!"
print("Length of s = %d" % len(s))
print("the first occurence of letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[: 5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The characters with odd index are '%s'" %s [1:2])
print("The last five characters '%s'" % s[-5:])
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome"):
    print("String ends with 'ome!'. Good!")
print("Split the words of the string: %s" % s.split(" "))

# Conditions
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
name = "John"
if name in ["John", "Rick"]:
    print("your name is either John or Rick.")

Statement = True
Another_statement = False
if Statement is True:
    pass
elif Another_statement is True:
    pass
else:
    pass
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# change this code
number = 16
second_number = 0
first_array = [1,2]
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# Loops
primes = [2,3,5,7]
for prime in primes:
    print(prime)
for x in range(5):
    print(x)
for x in range(3,6):
    print(x)
for x in range(3,8,2):
    print(x)
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
for x in range(10):
    if x % 2 == 1:
        continue
    print(x)

# Exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)

# functions
# Day 2 – Functions (learnpython.org lessons)

def my_function():
    print("Hello from my function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, from my function! I wish you %s" % (username, greeting))

def sum_two_numbers(a, b):
    return a + b

# Call the functions to test them (this is REQUIRED for the site to show "Success!")
my_function()

my_function_with_args("Elton", "a wonderful data engineering career")

x = sum_two_numbers(5, 10)
print(x)        # should print 15
# Exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()