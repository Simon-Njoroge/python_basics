def add(a,b):
    print(a+b)

add(2,2)

def product():
    total=["simon","jane","caleb"]
    total.insert(3,"simon")
    total.append("joy")
    total.remove("caleb")

    print(len(total))

product()
def sum(x,y):
    print(f"the value of x is {x} and y is {y}={x+y}")
    return x+y
# pass
sum(2,2)