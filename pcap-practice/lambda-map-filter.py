from math import sqrt

# Important Note
## Once a Lambda map or filter is used the data processed must be moved to a new list to be persistent 

# Lambda function to determine area
area = lambda x,y: x ** 2 + y ** 2

# Lambda function to determine the hypotenuse
hypot = lambda a,b: sqrt(a ** 2 + b ** 2)

x = 7
y = 8

a = 4
b = 3

print(f'\nThe area of {x} and {y} is', area(x,y))
print(f'The hypotenuse of {a} and {b} is', hypot(a,b), '\n')

# Lambda function that finds x * x * x
x3 = lambda x: x ** 3

# Lambda function that finds even numbers
even = lambda x: x % 2 == 0

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

# Dont include the () in the lamba function (ref line 15-16)
triple_x = map(x3, arr) 
map_list = [] 

# Create new list for processed mapped data
for i in list(triple_x):
    map_list.append(i)

#  Fitler based on even numbers
even_filter = filter(even, map_list) # Don't forget to add list() function to map function variable

print('The numbers in the list "arr" raised to the third power are: ')
print(map_list)

print('\n\nThe even numbers are: ')
print(list(even_filter),'\n')