name="ansh"

para='''this is
a multiline
string
paragraph made using
triple singe quote'''
print(para)

print()

para="""this is
a multiline
string
paragraph made using 
triple double quote"""
print(para)

print()

s="apple"
print(s[0])
print(s[-5])
print(s[4])
print(s[-1])

#slicing
print(s[1:4])
print(s[:4])
print(s[1:])
print(s[0:5:2])
print(s[::-1])
print()
print(s[0:5:-1])
print(s[-1:0:-1])
print(s[-1:-5:-1])
print(s[4:-6:-1])
print(s[6:-5:-1])

a="ans"
b='h raj'
c=a+b
print(c)
c=a*2
print(c)

for ch in a:
    print(ch*2)
print()


#string functions
password="abcdA&"
print(password.isalpha())
print(password.islower())
print(password.isupper())
print(password.upper())
print(password.lower())
print(len(password))

password="345"
print(password.isdigit())

'''
s="   c   "
s.lstrip()
'c   '
s.rstrip()  
'   c'

'''