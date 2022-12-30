# Given an interger, n, and n space-seperated integers as input, create a tuple, t, of those n intergers. 
# Then compute and print the result of hash(t)

# Ran in Pypy 3 

n = int(input())

sn = input()

l = list(sn.split())
int_list = []

for num in l:
    int_list.append(int(num))

t = tuple(int_list)
print(hash(t))