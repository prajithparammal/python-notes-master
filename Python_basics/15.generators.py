'''
Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.
'''

def craete_cubes(n):
    result =[]
    for x in range (n):
        result.append(x**3)
        return result

## Better way

def craete_cubes(n):
    for x in range (n):
        yield x**3

for x in craete_cubes(10):
    print(x)

######################
def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)
###################### normal way without yield
def gen_fibon(n):
    a = 1
    b = 1
    output =[]

    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

######################

s = 'hello'
for letter in s:
    print(letter)
######################
s_iter = iter(s)
next(s_iter)
next(s_iter)
######################

