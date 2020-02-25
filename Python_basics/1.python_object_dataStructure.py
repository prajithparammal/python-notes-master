#Numbers: Store numerical infromation and come in two forms: Integers and Floating Point
#Strings: Ordered sequence of characters
#Lists: Ordered sequence of objects (mutable)
#Tuples: Ordered sequence of objects (immuntable)
#Dictionaries: Key-value pairing that is unordered

print("----------------------------------------------")
a = 5
a = a + a
print (a)

print("----------------------------------------------")
print("Hello \nworld")
print('hello \tworld')

print("----------------------------------------------")

print ('Indexing and slicing of Strings')

myname="prajith"
print(myname)
print("To print first character", myname[0])
print("To Print last character", myname[-1])

mystring="abcdefghijklmnopqrstuvwxyz"
print (mystring)
print ("To print letter from c and all the way to end", mystring[2:])
print ("To print letter upto d, not including d", mystring[:3])
print ("To print only def", mystring[3:6])
print ("To print all letters with a step size of 2", mystring[::2])
print ("To reverse entire string from z to a", mystring[::-1])

print("----------------------------------------------")

print ("String properties are immuntable and string methods")

name = "Sam"
last_letter = name[1:]
print ("Change Sam to Pam with concatenation", 'P' + name[1:])
print ("Change Sam to Pam with concatenation", 'P' + last_letter)

wife = "Nimmi"
print ("Adding Nimmi with Prajith", wife + 'Prajith')

name = "Prajith"
print ("Printing Prajith 10 times", name * 10)

x = "Hello Prajith"
print ("x in upper case using build in string method, which is essentially a function within object", x.upper())

print ("x into list of strings", x.split())

ip = "192.168.10.1"
print ("slip ip with delimited of dot and convert into list", ip.split('.'))

print ("Two print formatting methods are .format() and f-strings")

print ('This is a string {}'.format('INSERTED'))
print ('My name is {}'.format('Prajith'))
print ('Main public cloud providers are {} {} {}'.format('GCP','AZURE','AWS'))
print ('Main public cloud providers are {2} {1} {0}'.format('GCP','AZURE','AWS'))
print ('Main public cloud providers are {a} {b} {c}'.format(a='GCP',b='AZURE',c='AWS'))

result=100/777
print ("This result was {}".format(result))
print ("This result was {r}".format(r=result))
print ('The result with float formatting with .format method  value:width.precision f fromat {r:1.3f}'.format(r=result))

name = "Jose"
age = 3
print (f'Hello, his name is {name}')
print (f'{name} is {age} years old')

print("----------------------------------------------")

print ('List in python')
my_list = ['string',2,3.0]
mylist=['one','two','three']
mylist1=['four','five']
mynewlist=mylist+mylist1

print (f'mynewlist value is {mynewlist}')

print ('To grab element at index 0 is {}'.format(mylist[0]))
print ('To grab element at index 0 is', mylist[0])
print (f'To grab element at index 0 is {mylist[0]}')

print ("concatenate mylist and mylist1", mylist+mylist1)
print (f'Concatenate mylist and mylist1 {mylist+mylist1}')
print ("concatenate mylist and mylist1 {}".format(mylist+mylist1))

mynewlist[0]='ONE'
print ("mynewlist is now {}".format(mynewlist))
mynewlist.append('six')
print ("mynewlist is now {}".format(mynewlist))
mynewlist.pop()
print (f'remove last element in mynewlist {mynewlist}')
mynewlist.pop(0)
print (f'remove first element at index 0 of mynewlist {mynewlist}')

numlist = [6,1,3,7,2,0]
alphalist = ['f','e','h','m','q','i']
print (f'numlist is {numlist}')
numlist.sort() ## or sorted(numlist)
print (f'numlist after sorting {numlist}')
numlist.reverse()
print (f'reverse version of list {numlist}')

alphalist.sort()
print (f'alphalist after sorting is {alphalist}')
alphalist.reverse()
print (f'reverse version of alphalist is {alphalist}')

print("----------------------------------------------")

print ('Dictionaries in python')

my_dict = {'key1':'value1','key2':'value2'}
print (f"value of key1 is {my_dict['key1']}")

prices_lookup = {'apple':3.00,'orange':4.5,'milk':5.90}
print ("Price of apple is {}".format(prices_lookup['apple']))

my_dict = {'key1':['a','b','c']}
print ("Print third element of list in caps")
print (f"Upper case of 3rd element in list is {my_dict['key1'][2].upper()}")

d={'k1':100,'k2':200,'k3':300}
print (f'{d.keys()}')
print (f'{d.values()}')
print (f'{d.items()}')
d['k1']=400
print (f"{d['k1']}")
d['k4']=500
print ("d value now is",d)

print("----------------------------------------------")
print ('Tuples in python')
t = (1,2,3) # Tuple
mylist = [1,2,3]  # list

t = ('a','a','a','b','c')
print (f"One of times a occured is {t.count('a')}")
print (f"Very first time a appread on at index {t.index('a')}")

print("----------------------------------------------")

print ('sets in python, which is unordered collection of unqiue objects')
myset = set()
myset.add(1)
print ("myset value is", myset)
myset.add(2)
print ("myset value is", myset)

mylist=[1,1,1,1,2,2,2,2,4,4,4,4,3,3,3]
newlist=set(mylist)
print("mylist values now is", newlist)
print("----------------------------------------------")

print ('Booleans in python')
b = None

print("----------------------------------------------")
print ('I/O with basic Files in python')
myfile = open('myfile.txt')
print ("myfile output is", myfile.read())
myfile.seek(0)
print ("myfile output is", myfile.read())
myfile.seek(0)
contents = myfile.read()
print ("myfile out is", contents)
myfile.seek(0)
print ("print each lines as list in myfile", myfile.readlines())
myfile.close()

with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()
	print ("Contents of my_new_file is", contents)

with open('myfile.txt', mode='r') as f:
	print (f.read())

with open('myfile.txt', mode='a') as f:
	f.write('\nthis is the fourth line')

with open('myfile.txt', mode='r') as f:
	print (f.read())

with open ('prajith.txt','w') as f:
	f.write('\n I created the file')

with open('prajith.txt','r') as f:
	print (f.read())

print("----------------------------------------------")


d = {'k1':[{'nest_key':['This is deep',['hello']]}]}

print ("printing hello from d", d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print ("Printing hello from d", d['k1'][2]['k2'][1]['tough'][2][0])