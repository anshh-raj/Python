a=list(range(10))
print(a)
a=list(range(5,10))
print(a)
a=list(range(6,10,2))
print(a)

for x in range(10):
    print(2*x)

for x in range(10):
    print(2*x, end=", ")

print()

a=["ansh","akash","shivam"]
for x in a:
    print(x*3)

n=5
while n>=0:
    print(n)
    n-=1
print()
 
for i in range(10):
    if i==6:
        break
    print(i)

print()

for i in range(10):
    if i==8:
        continue
    print(i)