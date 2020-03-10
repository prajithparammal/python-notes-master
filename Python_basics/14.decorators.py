def hello(name='Jose'):
    print('the hello() function has been executed')
    def greet():
        return '\t THis is the greet () func inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

#    print(greet())
#    print(welcome())
#    print('This is the end of the hello function')

    print ("Im going to return a function!!")
    if name == 'Jose':
        return greet
    else:
        return welcome

my_new_func = hello()
print(my_new_func())


my_new_func = hello('Prajith')
print(my_new_func())

print('#############################################################')

def cool():
    def super_cool():
        return 'Im very cool'
    return super_cool

some_func = cool()
print(some_func())

print('#############################################################')

def hello():
    return 'Hi Jose!!'

def other (some_def_func):
    print('other code runs here!!')
    print(some_def_func())

other(hello)

print('#############################################################')

def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before the original function')
        original_func()
        print('some extra code, after the orginal function')
    return wrap_func()

def func_needs_decorator():
    print("I want to be decoreated!!!")



decorated_func = new_decorator(func_needs_decorator)
decorated_func()

@new_decorator
def func_needs_decorator():
    print("I want to be decoreated!!!")

func_needs_decorator()

print('########################################################')


