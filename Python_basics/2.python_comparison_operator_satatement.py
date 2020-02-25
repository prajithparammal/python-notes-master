print ("Python comparison operator")
print ("comparison result in True or False :", 1<2 and 2<3)
print ("comparison result in True or False :", 1==1 or 2==3)
print ("comparison result in True or False :", not 1==1)

print("----------------------------------------------")

print ("Python satement if, elif and else statement")

if 3>2:
	print ('Its true')

hungry = False
if hungry:
	print ('FEED ME!!')
else:
	print ("Im not hungry!!")


hungry = True
if hungry:
	print ('FEED ME!!')
else:
	print ("Im not hungry!!")


loc='Bank'
if loc == 'car':
	print ('cars are cool!!')
elif loc == 'Bank':
	print ('Bank is at the junction')
elif loc == 'store':
	print ('store is behind!!')
else:
	print ("I dont know much!!")

print("----------------------------------------------")

print ("Python for loop")

listtest = [1,2,3,4]
for i in listtest:
	print (i)


numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers:
	if i % 2 ==0:
		print (f'{i} is even number')
	else:
		print (f'{i} is Odd number')


## Tuple unpacking

mylist =[(1,2),(3,4),(5,6),(7,8),(9,10)]
for a,b in mylist:
	print (a)

## for loop with dictionaries

d = {'k1':"prajith",'k2':"Nimmi", 'k3':"Aarohi", 'k4':"Arush"}
for i in d.items():
	print (i)

d = {'k1':"prajith",'k2':"Nimmi", 'k3':"Aarohi", 'k4':"Arush"}
for i,j in d.items():
	print (j)

d = {'k1':"prajith",'k2':"Nimmi", 'k3':"Aarohi", 'k4':"Arush"}
for i in d.values():
	print (i)

d = {'k1':"prajith",'k2':"Nimmi", 'k3':"Aarohi", 'k4':"Arush"}
for i in d.keys():
	print (i)

print("----------------------------------------------")

print ("Python while loop")

x=0
while x < 5:
	print (f'current value of x is {x}')
	x=x+1 # x+=1
else:
	print ('x is not less than 5') 

print("----------------------------------------------")

print ('break, continue, pass in loops')

x =[1,2,3]
for i in x:
	pass  # do nothing at all. Programmer use as a place holder to avoid syntax error and for future code addition.
print ('end of my script')

mystring = 'sammy'
for letter in mystring:
	if letter == 'a':  ## a will be ignored from printing and continued
		continue
	print (letter)

mystring = 'sammy'
for letter in mystring:
	if letter == 'a':  ## a will be ignored from printing and continued
		break
	print (letter)

x = 0
while x < 5:
	if x == 3:
		break
	print (x)
	x+=1
print("----------------------------------------------")

print ('useful operator in python')

for i in range (10):
	print (i)

for i in range (3,10):
	print (i)

for i in range (1,10,2):
	print (i)

index_count = 0
for letter in 'abcd':
	print ('At index {} the letter is {}'.format(index_count,letter))
	index_count+=1

word ='abcd'
for i in enumerate(word):
	print (i) ## we get back tuple with index number and letter

word ='abcd'
for index,letter in enumerate(word):
	print (index) ## we get back tuple with index number and letter
	print (letter)
	print ('\n')


mylist1 = list(range(1,5))
mylist2 = ['a','b','c']
print ('casting as list',list(zip(mylist1,mylist2)))
for item in zip (mylist1,mylist2):
	print (item) ## returns tuples with mylist1 and mylist2

'x' in [1,2,3] ## will give False
'x' in ['x',2,3] ## will give True

mylist = list(range(1,5))
print ('lowest number in mylist is', min(mylist))
print ('lowest number in mylist is', max(mylist))

from random import shuffle ## importing shuffle function from build in random library
mylist = list(range(1,10))
shuffle(mylist)
print ('shuffled list is',mylist)

from random import randint
print ('print any random integer',randint(0,100))

#result = input('what is your name:')
#print('your name is',result)

print("----------------------------------------------")

print ('list comprehensions in python')

mystring = 'hello'
mylist = [letter for letter in mystring] ## hello will be converted as list of letters
print (mylist)

mylist = [x for x in 'world']
print (mylist)

mylist = [num**2 for num in range (0,11)]
print (mylist)

mylist = [x for x in range (0,11) if x%2 ==0]
print (mylist)

celcius = [0,10,20,30]
fahrenheit = [((9/5)*x +32) for x in celcius]
print (fahrenheit)

result = [x if x%2 ==0 else 'ODD' for x in range (0,11)]
print (result)

mylist = []
for x in [2,4,6]:
	for y  in [1,10,1000]:
		mylist.append (x*y)
print (mylist)
##another way of doing it
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print (mylist)

print("----------------------------------------------")





