#function this is the syntax
def Isaac(): 
    print("Isaac")
Isaac()

#for loop JS (Java Script)
# for(i=0; i<3; i++)
# print("Name")

#https://www.w3schools.com/python/python_for_loops.asp
#this first exmaple

# for x in friends:
    # print(x)

#how to create a list in Python 
# friends = ["Lexi", "Mitch", "Andy", "Colton"]

#NameError: name 'friends' is not defined

friends = ["Lexi", "Mitch", "Andy", "Colton"]
for x in friends: 
    print(x)

#this is the result: 
#Isaac
#Lexi
#Mitch
#Andy
#Colton

# for x in "Cartagena123!"
# print(x)

#syntax error if don't indent "print" 
#SyntaxError: invalid syntax

for x in "Cartagena123!":
    print(x)

#this is called looping through a string
#even strings are iterable objects, they contain a sequence of characters

#this is the result:
#C
# a
# r
# t
# a
# g
# e
# n
# a
# 1
# 2
# 3
# !

#for loops print strings in a list
#looping through a string prints all characters in that string because it is an iterable object; prints characters vertically
#what is a character? any letter, number, or special punctuation 
#http://cs.smu.ca/~porter/csc/ref/ascii.html

friends = ["Lexi", "Mitch", "Helen", "Isabelle"]
#iterator: friends, iterable: y
for y in friends:
    print(y)
#In Python and many other programming languages, a single equal mark is used to assign a value to a variable, whereas two consecutive equal marks is used to check whether 2 expressions give the same value .

# = is an assignment operator

# == is an equality operator

    if y == "Helen":
        break

#An iterator is an object representing a stream of data. It does the iterating over an iterable. You can use an iterator to get the next value or to loop over it. Once, you loop over an iterator, there are no more stream values.

#still completes break string but doesn't complete one after that 

#how to do git pushing
#make sure to save document before
#step one click add
#step two click commit
#step three click push

