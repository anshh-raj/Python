#strings and tuples are immutable whereas list are mutable

# a="ansh"
# a[0]='b' #throws an error

a=['a',5,'d8',7]
a[1]=3
print(a)

# a=('a',5,'d8',7)
# a[1]=3 #throws an error

# tuple creation

a=('a','n','s','h',8,1)
print(a[3])

#rest all fnc and operation same as list

n="ansh"
print(tuple(n))