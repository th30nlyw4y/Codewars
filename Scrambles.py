import time

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



if __name__ == '__main__':
    start_time = time.time()
    print(scramble('vveqgvuuygp', 'hpsrmkhrft'))
    print(time.time()-start_time)