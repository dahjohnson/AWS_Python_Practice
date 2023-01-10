# Create a Range from 1 to the User's Provided Number and Loop Through It

# Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# Print "Fizz" if the Value Is a Multiple of Three and "Buzz" if It's a Multiple of Five

number = int(input('How many values should we process? '))

for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)