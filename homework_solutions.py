def anagram_dist_first_way(word_1, word_2):
    """
     Your function should take two words and determine the "distance" between them as anagrams.
    """
    first_word_letters = {}
    second_word_letters = {}
    for letter in word_1:
        if letter is first_word_letters:
            first_word_letters[letter] += 1
        else:
            first_word_letters[letter] = 1
    print(first_word_letters)
    for letter in word_2:
        if letter in second_word_letters:
            second_word_letters[letter] += 1
        else:
            second_word_letters[letter] = 1

    distance = 0
    for letter in first_word_letters:
        if letter in second_word_letters:
            distance += abs(first_word_letters[letter] - second_word_letters[letter])
        else:
            distance += first_word_letters[letter]

    for letter in second_word_letters:
        if letter not in first_word_letters:
            distance += second_word_letters[letter]

    return distance


def anagram_distance_trial_two(word_1, word_2):
    word_letters = {}
    for letter in word_1:
        if letter is word_letters:
            word_letters[letter] += 1
        else:
            word_letters[letter] = 1

    for letter in word_2:
        if letter is word_letters:
            word_letters[letter] -= 1
        else:
            word_letters[letter] = -1

    distance = 0
    for letter in word_letters:
        distance += abs(word_letters[letter])

    return distance


def anagram_distance_third_try(word_1, word_2):
    split_word_1 = list(word_1)
    split_word_2 = list(word_2)

    distance = 0

    for letter in word_2:
        if letter in split_word_1:
            split_word_1.remove(letter)
        else:
            distance += 1

    for letter in word_1:
        if letter in split_word_2:
            split_word_2.remove(letter)
        else:
            distance += 1

    return distance


def anagram_tester():
    words = input('Enter two words, or quit.')
    while words.lower() != 'quit':
        split_words = words.lower().split()
        word_1 = split_words[0]
        word_2 = split_words[1]
        print('The anagram distance between {} and {} is {}'.format(word_1, word_2, anagram_distance_third_try(word_1, word_2)))
        words = input('Enter two words, or quit.')


def major_key():
    MUSIC_NOTES = ["C", " C#", "D", "D#", "E", " F", "F#", "G", " G#", " A", " A#", " B"]
    note = input('What note do you want to start with? ')
    start_note = -1
    for i in range(len(MUSIC_NOTES)):
        if note.upper().strip() == MUSIC_NOTES[i].strip():
            start_note = i

    if start_note == -1:
        print('Nope, {} was not a note'.format(note))
        return

    # this is the part that I like.
    MAJOR_SCALE = [2, 2, 1, 2, 2, 2, 1]
    # whole step is that it steps 2 notes (in the middle there are sharps/flats)
    current = start_note
    for step in MAJOR_SCALE:
        print(MUSIC_NOTES[current], end=" ")
        current += step
        current %= len(MUSIC_NOTES)
        # current = (current + step) % len(MUSIC_NOTES)
    print(MUSIC_NOTES[start_note], end=" ")
    # we're done, function over


def is_there_space_ec(grid, shape=[['', 'x', ''], ['x', 'x', 'x']]):
    """
     Determine whether or not the shape can be placed into the
         empty space
    :param grid: a 2d list (all sublists have the same size) of the
         total grid
    :param shape: a 2d list (all sublists will have the same)
     If the position is the empty string (evaluates to false) then it's
     empty, if it doesn't then it's full (for the grid) or part of the
     shape.
    :return: True if there is a place to put the shape on the grid, otherwise False.
    """
    ret = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # what if (i, j) is the start position of the shape?
            found = True
            for shape_i in range(len(shape)):
                for shape_j in range(len(shape[shape_i])):
                    if i + shape_i < len(grid) and j + shape_j < len(grid[i]):
                        # if the position is NOT empty, but we need that position
                        if grid[i + shape_i][j + shape_j] and shape[shape_i][shape_j]:
                            found = False

            if found:
                print('Position found at ({}, {})'.format(i, j))
                ret = True

    return ret


def is_there_space(grid, shape=[['', 'x', ''], ['x', 'x', 'x']]):
    """
    (0, 1)
    (1, 0), (1, 1), (1, 2)
     Determine whether or not the shape can be placed into the
         empty space
    :param grid: a 2d list (all sublists have the same size) of the
         total grid
    :param shape: a 2d list (all sublists will have the same)
     If the position is the empty string (evaluates to false) then it's
     empty, if it doesn't then it's full (for the grid) or part of the
     shape.
    :return: True if there is a place to put the shape on the grid, otherwise False.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # what if (i, j) is the start position of the shape?
            if not grid[i][j + 1] and not grid[i + 1][j] and not grid[i + 1][j + 1] and not grid[i + 1][j + 2]:
                return True
    return False


def weave_lists(first_list, second_list):
    if len(first_list) < len(second_list):
        min_length = len(first_list)
    else:
        min_length = len(second_list)

    # min_length = min(len(first_list), len(second_list))
    # forbidden
    new_list = []
    for i in range(min_length):
        new_list.append(first_list[i])
        new_list.append(second_list[i])

    # until you get to the end, then just dump the rest
    for j in range(min_length, len(first_list)):
        new_list.append(first_list[j])

    for j in range(min_length, len(second_list)):
        new_list.append(second_list[j])

    return new_list


def pig_latin(word):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    # consonants on the front, you move to the back and then have a + ay
    # for vowels we're going to just put "yay" on the back.
    if len(word) > 0 and word[0].lower() in VOWELS:
        return word + 'yay'
    else:
        last_cons = 0
        for i in range(len(word)):
            if word[i].lower() in VOWELS:
                last_cons = i
        return word[last_cons:] + word[0: last_cons] + 'ay'


if __name__ == "__main__":
    print(is_there_space([['x', 'x', 'x'],
                          ['x', 'x', 'x'],
                          ['x', 'x', 'x']],
                         [['x']]))
    print(is_there_space([['x', 'x', 'x'],
                          ['x', '', 'x'],
                          ['x', 'x', 'x']],
                         [['x']]))
    print(is_there_space([['x', 'x', ''],
                          ['x', '', ''],
                          ['x', '', '']],
                         [['', 'x'],
                          ['', 'x'],
                          ['x', 'x']]))
    print(is_there_space([['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['x', '', '', '', ''],
                          ['x', '', '', '', ''],
                          ['x', '', '', '', '']],
                         [['', 'x', ''],
                          ['x', 'x', 'x'],
                          ['', 'x', '']]))
