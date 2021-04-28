import time
import random


def swap(the_list, i, j):
    """
    :param the_list: is a list, so it's mutable.
    :param i: first index
    :param j: second index
    """
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp


def bubble_sort(the_list):
    swapped = True

    while swapped:
        swapped = False
        # why did you do the minus one?
        # when i compare pairs of elements, i, i + 1, need it to prevent going too far
        # print(the_list)
        for i in range(len(the_list) - 1):
            if the_list[i] > the_list[i + 1]:
                swap(the_list, i, i + 1)
                swapped = True

    return the_list


def sort_test(num_tests, size_of_list, the_sort):
    for test in range(1, num_tests + 1):
        # forbidden arts
        list_to_sort = [random.randint(0, 100) for _ in range(size_of_list)]
        copy_of_list = list(list_to_sort)
        list_to_sort = the_sort(list_to_sort)
        copy_of_list.sort()
        if list_to_sort == copy_of_list:
            print('Test {}: The list was sorted'.format(test))
        else:
            print('Test {}: The list was not sorted.'.format(test))
            print(list_to_sort)
            print(copy_of_list)


def selection_sort(the_list):
    for i in range(len(the_list)):
        min_index = i
        # print(the_list)
        for j in range(i + 1, len(the_list)):
            if the_list[min_index] > the_list[j]:
                min_index = j
        if i != min_index:
            swap(the_list, i, min_index)

    return the_list


def selection_sort_max_instead(the_list):
    for i in range(len(the_list)):
        # len(the_list) - 1 (the last element)
        # len(the_list) - 1 - i (i elements from the end)
        max_index = len(the_list) - 1 - i
        for j in range(len(the_list) - 1 - i):
            if the_list[max_index] < the_list[j]:
                max_index = j
        if len(the_list) - 1 - i != max_index:
            swap(the_list, len(the_list) - 1 - i, max_index)

    return the_list


def insertion_sort(the_list):
    """
        Hardest one for me to understand.  But why?
        I have no idea.

        Pull-back sort until the sublist from 0 to i is sorted
            indexes up to i + 1 and repeats.
    :param the_list:
    :return:
    """
    for i in range(1, len(the_list)):
        j = i
        while j > 0 and the_list[j - 1] > the_list[j]:
            swap(the_list, j - 1, j)
            j -= 1

    return the_list


# Quick Sort this time, we'll save merge sort (my favorite) until last.
def quick_sort(the_list):
    if len(the_list) in [0, 1]:
        return the_list

    less_list = []
    greater_list = []
    equal_list = []

    pivot = the_list[0]

    for x in the_list:
        if x < pivot:
            less_list.append(x)
        elif x == pivot:
            equal_list.append(x)
        elif x > pivot:
            greater_list.append(x)

    return quick_sort(less_list) + equal_list + quick_sort(greater_list)


def sort_time_test(sorting, n):
    for i in range(3):
        my_list = [random.randint(0, 100) for _ in range(n)]
        start = time.time()
        sorting(my_list)
        end = time.time()
        # ns is 10^(-9) seconds
        print('The time was', end - start)


def time_test(the_sort):
    print('size 10')
    sort_time_test(the_sort, 10)
    print('size 100')
    sort_time_test(the_sort, 100)
    print('size 1000')
    sort_time_test(the_sort, 1000)
    print('size 10000')
    sort_time_test(the_sort, 10000)
    # print('size 100000')
    # sort_time_test(the_sort, 100000)
    # print('size 1000000')
    # sort_time_test(the_sort, 1000000)


def merge(first_list, second_list):
    """
        first_list, and second-list must be sorted already.
        :return: sorted combination of the two lists

        sor(t/d)ed list sordid <--> sorted ??
    """

    result = []
    first_index = 0
    second_index = 0
    while first_index < len(first_list) and second_index < len(second_list):
        # if the first list at the current index is smaller take that one
        if first_list[first_index] <= second_list[second_index]:
            result.append(first_list[first_index])
            # dont' want to take an element twice
            first_index += 1
        else:
            result.append(second_list[second_index])
            # dont' want to take an element twice
            second_index += 1

    # are we done? not quite yet
    for index in range(first_index, len(first_list)):
        result.append(first_list[index])
    # only one will ever go, the loop above, or the loop below.
    for index in range(second_index, len(second_list)):
        result.append(second_list[index])

    return result


"""
    [5 3]
    merge([5], [3]) = [3, 5]
    
    [2, 8, 1, 4]
    [2, 8] [1, 4]
    [2] [8] [1] [4]
    Merge([2] [8]) Merge([1] [4])
    Merge([2, 8], [1, 4])
    [1, 2, 4, 8]
    
    [5, 3, 1, 9, 2]
    5 // 2 -> 2 [0: 2] 0, 1 [2: 5] 2, 3, 4
    [5, 3] [1, 9, 2]
    [5] [3] | [1] [9, 2]
    [5] [3] | ([1] | [9] [2])
    [3, 5] | ([1] [2, 9])
    [3, 5] | ([1, 2, 9])
    [1, 2, 3, 5, 9]
"""


def merge_sort(the_list):
    if len(the_list) <= 1:
        # [] empty list is sorted
        # [x] sorted
        return the_list

    # dumbest possible idea, just split list in half, 0 up to half way, half way up to the rest
    first_half = merge_sort(the_list[0: len(the_list) // 2])
    second_half = merge_sort(the_list[len(the_list) // 2: len(the_list)])
    return merge(first_half, second_half)


def linear_search(a_list, element):
    for x in a_list:
        if x == element:
            return True

    return False


def binary_search(a_list, element):
    return binary_search_rec(a_list, element, 0, len(a_list))


def binary_search_rec(a_list, element, start, end):
    # this is the midpoint formula
    place_to_search = (start + end) // 2
    # print(start, end, place_to_search, a_list[place_to_search])
    if end <= start:
        return False
    if a_list[place_to_search] == element:
        return True
    elif element < a_list[place_to_search]:
        return binary_search_rec(a_list, element, start, place_to_search)
    else:
        return binary_search_rec(a_list, element, place_to_search + 1, end)


def binary_search_slices(a_list, element):
    # this is the midpoint formula
    place_to_search = len(a_list) // 2
    if not len(a_list):
        return False
    if a_list[place_to_search] == element:
        return True
    elif element < a_list[place_to_search]:
        return binary_search_slices(a_list[0: place_to_search], element)
    else:
        return binary_search_slices(a_list[place_to_search + 1: len(a_list)], element)

def permutation(n, current, used):
    if len(used) == n:
        print(current)
        return

    for i in range(1, n + 1):
        if i not in used:
            permutation(n, current + str(i), used + [i])


def binary_search_time_test():

    my_list = []
    for i in range(10000000):
        my_list.append(random.randint(0, 10000))

    my_list.sort()  # running in C under python so it'll be faster.
    print(my_list)
    # x = int(input('Enter element to search: '))
    lin_average = 0
    bin_average = 0
    for i in range(10):
        find_me = random.randint(0, 1000)
        bin_start = time.time()
        binary_search(my_list, find_me)
        bin_time = time.time() - bin_start

        lin_start = time.time()
        linear_search(my_list, find_me)
        lin_time = time.time() - lin_start
        bin_average += bin_time
        lin_average += lin_time
        print('The binary time was {}, the linear time was {}'.format(bin_time, lin_time))

    bin_average /= 10
    lin_average /= 10
    print('The average binary time was {}, the linear average time was {}'.format(bin_average, lin_average))


if __name__ == '__main__':
    # sort_test(10, 1000, quick_sort)
    # time_test(bubble_sort)
    # time_test(insertion_sort)
    # time_test(quick_sort)
    """
    print('Bubble')
    time_test(bubble_sort)
    print('Selection')
    time_test(selection_sort)
    print('Insertion')
    time_test(insertion_sort)
    # sort_test(10, 10000, merge_sort)
    print('Selection')
    time_test(selection_sort)
    print('Quick')
    time_test(quick_sort)
    print('Merge')
    time_test(merge_sort)
    """
    permutation(12, '', [])
