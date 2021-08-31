def does_string_have_unique_chars(s : str) -> bool:
    sorted_string = ''.join(sorted(s))
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    
    return True

test_cases = [
    'a',
    'aa',
    'abb',
    'abc',
    'abcdba'
]
for test_string in test_cases:
    print(does_string_have_unique_chars(test_string))