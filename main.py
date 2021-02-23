#print out the numbers 1 - 10

counter = 1
while(counter <= 10):
  print(counter)
  counter += 1

print(" ")
# print out all even numbers between 0 - 20 

number = 2
while(number <= 20):
  print(number)
  number += 2

#ask the user for a number
#print all the number up to the user's number starting at 1

print(" ")

counter = 1
userNumber = int(input("Enter a Number: "))

while(counter <= userNumber):
  print(counter)
  counter += 1

#while():
#    if(condition):
#         print("I am amazing")

print(" ")

counter = 1

while(counter <= 20):
  if(counter%2 == 0):
    print(str(counter) + " is divisible by 2.")
  counter += 1

#print all the numbers between 1-100 that are divisible by 3 or 7.. BUT NOT BOTH

print(" ")

counter = 1
while(counter < 100):
  if(counter%3 == 0):
    if(counter%7 != 0):
       print(str(counter) + " is divisible by 3")
  if(counter%7 == 0):
    if(counter%3 != 0):
      print(str(counter) + " is divisble by 7")
  counter += 1

#print all the numbers between 1-100
#if the number is divisble by 3, print out "Fizz"
#If the number is divisible by 5, print out "Buzz"
#if the number is fivisble by BOTH print out "FizzBuzz"

print(" ")

counter = 1
while(counter <= 100):
  if(counter%3 == 0 and counter%5 != 0):
   print("Fizz")
  if(counter%5 == 0 and counter%3 == 0):
    print("FizzBuzz")
  if(counter%5 == 0 and counter%3 != 0):
    print("Buzz")
  if(counter%5 != 0 and counter%3 != 0):
    print(counter)
  counter += 1