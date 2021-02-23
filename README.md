## While Loops

Repeat a set of statements as long as a condition is True

### DRY : Don't Repeat Yourself

### Formula
```python
while(condition): 
  #Comment

else:
  #Optional
  #Body
```

*Ex*
```python
while(True):
  print("This statement prints despite anything")
```

### Rule

A loop becomes an infinite loop if a condition never becomes __False__

To avoid an infinite loop, make sure to use a variable and keep track of it's value.

*Ex*
```python
counter = 0

while(counter < 3):
  print("Inside Loop")
  counter += 1
  #counter = counter + 1

print("Outside Loop")

>Inside loop
>Inside loop
>Inside loop
>Outside loop