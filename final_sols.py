def simple_jumble(a_string, a, b):
    answer = ''
    for x in range(len(a_string)):
        answer += a_string[(a * x + b) % len(a_string)]

    return answer


"""
    How do we fix the repetition business?
"""


def jumble(a_string, a, b):
    """
        Remember things by sticking them into a list or a dict.
            Check every time to make sure there's no repetition going on.
    """
    answer = ''
    index_dict = {}
    for x in range(len(a_string)):
        jumble_index = (a * x + b) % len(a_string)
        if jumble_index not in index_dict:
            answer += a_string[jumble_index]
            index_dict[jumble_index] = True

    return answer


def test_jumble():
    print(jumble('ninewords', 3, 7))
    print(jumble('aaaaaaaa', 5, 0))
    print(jumble('abcdefgh', 5, 0))


""" 
    how do you search through all substrings of a string?
        What is a substring?
            a contiguous sequence formed from the original string.  
            
        abcdefg
        cdef
        ab
        abcd
        aef <-- not a substring
        
        start, end, because it's contiguous "substrings are parametrized by these two numbers."
              
"""


def longest_substring(total_string, find_string):
    max_length = 0
    for start in range(len(find_string)):
        for end in range(start + 1, len(find_string) + 1):
            if find_string[start: end] in total_string:
                if max_length < end - start:
                    max_length = end - start

    return max_length


def test_longest_substring():
    print(longest_substring('wherefore art thou romeo', 'four score and seven years ago'))
    print(longest_substring('rqqrfxwdpgkqihdhyuqath', 'lfxwc'))


"""
    1 -> 1 cool
    2 -> 2 + 1 = 3
    3 -> 3 + 2 + 1 = 6
    4 -> 4 + 3 + 2 + 1 = 10
    5 -> 5 + 4 + 3 + 2 + 1 = 15
    6 -> 6 + 5 + 4 + 3 + 2 + 1 = 21
    ...
    g(d) = d(d + 1)/ 2 <-- my favorite formula in CS, other than maybe Stirling.  
"""


def nth_day_of_christmas_nrec(day):
    total_gifts = 0
    for d in range(day + 1):
        gifts_on_day_d = 0
        for i in range(d + 1):
            gifts_on_day_d += i
        total_gifts += gifts_on_day_d
    return total_gifts


def nth_day_of_christmas_nrec_easier(day):
    total_gifts = 0
    for d in range(day + 1):
        # 1 + 2 + 3 + ... + d = d(d + 1) / 2
        gifts_on_day_d = d * (d + 1) / 2
        total_gifts += gifts_on_day_d
    return total_gifts


def nth_day_of_christmas_nrec_easiest(day):
    # sum d = 1 to n of d (d + 1) / 2
    # sum d^2 = d(d + 1)(2d + 1) / 12
    # sum d = d( d + 1) / 4
    # but that's hard because i don't know math.
    return int(day * (day + 1) * (2 * day + 1) / 12 + day * (day + 1) / 4)


def nth_day_of_christmas(day):
    if not day:
        return 0

    # gifts_on_day_d = day * (day + 1) // 2
    gifts_on_day_d = 0
    for i in range(day + 1):
        gifts_on_day_d += i

    # but wait we don't have a base case we're all going to die... ok now we do.
    return gifts_on_day_d + nth_day_of_christmas(day - 1)
    # what is this "really"? it's a recursive countdown, we've done that all the time.


def test_nth_day():
    # cool it works
    print(nth_day_of_christmas_nrec_easiest(12))
    print(nth_day_of_christmas_nrec_easiest(365))
    print(nth_day_of_christmas_nrec_easiest(52))
    print(nth_day_of_christmas_nrec_easiest(821))


def lucky_base(base_ten_number):
    base_seven_result = ''
    if base_ten_number == 0:
        return '0'

    while base_ten_number:  # != 0
        # backwards
        # base_seven_result += str(base_ten_number % 7) # this line here add new digit to the start
        # forwards
        base_seven_result = str(base_ten_number % 7) + base_seven_result
        base_ten_number //= 7

    return base_seven_result


print(lucky_base(0))
print(lucky_base(5))
print(lucky_base(15))
print(lucky_base(381))
print(lucky_base(2873))
print(lucky_base(112334))
"""
dec     lucky
0       0
5       5
15      21
381     1053
2873    11243
112334  645335
"""

"""
    either it's a P or a space<--
"""

SPACE = ' '
PICKET = 'P'


def check_picket(board, y, x):
    for i in range(2, len(board)):
        # testing understanding of how to check if you're on a board, in range
        if 0 <= y + i < len(board) and 0 <= x + i < len(board[0]):
            # testing understanding of 2d grid
            if board[y + i][x + i] == PICKET:
                print(y + i, x + i)
                return False
        if 0 <= y - i < len(board) and 0 <= x - i < len(board[0]):
            if board[y - i][x - i] == PICKET:
                print(y - i, x - i)
                return False
        if 0 <= y + i < len(board) and 0 <= x - i < len(board[0]):
            if board[y + i][x - i] == PICKET:
                print(y + i, x - i)
                return False
        if 0 <= y - i < len(board) and 0 <= x + i < len(board[0]):
            if board[y - i][x + i] == PICKET:
                print(y - i, x + i)
                return False

    return True


def pickets_problem(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == PICKET:
                if not check_picket(board, y, x):
                    print(y, x)
                    return False
    return True


print(pickets_problem([[PICKET, SPACE, SPACE],
                       [SPACE, SPACE, SPACE],
                       [PICKET, PICKET, PICKET]]
                      ))

print(pickets_problem([[PICKET, SPACE, SPACE],
                       [SPACE, SPACE, SPACE],
                       [PICKET, PICKET, SPACE]]
                      ))


def jelly_bean_sort(list_of_beans):
    # just for ease of counting
    color_map = {}
    for color in list_of_beans:
        if color in color_map:
            color_map[color] += 1
        else:
            color_map[color] = 1

    list_to_sort = []
    for color in list_of_beans:
        list_to_sort.append([color, color_map[color]])

    # chose insertion sort (short, code length wise)
    for i in range(len(list_to_sort)):
        j = i
        while j > 0 and list_to_sort[j][1] < list_to_sort[j - 1][1]:
            swap_temp = list_to_sort[j]
            list_to_sort[j] = list_to_sort[j - 1]
            list_to_sort[j - 1] = swap_temp
            j -= 1
    return list_to_sort

