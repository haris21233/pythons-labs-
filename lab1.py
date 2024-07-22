
# comments  in python " # "

x=1
# My name is Haris
if x > 0:
    print("Hello,World!")


# input and output

y = input("Enter a number: ")
print(y)

# must give indentation 

print("Semester 1")
print("Semester 2")

# in a single line 
print("Semester 1");print("Semester 1")

# if we didnot give indentation it take an error
z = 1
if z > 0:
    print("My name is Faheem ")

# type of the variable 

a = 123
print(type (a))

b = 1.23
print(type (b))

# complex number 

c = complex(1 , 2)
print(type(c))
print(c)

d = 1 + 3j
print(type(d))

# string 
str1 = "Hello, I'am Faheem "
print(str1)

print("This is a (\\) tab use ")
print("This is a \t tab use ")
print("This is a \'hello \' tab use ")
print("This is a \n tab use ")
print("This is a \"Hello\" tab use ")


# string indicate accessing string element 

str1 = "Mian Faheem Hussain"
print(str1[1]) 
print(str1[12]) 
print(str1[14]) 
print(str1[5]) 
print(str1[-13]) 

# Creating list
my_list1 = [3, 23 , 332 , 2332] 
print(my_list1)
my_list2 = ['red', 'blue', 'green' , 'yellow'] 
print(my_list2)
my_list3 = ['red', 23 , 332 , 2332] 
print(my_list3)

my_list4 =[]
print(my_list4)


#indecate the list 
colour_list = ['red', 'blue', 'green' , 'yellow'] 
print(colour_list[1])
print(colour_list[1], colour_list[2])
print(colour_list[-1], colour_list[-2])
print(colour_list[1], colour_list[-2])
print(colour_list[:])



s = input("Enter a 1st Number: ")
t = input("Enter a 2nd number ")

print(s)
print(t)

if s>t:
    print("1st number is greater ")
else:
    print("2nd number is greater")