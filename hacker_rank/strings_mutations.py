# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    next_position = position + 1
    new_string = string[:position] + character + string[next_position:]
    return new_string
    
s = input('Enter a string: ')
i, c = input('Enter position and new character: ').split()
s_new = mutate_string(s, int(i), c)
print(s_new)