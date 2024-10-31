class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mobe(self):
        print("simon")
        return "hi"
    
class inherit(point):
    pass

point1=point(2,2)
point2=inherit(2,2)
print(point1.mobe())
print(point2.mobe())

class details:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"my name is {self.name} and i am {self.age} year old")

me=details("simon",20) 

class myname:
    def __init__(self,first,second):
        self.first=first
        self.second=second
        print(f"my name is {self.first} {self.second}")

class myname2(myname):
      pass

try:
 name=myname("simon","njoroge")
 name2=myname2("simon","njoroge")
 print(name2)

except TypeError:
    print("error found")

class sum:
    def s(self):
        print(2+2)

add=sum()
print(add.s())

