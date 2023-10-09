class person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(self.name,self.id)

p1=person("ansh",25081)
p1.display()

class emp(person):
    def print(self):
        print("emp class called")

p2=emp("raj",222)
p2.display()
p2.print()