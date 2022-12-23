# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following: 
# 123...n

n = int(input('Enter a Number: '))

for i in range(n):
    print(i + 1, end ='')

