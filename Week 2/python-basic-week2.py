#Basic function
def make_sum(x,y):
    return x+y
print(make_sum(10,15))

# * indicates that the argument is tuple so id we use * in
#parameter, we can give multiple (variable size) input
def make_sum2(*args):
    sum = 0
    for num in args:
        sum+=num
    return sum
#Return statement returns the sum to total variable
total = make_sum2(1,2,3,4,5,6,7,8,9)
print(total)

# ** indicates the argument is a named parameter so when calling we
#have to give name to the arguments. this argument works like a dictionary
def make_dict(**kwargs):
    print(type(kwargs))
    print(kwargs)
make_dict(a=1,b=2,c=3)

#Combination of all three
def print_all(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
print_all(1,2,3,4,5,a=6,b=7,c=8)

#Function as an argument
def add_excla(text):
    return text + ' !!!'
def add_greet(text,func):
    return 'Hey ' + func(text)
print(add_greet('Beautiful', add_excla))

#Lambda Function 
x = lambda a : a*2
print(x(5))
"""
Module is a collection of code which can contain various func, attribute or variables
that we can use. To use a module first we have to import it and then we can use it.
Tensorflow, NumPy, Pandas, random etc are all module/library. Some module are built-in python
and others have to be downloaded using pip command in terminal
"""

"""
Exception Handling
use try whenever there is a change of being a exception then use except to show 
proper error message and the programme doesnt stop executing
try:
    Statement
except:
    Statement (executed only when there is an exception)
finally:
    Statement (Executed after try & except but will execute for sure)
"""
try:
    print(5/0)
    print('my' + 5)
except ZeroDivisionError:
    print('Division by zero')
except TypeError:
    print('Type Error')
except:
    print('There was an error')
    #raise can be used in exception block to identify the type of exception
    raise
#even if expect block has an error finally will execute
finally:
    print('This will run for sure')

# raise statement is used to create an exception
#raise Exception('An error')
#print(1)

#Assertion is used to immedietly check a condition. It's usually used to check
#weather the given input in a function is correct or not.If it isn't corrent 
# assetion raises a AssertionError
# assert (condition), statement(if False)
def even_multiplier(x):
    assert x%2==0, 'Please enter an even number'
    print(2*x)
even_multiplier(4)

'''
File Handling
open(path,mode) to open file
mode = 'w'(write), 'r'(read), 'a'(append), 'wb'(open in binary mode)
close() to close the file
'''
#fp.read() to read entire text,readlines to store each line in a list
fp = open('/media/nsl45/DATA-DISK/hujaifa/study/Week 2/file.txt','r')
print(fp.read())
fp.close()

fp = open('/media/nsl45/DATA-DISK/hujaifa/study/Week 2/file.txt','r')
print(fp.readlines())
fp.close()
#for loop on file reads each line
fp = open('/media/nsl45/DATA-DISK/hujaifa/study/Week 2/file.txt','r')
for line in fp:
    print(line)
fp.close()
#write() to write on a file if the file was opened in w mode then
#the file will be overwritten and if mode was a then the writting 
#will be appended on the end
#fp = open('/media/nsl45/DATA-DISK/hujaifa/study/Week 2/file.txt','a')
#p.write('This is written by programme')
#fp.close()

#Always use with when using open(),it automatically destroys all temporary
#variable so we don't need to write close()
with open('/media/nsl45/DATA-DISK/hujaifa/study/Week 2/file.txt','r') as fp:
    print(fp.close())


"""
PEP (Python Enhancement Proposal) is a guideline proposed by python developer experts to ensure python codes 
are readble, clean and understandable. Following PEP makes understanding the code easier for others
"""

"""
if __name__ == "__main__":
    Statement1
Here Statement1 will be executed by default only if that script is run. But if this script is imported as a module
for another script then __name__ will not be equal to __main__ and Statement1 won't be executed
"""

"""
# -*- coding: utf-8 -*-
the above line is used in python to tell the interpreter the code has to be decoded using utf-8. Python3
don't require this command as it's default encoding is utf-8
"""

"""
#! /usr/bin/env python3
The above line is used to tell python interpreter which enviroment to use.
"""

"""
CPython is a python interpreter where the formal language python is implemented using C.
Jython is a python interpreter where the formal language python is implemented using Java.
Python Source Code (.py) -> Compiler -> Bytecode (.pyc) -> Interpreter (VM/CPython/Jython) -> Output (Hello World!)
"""