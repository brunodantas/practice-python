# Ask the user for a string and print out whether this string
# is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# Solution using generators

def palindrome(word):
    # length = len(word)
    forward_generator = (word[i] for i in range(len(word) // 2))
    backward_generator = (word[-1 - i] for i in range(len(word) // 2))

    for c in forward_generator:
        if c != next(backward_generator):
            return False

    return True


print(palindrome(input()))
