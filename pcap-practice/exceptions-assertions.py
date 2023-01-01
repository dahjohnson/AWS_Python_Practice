# Bad Division Exception Example
# You are able to run try and except blocks inside/outside a function

def bad_division(x,y):
    try:
        return x / y
    except ZeroDivisionError: # concrete exception
        print(('You can\'t divide {0} by Zero you Silly Goose! :P').format(numerator))
        raise # the raise instruction can only be used in an except block

numerator = 1
denominator = 0

# assertions used to verify integers are not negative
assert numerator >= 0.0 
assert denominator >= 0.0

try:
    division = bad_division(numerator, denominator)
    print(('{0} divided by {1} is {2}').format(numerator, denominator, division))
except ArithmeticError: # base class for those built-in exceptions that are raised for various arithmetic errors
    print("This was an Arithmetic Error!")

print("THAT'S ALL FOLKS!")