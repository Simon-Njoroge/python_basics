
try:
  age=int(input("age: "))
  try:
    print(age)
  except ZeroDivisionError:
    print("age cant be zero")
except ValueError:
  print("inavlid value")
