# For a list of words, print out each word on a separate line, but in all uppercase.
words = ["hello", "hey", "goodbye", "yo", "yes", "Eagle", "engine"]

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """Print each word in a passed list

    Args:
        words ([list]): a list of words
    """    

    for word in words:
        upper_word = word.upper()
        print(upper_word)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def print_words_that_start_with_passed_letter(words, letter):
    """Print words that only start with the 'letter' param.
    Example: 
        print_words_that_start_with_passed_letter(words, "a")
        would only print words that start with "a"
    Args:
        words (list): a list of words
        letter (string): a letter you want to pass as a parameter
    """    
    for word in words:
        if (word.startswith(letter.lower())) or (word.startswith(letter.upper())):
            print(word.upper())
            
print_words_that_start_with_passed_letter(words, "e")

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(words, must_start_with):
    """Print words that start with letters passed in 'must_start_with'.

    Args:
        words (list): a list of words
        must_start_with (dict): a dictionary of letters to check against words
    """    
    for word in words:
        for letter in must_start_with:
            if (word.startswith(letter)):
                print(word)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"})
