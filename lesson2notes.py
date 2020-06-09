x = 1
x_str = str(x)
# commas in print() get coerced to a string type, and are added to the string with a space
print('my fav number is',x,'.','x=',x)
# plus signs in print() only allows strings, and doesn't add spaces.
print('my fav number is'+x_str+'x='+x_str)
# the first example is using multiple inputs to the print() function
# the second example is only using one input, and so it must all be the same type

# here we see the operation where we print out the result from multiplying two ints
print(5*x)
# here we see the operation where we print out the result from multiplying a string and an int
print(5*x_str)

# input only returns strings from the user (user types 5, and the function returns "5")

# and not and or are boolean operators
and_val = x==1 and x==4
or_val = x==1 or x==4
not_val= not x==4
print(and_val)
print(or_val)
print(not_val)

# string can be compared as greater or less than. This is done by sorting alphabeticlaly
print ("a" < "ba")

# range(number) creates an array going from 0 to (number-1)
print(range(5))

# this prints out the numbers 0 through 4
n = 0
for n in range(5):
    print(str(n))

# this also prints out numbers 0 through 4
n = 0
while n < 5:
    print(n)
    n += 1

# range(start, stop, step)
# range goes up to one less than the stop number
# range(number) is range(0, number, 1)
# range(numberA, numberB) is range(numberA, numberB, 1)
# range(numberA, numberB, numberC) is range(numberA, numberB, numberC)

# if you want to exit a loop before its condition is met, you can use the break statement
while True:
    print("I'm running!")
    while True:
        print("So am I!")
        # exit out of the inner loop
        break
    # exit out of the outer loop
    break