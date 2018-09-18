"""
Exam 1, problem 2.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and Jacob Pinney.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time
import math


def main():
    """ Calls the   TEST   functions in this module. """
    problem2a_testing()
    run_test_problem2b()
    run_test_problem2c()


def problem2a_testing():
    """ Tests the   sum_of_digits_of_sum_of_factors   function. """
    ############################################################################
    #  DONE: 2. Implement this TEST function.  See the IMPORTANT NOTE below.
    #     This problem TESTS the    sum_of_digits_of_sum_of_factors    function
    #     that is defined below.  Include at least **   4   ** tests.
    #     Use the usual format:
    #       Test XXX:
    #       expected = XXX
    #       actual = XXX
    #       print()
    #       print('Expected:', expected)
    #       print('Actual:  ', actual)
    #
    #  DONE (continued): IMPORTANT NOTE:
    #  DONE (continued):   The function that you are TESTING is PURPOSELY
    #  DONE (continued)    NOT implemented.  Do NOT implement it.  That is,
    #                   do NOT implement the
    #                           sum_of_digits_of_sum_of_factors
    #                   function!  Just write these TESTS of that function
    #                   after reading the green doc-string for the
    #                   sum_of_digits_of_sum_of_factors   function below.
    ############################################################################
    print()
    print('---------------------------------------------------------')
    print('Testing the   sum_of_digits_of_sum_of_factors   function:')
    print('---------------------------------------------------------')

    #Test 1:
    expected = 6
    actual = sum_of_digits_of_sum_of_factors(5)
    print()
    print("---------------- Test 1 ----------------")
    print("Expected: ", expected)
    print("Actual:   ", actual)

    # Test 2:
    expected = 15
    actual = sum_of_digits_of_sum_of_factors(8)
    print()
    print("---------------- Test 2 ----------------")
    print("Expected: ", expected)
    print("Actual:   ", actual)

    # Test 3:
    expected = 13
    actual = sum_of_digits_of_sum_of_factors(9)
    print()
    print("---------------- Test 3 ----------------")
    print("Expected: ", expected)
    print("Actual:   ", actual)

    # Test 4:
    expected = 42
    actual = sum_of_digits_of_sum_of_factors(20)
    print()
    print("---------------- Test 4 ----------------")
    print("Expected: ", expected)
    print("Actual:   ", actual)


def sum_of_digits_of_sum_of_factors(n):
    """
    Given a positive integer n,
    returns the sum of the digits of the sum of the factors of n,
    where a FACTOR of n is an integer that divides evenly into n.

    For example, if n is 28, this function returns 11, because:
      -- the factors of n are:
             1  2  4  7  14  28
      -- and the sum of those numbers is   1 + 2 + 4 + 7 + 14 + 28,
             which is 56
      -- and the sum of the digits of 56 is 11,
    so this function returns 11 when n is 28.

       *** ASK FOR AN EXPLANATION IF YOU DO NOT UNDERSTAND THE ABOVE. ***
    """
    ############################################################################
    #  DONE (continued):  This function is PURPOSELY ** not implemented. **
    #  DONE (continued):  DO NOT IMPLEMENT  sum_of_digits_of_sum_of_factors.
    #                     Just leave it as it is (with no code).
    ############################################################################


################################################################################
# DONE: 3.  READ the green doc-string for the   number_of_factors   function
#    defined below.  You do NOT need to understand its implementation,
#    just its specification (per the doc-string).
#    You should  ** CALL **  that function as needed in implementing
#    the other functions.
# DONE (continued):  After you have READ this _TODO_, change its _TODO_ to DONE.
################################################################################

def number_of_factors(n):
    """
    Given a positive integer n, returns the number of factors of n,
    where a FACTOR of n is an integer that divides evenly into n.

    For example, if n is 28, then the factors of n are:
             1  2  4  7  14  28
    so this function returns 6.

       *** ASK FOR AN EXPLANATION IF YOU DO NOT UNDERSTAND THE ABOVE. ***
    """
    if n == 1:  # special case
        return 1

    count = 2  # The number and 1 are factors
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            count = count + 2  # k and (n // k) are factors

    if round(math.sqrt(n)) * round(math.sqrt(n)) == n:
        count = count - 1  # n is a perfect square, the above double-counted

    return count
    ############################################################################
    #  DONE (continued):  Students: Do NOT touch the above   number_of_factors
    #  DONE (continued)   function; CALL it as appropriate in problem(s) below.
    ############################################################################


def run_test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')

    format_string = '    problem2b( {}, {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 16 + 18 + 20 + 24  # which is 78
    print_expected_result_of_test([13, 25, 5], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 5)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 18 + 20 + 24  # which is 62
    print_expected_result_of_test([13, 25, 6], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 6)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 24
    print_expected_result_of_test([13, 25, 7], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 7)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 24
    print_expected_result_of_test([13, 25, 8], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 8)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 0
    print_expected_result_of_test([13, 25, 9], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 9)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 14 + 15 + 16 + 18 + 20 + 21 + 22 + 24  # which is 150
    print_expected_result_of_test([13, 25, 4], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 4)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 14 + 15 + 16 + 18 + 20 + 21 + 22 + 24 + 25  # which is 175
    print_expected_result_of_test([13, 25, 3], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 3)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25
    # which is 247
    print_expected_result_of_test([13, 25, 2], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25
    # which is 247
    print_expected_result_of_test([13, 25, 1], expected, test_results,
                                  format_string)
    actual = problem2b(13, 25, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 1 + 2  # which is 3
    print_expected_result_of_test([1, 2, 1], expected, test_results,
                                  format_string)
    actual = problem2b(1, 2, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 2
    print_expected_result_of_test([1, 2, 2], expected, test_results,
                                  format_string)
    actual = problem2b(1, 2, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 12:
    expected = 0
    print_expected_result_of_test([1, 2, 3], expected, test_results,
                                  format_string)
    actual = problem2b(1, 2, 3)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 13:
    expected = 0
    print_expected_result_of_test([1, 10000, 10000], expected, test_results,
                                  format_string)
    actual = problem2b(1, 10000, 10000)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 14:
    expected = 0
    print_expected_result_of_test([1, 100000, 10000], expected, test_results,
                                  format_string)
    actual = problem2b(1, 100000, 10000)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 15:
    expected = 49350803
    print_expected_result_of_test([1000, 20000, 13], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 13)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 16:
    expected = 49346707
    print_expected_result_of_test([1000, 20000, 14], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 14)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 17:
    expected = 194220
    print_expected_result_of_test([1000, 20000, 72], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 72)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 18:
    expected = 15120 + 18480  # which is 33600
    print_expected_result_of_test([1000, 20000, 73], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 73)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 19:
    expected = 15120 + 18480  # which is 33600
    print_expected_result_of_test([1000, 20000, 80], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 80)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 20:
    expected = 0
    print_expected_result_of_test([1000, 20000, 81], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 81)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 21:
    expected = 414348
    print_expected_result_of_test([1000, 20000, 62], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 62)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 22:
    expected = 414348
    print_expected_result_of_test([1000, 20000, 63], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 63)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 23:
    expected = 414348 - 14400  # which is 399948
    print_expected_result_of_test([1000, 20000, 64], expected, test_results,
                                  format_string)
    actual = problem2b(1000, 20000, 64)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem2b(a, b, x):
    """
    What comes in:  Positive integers a, b and x, with a <= b.
    What goes out:
      -- Returns the sum of all the integers from a to b, inclusive,
           whose number of factors is greater than or equal to x.
    Side effects:   None.
    Examples:
      -- problem1b(13, 25, 5) returns 78 because:
           - 13 has 2 factors (namely: 1, 13)
           - 14 has 4 factors (namely: 1, 2, 7, 14)
           - 15 has 4 factors (namely: 1, 3, 5, 15)
           - 16 has 5 factors (namely: 1, 2, 4, 8, 16)
           - 17 has 2 factors (namely: 1, 17)
           - 18 has 6 factors (namely: 1, 2, 3, 6, 9, 18)
           - 19 has 2 factors (namely: 1, 19)
           - 20 has 6 factors (namely: 1, 2, 4, 5, 10, 20)
           - 21 has 4 factors (namely: 1, 3, 7, 21)
           - 22 has 4 factors (namely: 1, 2, 11, 22)
           - 23 has 2 factors (namely: 1, 23)
           - 24 has 8 factors (namely: 1, 2, 3, 4, 6, 8, 12, 24)
           - 25 has 3 factors (namely: 1, 5, 25)
         so the integers from 13 to 25, inclusive, whose number of factors
         is great than or equal to 5 are: 16, 18, 20, and 24,
         and the sum   16 + 18 + 20 + 24   is 78.
     """
    ############################################################################
    # DONE: 4. Implement and test this function.  See the IMPORTANT NOTE below!
    #          Tests have been written for you (above).
    ############################################################################
    # DONE (continued): IMPORTANT NOTE:
    # DONE (continued):   **  For full credit you must appropriately use
    # DONE (continued):       (i.e., call) the   number_of_factors   function
    #                         that is DEFINED ABOVE.
    ############################################################################
    r = b - a + 1
    total = 0
    for k in range(r):
        if number_of_factors(a + k) >= x:
            total = total + (a + k)
    return total


def run_test_problem2c():
    """ Tests the   problem2c   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2c   function:')
    print('--------------------------------------------------')

    format_string = '    problem2c( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 24  # from 8 to 16:  11 + 13 = 24
    print_expected_result_of_test([7], expected, test_results,
                                  format_string)
    actual = problem1c(7)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 60  # from 11 to 19:  11 + 13 + 17 + 19 = 60
    print_expected_result_of_test([10], expected, test_results,
                                  format_string)
    actual = problem1c(10)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 49  # from 13 to 21:  13 + 17 + 19 = 49
    print_expected_result_of_test([12], expected, test_results,
                                  format_string)
    actual = problem1c(12)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 36  # from 14 to 22:  17 + 19 = 36
    print_expected_result_of_test([13], expected, test_results,
                                  format_string)
    actual = problem1c(13)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 311  # from 100 to 108:  101 + 103 + 107 = 311
    print_expected_result_of_test([99], expected, test_results,
                                  format_string)
    actual = problem1c(99)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 420   # from 101 to 109: 311 + 109 = 420
    print_expected_result_of_test([100], expected, test_results,
                                  format_string)
    actual = problem1c(100)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 319  # from 102 to 110: 420 - 101 = 319
    print_expected_result_of_test([101], expected, test_results,
                                  format_string)
    actual = problem1c(101)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 20016  # computed by running a correct solution
    print_expected_result_of_test([10000], expected, test_results,
                                  format_string)
    actual = problem1c(10000)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 0  # no primes from 20001 to 20009
    print_expected_result_of_test([20000], expected, test_results,
                                  format_string)
    actual = problem1c(20000)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 31541 + 31543 + 31547
    print_expected_result_of_test([31540], expected, test_results,
                                  format_string)
    actual = problem1c(31540)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 31543 + 31547
    print_expected_result_of_test([31541], expected, test_results,
                                  format_string)
    actual = problem1c(31541)
    print_actual_result_of_test(expected, actual, test_results)

    print_summary_of_test_results(test_results)


def problem1c(m, total=0):
    """
    What comes in:  An integer  m  that is at least 2.
    What goes out:
      -- Returns the sum of all the prime numbers p
           such that  p > m  and  p < (m + 10).

         Recall that an integer is PRIME if its only factors are 1 and itself.

           ** SEE THE IMPORTANT NOTE IN THE _TODO_ BELOW. **

    Side effects:   None.
    Examples:
      -- problem1c(7) returns 24 because the prime numbers that are
           bigger than 7 but less than 17 are:
             11 and 13,
           and 11 + 13 = 24.
      -- problem1c(10) returns 60 because the prime numbers that are
           bigger than 10 but less than 20 are:
             11 13 17 19,
           and 11 + 13 + 17 + 19 = 60.
     """
    ############################################################################
    # DONE: 4. Implement and test this function.  See the IMPORTANT NOTE below!
    #          Tests have been written for you (above).
    ############################################################################
    # DONE (continued): IMPORTANT NOTE:
    # DONE (continued):   This problem is 1 point (of 100) on the exam.
    # DONE (continued)    Do not spend more than a few minutes on it.
    # DONE (continued)    You get   NO credit   if your solution is more
    # DONE (continued)    than 3 lines of code (and it can be done in 1 line).
    ############################################################################

    for k in range(m + 1, m + 10):
        if number_of_factors(k) == 2: total = total + k
    return total


################################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
################################################################################

def print_expected_result_of_test(arguments, expected, test_results,
                                  format_string):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string)


def print_actual_result_of_test(expected, actual, test_results, precision=None):
    testing_helper.print_actual_result_of_test(expected, actual, test_results,
                                               precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# ------------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console
# from being intermingled with ordinary output to the console.
# ------------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
