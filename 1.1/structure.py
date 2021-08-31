def does_string_have_unique_chars(s : str) -> bool:
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

test_cases = [
    ['a', True],
    ['aa', False],
    ['abb', False],
    ['abc', True],
    ['abcdba', False]
]
for test_case in test_cases:
    if does_string_have_unique_chars(test_case[0]) == test_case[1]:
        print("PASS")
    else:
        print("FAIL")