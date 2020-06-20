'''
print('Hello world!')
print('My name is Isaac') #comment
'''
#this is a comment code

'''
this is a comment
'''
'''
str = 'Hello world'
print(str)

variable = 'My name is Isaac'
print(variable)
'''
var = 64 * 81
print("64 * 81 = ", var)

str = 3 + 5
print("3 + 5 =", str)

var2 = 67 - 17
print("67 - 17 =", var2)

var3 = 19 / 3
print("19 / 3 =", var3)

var4 = var3 * 10
print("var3 * 10 =", var4)

str1 = 5 + 2
print ("5 + 2 =", str1)

str2= str1 + 1
print ("str1 + 1 =", str2)

var5 = 51 % 5 #modulo operator (remainder)
print("51 % 5 =", var5)

var6 = 61 % 6 
print("61 % 6 =", var6)

var7 = 2**2 #exponents -> 2 squared
print("2^2 =", var7)

var8 = 19 // 3 #floor division, takes lower bound
print("19 // 3 =", var8)

var9 = 4**4 
print("result is", var9)

var10 = 20 // 3
print("20 // 3=", var10)

'''
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''

var11 = 19
modresult = var11 % 2
print("modresult is", modresult)

var12 = 21
modresult = var12 % 2
print("modresult is", modresult)

#var12 = var12 + 1
var12 += 1 #"increments" var12 by 1
print(var12)

str10 = 23
modresult = str10 % 2
print ("result is", modresult)

str10 += 1
print(str10)

#string is text variable

#10 -> int
#2.33 -> float
#"word" -> string

str11 = 5 + 2
str11 -= 1 # equivalent str11 = str11 - 1
print(str11)

var100 = 5
print("var100 = 5")

var100 -= 2
print(var100)

var100 *= 10
print(var100)

var100 //= 10
print(var100)

#floor division operator always returns whole number
#regular division always returns floating number
#variable value is always most recent value assigned to it in code (in chronological order)
#code is like a timeline

#true/false -> boolean

#BOOLEAN OPERATORS
bool1 = (5 > 7)
print(bool1)

bool2 = 2 < 1
print(bool2)

bool3 = 3 < 4
print(bool3)

bool4 = (3 <= 3)
print(bool4)

bool5 = (19 >= 11)
print(bool5)

bool6 = (56 == 9) #checks if something is equal to other item
print("56==9 is ", bool6)

bool7 = (11 != 11) #checks if something is NOT equal to other item
print("11!=11 is ", bool7)

bool20 = 2

bool21= 3

bool22 = bool20 == bool21
print(bool22)

#logical operators: and, or, not

bool100 = 5 > 7 #false
bool101 = 4 < 5 #true
print(bool100 and bool101)

#will return true if only BOTH are true
#one false item equates to false overall

bool100 = 5 > 7 #false
bool101 = 4 < 5 #true
print(bool100 or bool101)

#will return true if EITHER is true

print("not(bool100) is",not(bool100))

print("Hello World")
print("Isaac")

print("Hello World")

bool1 = 2 < 3
print(bool1)