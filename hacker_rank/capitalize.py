# Hacker Rank Challenge
# Capitalize the First and Last name of a user

user_name = input("Enter a user's first and last name: ")

mylist = user_name.split(" ")
capital = [name.capitalize() for name in mylist]
join = " ".join(capital)
print(join)