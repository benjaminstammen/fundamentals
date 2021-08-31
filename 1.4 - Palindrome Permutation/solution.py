# We want to know if a string is a permutation of a palindrome.
# It doesn't matter where spaces are, so ignore those
def is_word_palindrome_permutation(s : str) -> bool:

    char_dictionary = {}
    for char in s.lower():
        if char in char_dictionary:
            char_dictionary[char] = char_dictionary[char] + 1
        else:
            char_dictionary[char] = 1
    
    odd_available = True
    for char, val in char_dictionary.items():
        if char == ' ':
            continue

        if val % 2 != 0:
            if odd_available:
                odd_available = False
            else:
                return False
    return True

test_cases = [
    ['a', True],
    ['aa', True],
    ['abb', True],
    ['abc', False],
    ['abcdba', False],
    ['supercalafragalisticexpealidocious', False],
    ['tacos ubu tacos', True],
    ['Tact coa', True]
]
for test_case in test_cases:
    if is_word_palindrome_permutation(test_case[0]) == test_case[1]:
        print("PASS")
    else:
        print("FAIL")