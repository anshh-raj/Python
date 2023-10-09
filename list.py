my=[1,'t',2,"ansh"]
print(my[1])
print(my[-1])
print(my[1:3])
print(my[::-1])
my[1]="X"
print(my[1])
del my[0]
print(my)

#creating list using for loop

a=[x for x in range(10)]
print(a)
a=[x for x in range(10) if x%2==0]
print(a)

b=[3**i for i in range(10)]
print(b)

# list function
print()
print()
a=[1,3,2,3,3,3,3,3]
a.append(4)
print(a)
a.insert(1,0.5)
print(a)
a.sort()
print(a)

fru=["banana","kiwi","apple"]
fru.sort()
print(fru)

a.pop(0)
print(a)

fru.clear() #this will just clear the list but the list will be there in the memory
print(fru)

del fru #this will remove the list from the memory

a.reverse()
print(a)
print(a.index(2))
print(a.count(3))

print()
#list function

print(len(a))
print(max(a))
print(min(a))
print(sum(a))

n="ansh"
print(list(n))
print()

# loops in list
for element in a:
    print(element*2, end=" ")
print()
for cars in ["swift","mercedes","ferrari"]:
    print(cars,end=" ")
print()
