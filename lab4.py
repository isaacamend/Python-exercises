#June 27, 2020 PYTHON lesson
#Python data types

name = "Isaac" #str
int = 5 #int
print(int)
#not advisable to write int, technically OK but might interact negatively with Java

x = 1.3 
y = 2.5 

#float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1 + 2j #j is an imaginary number
#complex 

colors = ["red", "blue", "violet"]
print(colors)

#list = A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

#tuple = A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#You can access tuple items by referring to the index number, inside square brackets:

 #           0          1        2
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

names = {"Isaac", "Lexi", "Helen"}
print(names)

#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

for x in names:
    print(x)

#as a result it's listed like this: 
#Lexi it was 1 but now it is 0
#Helen
#Isaac

icecream = {"chocolate", "vanilla", "strawberry"}
print("strawberry" in icecream)

#result is True 

bool1 = 5
bool2 = 10
print(bool1 > bool2)

bool3 = bool1 + bool2
bool4 = 12
print(bool3 + bool1 > bool4)

x = 2
y = 3
z = 5
a = (x > y) > z 
#False
print(a)
#why does a boolean get compared to an integer? 

