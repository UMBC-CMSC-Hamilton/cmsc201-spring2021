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
    print('size 100000')
    sort_time_test(the_sort, 100000)
    print('size 1000000')
    sort_time_test(the_sort, 1000000)

if __name__ == '__main__':
    # sort_test(10, 1000, quick_sort)
    # time_test(bubble_sort)
    # time_test(insertion_sort)
    time_test(quick_sort)
