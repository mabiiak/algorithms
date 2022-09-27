def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first = list(first_string.lower())
    second = list(second_string.lower())

    for letter in first:
        if letter in second:
            second.remove(letter)
        else: 
            return False

    return True
