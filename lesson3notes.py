'''
when you are indexing into a string, position -1 is the last position, 0 is the first
-2 is the second to last, etc.
s = "abc", s[-1] is "c", a[0] is "a", s[20] returns an index out of range error
'''

s = 'abc'
print(s[0], s[1], s[2])

'''
what we're doing is called "slicing" the string
format is [start:stop:step]
The defaults are [0:len(s):1]
if one number is given, it selects the one item at that location
if two numbers are given, it selects the range of values from the first location to one before the second location
'''

print(s[1:3])

# reversing a string can be done by taking a slice of it with a backwards counting step

print(s[::-1])

# strings are immutable, so saying s[0]="y" will result in an error
# s must instead be redefined
# this is equivalent: s = "y"+s[1:len(s)]
s = "y"+s[1:len(s)]
print(s)

# looping
for var in range(4):
    # do somethiing for var being 0, 1, 2, or 3
    break


s = "abcdefgh"

# the following does the exact same thing, but the bottom way is more "pythony"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("there is an i or u")

for char in s:
    if char == 'i' or char == 'u':
        print("there is an i or u")