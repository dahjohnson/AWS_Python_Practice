# HackerRank task - Basic Data Types - Lists

N = int(input('Enter a number: '))
my_list = []

def user_input():
    string = input('Enter command: ')
    s = string.split(' ')
    if s[0] == 'insert':
        my_list.insert(int(s[1]),int(s[2]))
    elif s[0] == 'append':
        my_list.append(int(s[1]))
    elif s[0] == 'remove':
        my_list.remove(int(s[1]))
    elif s[0] == 'pop':
        my_list.pop(-1)
    elif s[0] == 'sort':
        my_list.sort()
    elif s[0] == 'reverse':
        my_list.reverse()
    elif s[0] == 'print':
        print(my_list)
        

for x in range(N):
    user_input()
