f=open('data_folder/data.txt', 'r') #by default it is always read mode
# '+' mode can be used for both read and write

print(f.readline())
print(f.readline())
print(f.readline())

print("xxxx")

for line in f:
    print(line)


f.close()

'''
here it is not necessary that the file will always close for eg
when there will be error in between the program the f.close()
will never get executed hence its very risky

'''