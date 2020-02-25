print ("Methods in python")
mylist = [1,2,3]
mylist.append(4)
print ('my appended list',mylist)
mylist.pop()
print ('my popout list', mylist)

print ("-----------------------------------------------------------------")
print ('Function: clean repeatable code')

def add_fuction(num1, num2):
	'''
	DOCSTRING: Adding two numbers 
	INPUT: Give two number for addition
	RESULT: result of addition of two numbers
	'''
	return num1+num2

result = add_fuction(2,4)
print (result)

help (add_fuction)
print ("-----------------------------------------------------------------")

def say_hello():
	print ('hello')
say_hello()

print ("-----------------------------------------------------------------")

def say_hello (name='Prajith'):
	print ('hello\t'+ name)

say_hello()
say_hello('Nimmi')

print ("-----------------------------------------------------------------")

def say_hello (name='Prajith'):
	return 'Hai\t' + name

result = say_hello ('Rajish')
print (result)

print ("-----------------------------------------------------------------")

def dog_check(mystring):
	return 'dog' in mystring.lower()

result = dog_check ('Dog in my string')
print (result)

print ("-----------------------------------------------------------------")

#PIG LATIN
# if words start with a vowel, add 'ay' to end
# if words doesnt not start with vowel, put first letter at the end, then add 'ay'
# word ----> ordway
# apple ---> appleay

def piglatin(word):
	first_letter=word[0]
	
	if first_letter in 'aeiou':
		pig_word= word + 'ay'
	else:
		pig_word=word [1:] + first_letter + 'ay'

	return pig_word

result=piglatin('bpple')
print (result)

print ("-----------------------------------------------------------------")

print ('*args and **kwargs')

def myfunc(a,b):
	return sum((a,b)) * 0.05

result = myfunc (50,50)
print (result)

#or

def myfunc(*args):
	return sum (args) * 0.05

result = myfunc (40,60)
print (result)

print ("-----------------------------------------------------------------")

def myfunc (**kwargs):
	if 'fruit' in kwargs:
		print ('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print ('I didnt find any fruit here')

myfunc (fruiti='apple', veggie = 'lettuce')

print ("-----------------------------------------------------------------")


def myfunc(*args, **kwargs):
	print ('I would like {} {}'.format(args[0], kwargs['food']))

myfunc (10,20,30,fruit='oranges',food='eggs',animal='dogs')

print ("-----------------------------------------------------------------")




