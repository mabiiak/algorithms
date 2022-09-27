def is_palindrome_iterative(word):
    comum = list(word)
    contrary = []

    if not word:
        return False
    else:
        for letter in enumerate(word):
            remove = comum.pop()
            contrary.append(remove)

        if contrary == list(word):
            return True
        else:
            return False
