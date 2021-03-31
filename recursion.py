def countdown(x):
    print('we are in countdown({})'.format(x))
    if x == 0:
        # base case, terminating condition for the recursion, etc
        print('kaboom')
    else:
        # recursive case (it has a recursive call)
        print('x = ', x)
        countdown(x - 1)
    print('we leaving countdown({})'.format(x))


# countdown(5)  # recursion limit is about 1000

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + ... n = n(n - 1)/2
def gauss_sum_formula(n):
    return n * (n - 1) // 2


def gauss_sum_for_loop(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


# worst way to do it.
# recursive problems should mostly be thought of splitting a problem into a subproblem.
# what is the sum of all the numbers from 1 to n
# I don't know, but if I knew the sum from 1 to n - 1, then i'd add n.
# but when do we stop?  well i do know that if you're adding up from 0 to 0 the answer should be 0
def gauss_sum_recursive(n):
    # base case
    if n == 0:
        return 0
    # recursive case
    return gauss_sum_recursive(n - 1) + n


"""
print('gauss sum of 1 is', gauss_sum_recursive(1))
print('gauss sum of 5 is', gauss_sum_recursive(5))
print('gauss sum of 20 is', gauss_sum_recursive(20))
print('gauss sum of 100 is', gauss_sum_recursive(100))

gauss_sum_recursive(100) = gauss_sum_recursive(99) + 100
gauss_sum_recursive(100) = gauss_sum_recursive(98) + 99 + 100
gauss_sum_recursive(100) = gauss_sum_recursive(97) + 98 + 99 + 100
gauss_sum_recursive(100) = gauss_sum_recursive(96) + 97 + 98 + 99 + 100
gauss_sum_recursive(100) = gauss_sum_recursive(95) + 96 + 97 + 98 + 99 + 100

gauss_sum_recursive(5) = gauss_sum_recursive(4) + 5
gauss_sum_recursive(5) = gauss_sum_recursive(3) + 4 + 5
gauss_sum_recursive(5) = gauss_sum_recursive(2) + 3 + 4 + 5
gauss_sum_recursive(5) = gauss_sum_recursive(1) + 2 + 3 + 4 + 5
gauss_sum_recursive(5) = gauss_sum_recursive(0) + 1 + 2 + 3 + 4 + 5
gauss_sum_recursive(0) = 0
gauss_sum_recursive(5) = 1 + 2 + 3 + 4 + 5

The multiplicative analog of gauss sums are factorials.  

0! = 1 (by definition, other reasons)
1! = 1 = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120
6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
"""


def factorial_iterative(n):
    total = 1  # 0! = 1
    for i in range(n + 1):
        total *= i
    return total


def factorial_recursive(n):
    """
        Think to yourself: how do i break this problem down into a recursive problem?

        Well maybe if i knew (n - 1)! then i'd be in luck?
        (n - 1)! =  (n - 1)(n - 2)(n - 3)...(3)(2)(1)
        n!       = n(n - 1)(n - 2)(n - 3)...(3)(2)(1)

        n! = n * (n - 1)! (this is true) (this looks kind of recursive to me
        Fact(n) = n * Fact(n - 1)
        0! = 1 (hint, this is our base case)
    """
    print('We are entering factorial({})'.format(n))
    if n <= 0:
        result = 1
    else:
        result = n * factorial_recursive(n - 1)
    print('We are leaving factorial({}) and the result is currently {}'.format(n, result))
    return result


"""
    Describe the fibonacci numbers.
    Def: 
        Recursive Case/Definition
            Fib(n) = Fib(n - 1) + Fib(n - 2)
        Base case:
            Fib(0) = 1
            Fib(1) = 1
    
    Fib(2) = Fib(1) + Fib(0) = 1 + 1 = 2
    Fib(3) = Fib(2) + Fib(1) = 2 + 1 = 3
    Fib(4) = Fib(3) + Fib(2) = 3 + 2 = 5
    Fib(5) = Fib(4) + Fib(3) = 5 + 3 = 8
    Fib(6) = Fib(5) + Fib(4) = 8 + 5 = 13
    Fib(7) = Fib(6) + Fib(5) = 13 + 8 = 21 
"""


def fib(n):
    if n < 0:
        return 0
    elif n in [0, 1]:  # equivalently: elif n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def verbose_fib(n, N):
    if n < 0:
        print('\t' * (N - n) + 'Invalid fibonacci index. ')
        return 0
    elif n in [0, 1]:  # equivalently: elif n == 0 or n == 1:
        print('\t' * (N - n) + 'Base Case, Returning 1. ')
        return 1
    else:
        print('\t' * (N - n) + 'Calling Fib({})'.format(n - 1))
        fib_of_n_minus_one = verbose_fib(n - 1, N)
        print('\t' * (N - n) + 'Calling Fib({})'.format(n - 2))
        fib_of_n_minus_two = verbose_fib(n - 2, N)
        print('\t' * (N - n) + 'Fib({}) = {}'.format(n, fib_of_n_minus_one + fib_of_n_minus_two))
        return fib_of_n_minus_one + fib_of_n_minus_two


def test_fibonacci():
    s = input('Enter quit or int: ')
    while s != 'quit':
        verbose_fib(int(s), int(s))
        s = input('Enter quit or int: ')


"""
    I want you to give me a length n, and i'm going to write out every possibility in a's and b's that is length n.
    n = 0
        what do you know?
        there's no more length so no more a's and b's so basically you're done
    n = 1
        a
        b
    n = 2
        aa
        ab
        ba
        bb
    n = 3
        aaa     baa
        aab     bab
        aba     bba
        abb     bbb
    n = 4
        I used the copy-paste trick.  
        aaaa     abaa
        aaab     abab
        aaba     abba
        aabb     abbb

        baaa     bbaa
        baab     bbab
        baba     bbba
        babb     bbbb
        I took all the answers from n =3, then I added an a onto the front
        I took all the answers from n = 3 and added a b onto the front....
"""


def write_out_as_and_bs(n, current, tab_level):
    if n == 0:
        print('\t' * tab_level, current)
    else:
        print('\t' * tab_level, 'Current is now {}'.format(current))
        write_out_as_and_bs(n - 1, 'a' + current, tab_level + 1)
        write_out_as_and_bs(n - 1, 'b' + current, tab_level + 1)


"""
    Old HW problem: 
        Modify this solution to only strings with k a's.  (n - k) b's.
            Add another argument (which is k).  You'll need an extra if statement.  
            Or you can modify the base case.  
        
        If you have a string of a's and b's hypothetically 
            n = 5, k = 2
            
            C(5, 2) = 10 = 5!/(2!3!)
            aabbb
            ababb
            abbab
            abbba
            baabb
            babab
            babba
            bbaab
            bbaba
            bbbaa  
        
        If you already have a string
            bab
            What do you need to do to make it length 5?
                you need to add on two more letters
                already have 1 a, so we only want one more.
            
"""


def as_and_bs(n, current):
    if n == 0:
        print(current)
    else:
        as_and_bs(n - 1, 'a' + current)
        as_and_bs(n - 1, 'b' + current)


write_out_as_and_bs(4, '', 0)
"""
write_out_as_and_bs(3, 'a')
    write_out_as_and_bs(2, 'aa')
        write_out_as_and_bs(1, 'aaa')
        write_out_as_and_bs(1, 'baa')
    write_out_as_and_bs(2, 'ba')
        write_out_as_and_bs(1, 'bba')
        write_out_as_and_bs(1, 'bba')
write_out_as_and_bs(3, 'b')
    write_out_as_and_bs(2, 'ab')
    write_out_as_and_bs(2, 'bb')
"""

"""
    Recursion is usually confusing.
        but...
        
    Usually have some index.

    seq(n) = 3 seq(n - 1) + 5 seq(n - 2) - 2 * seq(n - 3)
        seq(0) = 2
        seq(1) = 3
        seq(2) = 1
"""


def seq(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    elif n == 2:
        return 1
    else:
        return seq(n - 1) + seq(n - 2) + seq(n - 3)


"""
    Branching recursion
        sequence which is defined in terms of smaller values
        calculate the smaller values first and then recalculate the big value.
    
        take a current object, and you add all the different options to it
            ok now make all the objects of size n - 1.  
    
        Palindromes - iterative solution, recursive solution using SLICES 
    
        Pathfinding maybe?
        Sierpinski's Triangle - pretty cool and it is a recursive-required object.
 
"""