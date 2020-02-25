print ("Lambda Expression, Map and Filter functions")

def square(num):
	return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
	print (item)

##or

print (list(map(square, my_nums)))

##or with lambda

print(list (map (lambda num: num **2, my_nums)))

print ('---------------------------------------------------------------------')

def splicer (mystring):
	if len(mystring)%2 == 0:
		return 'EVEN'
	else:
		return 'ODD'

names = ['Andy', 'eve', 'sally']
print(list(map(splicer, names)))

print ('---------------------------------------------------------------------')

def check_even(num):
	return num%2 == 0

mynums = [1,2,3,4,5]
filter(check_even, mynums)

print(list(filter(check_even, mynums)))

for i in filter(check_even, mynums):
	print (i)

print ('---------------------------------------------------------------------')

def square(num):
	result = num ** 2
	return result

print ('square of number is',square(3))

square = lambda num: num ** 2
print ('square with lambda function is', square(5))	

print ('---------------------------------------------------------------------')

