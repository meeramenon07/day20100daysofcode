print("Welcome to List Generator App")
print("In this list Generator App, you are going to enter the Starting number, the Ending number and also an Increment number to increase the numbers by that Increment number every time. Let's get started!")
print()
start = int(input("List a Starting Number: "))
end = int(input("List a End Number: "))
incr = int(input("List a Increment between values: "))

for i in range(start,end,incr):
  print(i)