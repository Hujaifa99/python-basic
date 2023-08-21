import re
import urllib.request
a = 'charlie chhaplin coa and the chocolate factory'
b = 'ayushi.jain@gmail.com'
c = 'hello'
d = 'xyz,yz,xxxxyyyyyyzz,xxzzy,zyz,xxy,xyzxyz'

# / to specify special charecter
regex = re.search(r'\.',b)
print(regex)
regex = re.findall(r'\.',b)
print(regex)
# [] a set of charecter
regex = re.findall(r'[a]',b)
print(regex)
# ^ start of string
regex = re.search(r'^charlie',a)
print(regex)
# $ start of string
regex = re.search(r'factory$',a)
print(regex)
# . any char except new line
regex = re.findall(r'c.a',a)
print(regex)
# | OR Operator
regex = re.findall(r'cha|fac',a)
print(regex)
# ? 0 or 1 occurance
regex = re.findall(r'ch?a',a)
print(regex)
# * 0 or more occurance
regex = re.findall(r'ch*a',a)
print(regex)
# + 1 or more occurance
regex = re.findall(r'xy+z',d)
print(regex)
# {star,end} number of occurance
regex = re.findall(r'x{2,4}',d)
print(regex)
# () groups an expression
regex = re.findall(r'(x|z)yz',d)
print(regex)

#\A begining of the string
a = 'harry potter'
regex = re.search(r'\Ahar',a)
print(regex)
# \b(str) (str)\b for start of end
regex = re.search(r'ter\b',a)
print(regex)
# \B opposite of b \b
regex = re.search(r'\Ber',a)
print(regex)
#\d for digits
a = 'harry1 potter23@ s+a'
regex = re.findall(r'\d',a)
print(regex)
#\D not digit
regex = re.findall(r'\D',a)
print(regex)
#\s for space
regex = re.findall(r'\s',a)
print(regex)
#\s for no space
regex = re.findall(r'\S',a)
print(regex)
#\w any alpha numberic charecter
regex = re.findall(r'\w',a)
print(regex)
#\W non any alpha numberic charecter
regex = re.findall(r'\W',a)
print(regex)
#(str)\Z matches ending
regex = re.search(r'a\Z',a)
print(regex)

# [] -> abc (a or b or c) a-z (a to z) ^abc(anything except a or b or c) $,/,# works
a = 'charlie and the chocolate factory'
match = re.findall(r'[atx]',a)
print(match)
match = re.findall(r'[a-c]',a)
print(match)
match = re.findall(r'[^act\s]',a)
print(match)
match = re.findall(r'[a-c][a-c]',a)
print(match)

#findall find every occurance
a = 'John has scored 89 marks Lisa has scored 90 marks David has scored 70 marks'
print(re.findall('\d+',a))
print(re.findall('[A-Z][a-z]*',a))
#search to find 1 occurance (first)
print(re.search('[A-Z][a-z]*',a))
#complie creates a pattern object from string
p = re.compile(r'[0-9]+')
print(re.findall(p,a))
#split split string on pattern match
print(re.split('\d+',a))
#sub replaces a pattern with a string
print(re.sub('\d+', '<number>', a))
#subn replaces a pattern with a string and counts the the number of replace
print(re.subn('\d+', '<number>', a))
#exxcape puts \ before space
print(re.escape(a))

#Match object contains all information about search
a = 'John has scored 98 mark'
match = re.search(r'\d+',a)
print(match)
print(match.re) #which regular expression is used
print(match.string) #the given string
print(match.start()) #where match starts and end
print(match.end())
print(match.span()) # start and end
print(match.group()) #What has matched multiple match possible

#match phone number
phn = '015-337-3104'
if re.search('01\d-\d{3}-\d{4}',phn):
    print('it is a valid number')
else:
    print('not a valid number')

#match email
email = 'john78@gmail.com john@.com dacid.989@yahoo.com'
print(re.findall(r'[\w._%]{0,20}@[\w-]+.com',email))

#Web scrapping
url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'
a = urllib.request.urlopen(url) #open url
html = a.read()
htmlstr = html.decode()
#Matches number
phn = re.findall('\(\d{3}\) \d{3}-\d{4}', htmlstr)
for i in phn:
    print(i)


