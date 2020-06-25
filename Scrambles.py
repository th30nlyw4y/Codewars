def scramble(str1, str2):
    letters = {}
    for letter in str2:
        letters[letter] = letters.get(letter, 0) + 1
    for letter in letters:
        if letters[letter] <= str1.count(letter):
            continue
        else:
            return False
    return True

