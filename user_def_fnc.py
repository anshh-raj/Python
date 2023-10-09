def greet(name, dish="cake"):
    print("good morning",name)
    print("please eat",dish)


greet("ansh","pasta")
greet(5.667,"a")
greet("akash")

def sum_of_list(a):
    print('calculating...')
    return sum(a)

marks=[45,16,87,98,45]
print(sum_of_list(marks))

def greets(a):
    for x in a:
        print("hello",x)

names=["ansh","akash","devanshi","aryan","nobita"]
greets(names)