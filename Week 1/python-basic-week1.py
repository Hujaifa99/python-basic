#Operator preference
print(2 * (2+2))
#Basic numerical operation, Division returns a float value
print(20/2)
#Negative number
print(-7+2)
#even if one operator is float, the result is float
print(4 + 1.65)
#power operation 2^3
print(2 ** 3)
#Use / for division (quotient), % for modulo (remainder) and // for floor division (not rounding up but using floor on the result)
print(10/3 , 10%3 , 10//3)


#Basic String
string = 'My name is Hujaifa'
print(string)
#If string contains special charecters (',",\ etc) use \ before them
print('He\'ll go to school but she\'ll not') 
# \n for new line, \t for tab, \v for vertical tab
print('I \nam\tHujaifa\vIslam')

#input() for taking input and print() for printing output
x = input('Enter any number: ')
print(f'x = {x}')

#String Concatenation using + (string + string)
print('My '+'name '+'is '+'Hujaifa')
#String Repetition using * (string * int)
print(5 * '1')
#String Formating
print('{2}{0}{0}{1}'.format('a','b','c'))
print('{a}{b}{a}{b}'.format(a='1',b='2'))
#String join ( "separator".join( [list] ) )
print(' and '.join(['a','b','c']))
#String replace ( 'original string'.replace('sub string to be replaced','sub string to replace with') )
print('My name is Hujaifa'.replace('My','Your'))
#String check using startwith and endswith
print('My name is Hujaifa.'.startswith('My'))
print('My name is Hujaifa.'.endswith('My'))
#convert string to upper letter or lower letter using upper() and lower()
print('i am hujaifa'.upper())
print('I AM A MAN'.lower())
#split a string using split()
print('a,b,c,d,e,f,g'.split(','))

#Type Conversion str to int and float to int
print(int('123') , int(123.123))
#int to float str to float
print(float(4) , float('5.00'))
#int to str float to str
print(str(1),str(2.00))

#Variable starts with lower/upper letter and _
#Variable cant starts with numbers or special charecter
#Variables are case sensitive a != A
#reserved keywords (if,else,and,or) cant be used on a variable

#Inplace operator (+,-,*,/ before =)
a = 'a'
a+='b'
a*=2
print(a)

#Boolean Value = True & False
#Any python comparism returns a bollean value
print(1==1)
print(7<2)
print('hujaifa' != 'islam')
#Boolean Operator = (and,or,not)
#is used to combine multiple condition in if statement
a = 5
if a == 5 or a == 3:
    print('a = 5 or 3')
if a == 5 and a == 3:
    print('a = 5 and 3')
print(not True)  

#if (condition):
    #statement
#Statement executes only if the condition returns true
a = 'abcd'
if a == 'abcd':
    print('String is abcd')
    if a.startswith('b'):
        print('String stars with b')
#if (condition):
    #statement 1
#else :
    #statement 2
#Statement 1 executes if the condition is true and if not true then executes statement 2
x = 10
if x>15:
    print('Greater than 15')
else:
    print('Less than 15')
#If and Else can be nested

#ternary operator
a = 100
b = 200 if (a>50 and a<150) else 300
print(b)
#if condition true b=200 and if condition false b=300

#Operator Precedence from left to right
#(), **, */%, +-, >> <<, &, ^, > < >= <=, == != <>, = += -= *= /=, not or and

#while (condition):
    #Statement
#the statement keep executing until the condition is false
#if the condition never becomes false the statement executes infinite times
i = 0
while i<5:
    print(i)
    i+=1
#break statement terminates the loop
i = 0
while True:
    print(i)
    i+=1
    if i==3:
        break

#continue statement terminates the loop for that iteration
i = 0
while True:
   i += 1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking")
      break
   print(i)

#List works like array so it can be indexed
#List can contain values of different data type
#Python sees strings as a list of charecters
x = [1,2.0,'a','b',52]
print(x[2],x[3],x[1])
x = 'abcdefg'
print(x[2],x[3],x[1])
#List concatenation (+) repetition (*)
x = [1,2,3]
print(x + [4,5,6])
print(x * 2)
#Search list using in
print(1 in x)
print(5 in x)
print(5 not in x)
#append() to insert element at last position
#insert() to insert element at specific position
x.append(4)
x.insert(0,0)
print(x)
#index(element) to find the location of an element
print(x.index(3))
#count(element) to find the number of occurance in the list
#max(),min() to find maximum and minimum
#len() to find the length
nums = [1,2,3,1,1,2,5,5]
print(nums.count(1) , max(nums) , min(nums) , len(nums))

#Range to create automatic list but have to convert into list
#range(start , end+1 , interval)
print(list(range(0,100,10)))
#interval can be negative
print(list(range(10, 0, -1)))

#For Loop
for elements in nums:
    print(elements)
for i in range(3):
    print(i)
for letters in 'hujaifa':
    print(letters)

#Data type None
def func(x = None):
    if x is not None:
        return x
    else:
        return 0
print(func(5))
print(func())

#dictional {
#    key1:value1,
#    key2:value2,
# }
#keys can be used to obtain any value
#keys can be any immutable object (so not list)
#value can be any type of object
mydict = {
    'A' : [1,2,3],
    0 : 'abc',
    5.3 : 2
}
print(mydict.keys() , mydict.values())
print(mydict['A'], mydict[0], mydict[5.3])
mydict['New'] = [0,0,0]
print(mydict)
#Find keys using in operator
print('A' in mydict)
print('New' in mydict)
print(53 in mydict)
#dict.get(key) to retrive value or return None if key not in dict
print(mydict.get(0))
print(mydict.get(1,'1 not in dict'))

#Tuple is exactly like list but it's immutable so values can't be changed
#(element1,element2,element3) to initilize tuple
#elements can be any data type
x = (0,1,{'A':111},3)
print(x[2]['A'])
x = (0,1)
a , b = x
print(a,b)
a,*b,c,d = [1,2,3,4,5,6,7,8,9]
print(a , b,c,d)
# * indicates everything in between

#List Slicing
x = [0,1,2,3,4,5,6,7,8,9,10]
print(x[4:8])
print(x[5:])
print(x[:7])
print(x[2::2])
print(x[-7:-10:-1])
#Negative index indicated elements from the last
#Last element is -1
#List sum()
print(sum(x))
#List Comprehension
y = [i for i in x if i%2==0]
#iterate through list if the element fullfill the condition it appends into list
print(y)
matrix_2d = [[1, 2, 3],[4, 5, 6]]
matrix_1d = [num for row in matrix_2d for num in row]
print(matrix_1d)

vowels = 'aeiou'
sen = 'i am a student.my name is hujifa'
filtered = ''.join( [letter for letter in sen if letter not in vowels] )
print(filtered)

#Dictionary Comprehension
class_rank = [1,2,3,4]
class_name = ['abul','rahim','karim','faysal']
rank_dict = {class_rank[i] : class_name[i] for i in range(len(class_name))}
print(rank_dict)
