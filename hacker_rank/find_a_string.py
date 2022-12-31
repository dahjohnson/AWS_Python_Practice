# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    locate = string.find(sub_string)
    count = 0
    while locate != -1:
        count += 1
        locate = string.find(sub_string, locate + 1)
    return count

string = input('Enter a string: ').strip()
sub_string = input('Enter a substring: ').strip()

count = count_substring(string, sub_string)
print(count)

