maths = 50
english = 100
kiswahili =80
bio=90
chem=89
comp=10
hist=90
agri=120
av=(maths+english+kiswahili+bio+chem+comp+hist+agri)/8
print(av)

if av<=100 and av>=80:
   print("A")
elif av<=79 and av>=60:
   print("B")
elif av<=59 and av>=50:
   print("C")
elif av<=49 and av>=40:
   print("D")
elif av<=39 and  av>=0:
   print("E")
else:
   print
students = ["jane","ann","joy","caleb","joy"]

last=len(students)-1
print(students[last])

hot=True
if hot:
    print("it is hot ")

name= len(input("insert your name: "))

if name<3:
   print("name must be at least 3 characters")
elif name>50:
   print("name can be a maxmum of 50 characters")
else:
   print("name looks good")

i=1
while i<=5:
   print(i)
   i+=1
print("done")

secret = 9
a=0

while a<3:
   guess=int(input("guess: "))
   a+=1
   if guess == secret:
    print("you won")
    break
else:
   print("you lost")
for items in range(10):
    print(items)
prices = [10,20,30]
total=0
for sum in prices:
   total += sum
print(f"sum: {total}")

# 2D LIST
matrix=[
   [1,2,3,4,5],
   [6,7,8,9,10],
   [11,12,13,14,15]
]



