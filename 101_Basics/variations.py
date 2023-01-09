# User will enter a message

message = input("Enter a message: ")

# Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input

print('Lowercase:', message.lower())
print('Uppercase:', message.upper())
print('Title Case:', message.title())
print('Capitalized:', message.capitalize())

# Separate the String and Present the Individual Words as a List

splitMessage = message.split()
print('Words:', splitMessage)

# Print the Alphabetic First and Last Words from the User's Input

sortedWords = sorted(splitMessage)

print('First alphabetic word: ', sortedWords[0])
print('Last alphabetic word: ', sortedWords[-1])