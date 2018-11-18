# -*- encoding: utf-8 -*-

# This problem was asked by Nest.
# 
# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.
# 
# We can consider a sentence valid if it conforms to the following rules:
# 
# The sentence must start with a capital letter, followed by a lowercase letter or a space.
# All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
# There must be a single space between each word.
# The sentence must end with a terminal mark immediately following a word.

END_PUNCT = ['.', '?', '!', '?', '‽']
SEPARATORS = list(',;: ')
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
ALLOWED_CHARS = LETTERS + SEPARATORS + END_PUNCT

def f(test):
    
    def starts_with_capital(test):
        if test[0].isupper() \
        and (
            test[1].islower()
            or test[1] == ' '
        ):
            return True
        return False
        
    def has_expected_characters(test):
        for char in test[1:]:
            if char not in ALLOWED_CHARS:
                return False
        return True
        
    def is_correctly_whitespaced(test):
        if ' '.join(test.split()) == test:
            return True
        return False
        
    def has_end_of_sentence(test):
        if test[-1] in END_PUNCT:
            return True
        return False
        
    def is_valid(test):
#         print '-starts_with_capital', starts_with_capital(test)
#         print '-has_expected_characters', has_expected_characters(test)
#         print '-is_correctly_whitespaced', is_correctly_whitespaced(test)
#         print '-has_end_of_sentence', has_end_of_sentence(test)
        if starts_with_capital(test) \
        and has_expected_characters(test) \
        and is_correctly_whitespaced(test) \
        and has_end_of_sentence(test):
            return True
        return False
    
    if is_valid(test):
        print test
        return True
    else:
        print
        return False


if __name__ == '__main__':
    
    tests = """This problem was asked by Nest.
Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
If a sentence is valid, the program should print it out.
We can consider a sentence valid if it conforms to the following rules:
-The sentence must start with a capital letter, followed by a lowercase letter or a space.
-All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
-There must be a single space between each word.
-The sentence must end with a terminal mark immediately following a word.""".split('\n')
    
    for test in tests:
        if not test.strip():
            continue
        print test
        f(test)
        print
