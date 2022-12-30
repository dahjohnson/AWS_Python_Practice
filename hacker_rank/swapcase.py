# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.

s = "This Is A String"
split_list = []
x_list = []

for char in s:
   split_list.append(char)
   
for x in split_list:
    if x.isupper():
        lower = x.lower()
        x_list.append(lower)
    elif x.islower():
        upper = x.upper()
        x_list.append(upper)
    else:
        x_list.append(x)

final_string = ''.join(x_list)

print(final_string)