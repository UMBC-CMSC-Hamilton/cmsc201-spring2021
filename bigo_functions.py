def count_total(a_list):
    """
    :param a_list: generally the list size is going to be what we call "n".
    :return:
    # steps it takes to run:
        1
        n * 1
        1
        n + 2 steps.
        O(n) algorithm.
        Think as n gets "large" n = 1,000,000 or 10,000,000
        difference between 10^6 and 10^6 + 2 is almost negligible.
    """
    total = 0
    for x in a_list:
        total += x

    return total


def is_prime(n):
    """
        What is the time complexity of this function?
        For loop runs ~ sqrt(n) times.
        O(sqrt(n))
    """
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_worse(n):
    """
        What is the time complexity of this function?
        For loop runs ~ sqrt(n) times.
        O(n)
        Why start at 2?
        n % 0 a division by zero error < can't do it.
        n % 1 == 0 n / 1 == n R 0 <-- mod is always remainder
        n % 1 == 0 not actually telling us anything about if the number n is prime.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def pointless_counting(n):
    """
        1
        outer for loop n * [ stuff inside ]
        stuff inside = inner for loop n * [stuff inside of that]
        innermost stuff = assignment
            Assume: all additions take the same amount of time.  All constant time relative to n.
                    if statements too, O(1)
            O(1)
            2 + n * n * O(1) = O(n^2)
    """
    total = 0
    for i in range(n):
        for j in range(n):
            # if you're looking at this calculation beyond just saying "it's constant time" then you're
            # thinking too hard about it.
            total += i * j - i ** 2 - j ** 2
    return total


def matrix_multiplication(matrix_a, matrix_b):
    """

    :param matrix_a: n * k matrix 2d list of numbers
    :param matrix_b: k * m matrix 2d list of numbers
    :return: A * B as matricies

    outer loop = n * [second loop]
    second loop = m * [third loop]
    third loop = k * [inner calculation]
    inner calculation = O(1)
    total time = n * m * k O(1) = O(nmk)
    Simplification: assume that n = m = k
    O(nnn) = O(n^3) time.
    """
    result_matrix = []
    for i in range(len(matrix_a)):
        result_matrix.append([])
        for j in range(len(matrix_b[0])):
            result_matrix.append(0)
            for k in range(len(matrix_a[0])):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix


def loggy_time(n):
    """
    O(lg(n)) time.
    Why ???
    n = 16
    16 -> 8 -> 4 -> 2 -> 1 -> 0 (ans = 5)
    32 -> 16 -> 8 -> 4 -> 2 -> 1 -> 0 (ans = 6)
    64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 -> 0 (ans = 7)
    128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 -> 0 (ans = 8)

    Q what about non-pure powers? 2^k = n; 17 = 2^k no integer k so that this works.
    345 -> 172 -> 86 -> 43 -> 21 -> 10 -> 5 -> 2 -> 1 -> 0 (9 steps)
    Is that approximately lg(345) ~= 8.4

    Yes it approximately is right.

    Def of lg is the number of times you have to divide by 2 until you get down to 1. (caveat: decimals exist)
    lg(x) = y when 2^y = x
    I have to divide x by 2 "y" times.
        ln(x) = int 1 to x of 1/x dx
        Inverse of exponential: what does that mean?
            2^y = 2* 2* 2 * 2 * 2 ... * 2 (y times) = x
            lg(x) = y
    """
    count = 0
    while n >= 1:
        count += 1
        n //= 2
    return count
