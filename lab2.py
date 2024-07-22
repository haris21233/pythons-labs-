                                    
# while loop 
count = 0
while (count < 3):
    count = count + 1
    print("Hello Faheem")


# For Loop

print ("List Iteration")
l = ["Geek" , "For" , "Geek"]
for i in l:
    print(i)


print ("\nTuple Iteration")
t = ["Geek" , "For" , "Geek"]
for i in t:
    print(i)

print ("\nstring Iteration")
s = "Geek"
for i in s:
    print(i)

# Iteration by index
list = ["Geek" , "For" , "Geek"]
for index in range(len(list)):
    print (list[index])

# coutinue and break statement 

for letter in "geekforgreek":
    if letter=='e' or letter=='s':
        continue
    print ('current letter:'), letter
    var = 10


for letter in "geekforgreek":
    if letter=='e' or letter=='s':
        break
    print ('current letter:'), letter


# function
def my_function():
    print("hello, the is my function")

my_function()


def haris():
    print("Useless person")
    print("Qari sab friend ")

haris()

def my_funtion1(country):
    print("I am from " + country)

my_funtion1("pakistan")
my_funtion1("India")
my_funtion1("UK")

def my_funtion2(Father):
    print("Faheem is haris's " + Father)

my_funtion2("Father")


def my_function3(food):
    for i in food:
        print(i)

my_function3("faheem")

furits = ["apple" , "banana" , "cheery" ]
def my_function4(furits):
    for i in furits:
        print(i)

my_function4(furits)


def my_function5(x):
    return 5*x

print(my_function5(5))
print(my_function5(3))


def my_child(child1 , child2 , child3):
    print("my youngest child is " + child1)
    print("my youngest child is " + child3)
    print("my youngest child is " + child2)

my_child("haris ", "qari sab " , "moiz")


# Classes

class my_class():
    x = 5
p1 = my_class()
print(p1.x)

class person():
    def __init__(self , name , age):
        self.name = name 
        self.age = age 


p1 = person("john",36)
print(p1.name )
print(p1.age)
