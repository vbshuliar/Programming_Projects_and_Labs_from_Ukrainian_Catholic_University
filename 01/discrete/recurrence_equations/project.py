'''Recurrent equations solver'''
from time import time
from typing import List
import numpy as np


def main_info_start():
    '''The main function to start'''
    print(
        '''__________________________________________________________________________________________
    This program is created to solve homogeneous linear recurrence equations.
    To start the program, type the exact amount of coefficients needed.
    Coefficients are represented by integers to which we multiply the
    corresponding members of the recurrent sequence.
    For example:
    >>> 1 3 0 -1
    Program perceives this equation : 1 * a[n] = 3 * a[n - 1] + 0 * a[n - 2] -1 * a[n - 3],
    where a[k] is the member of recurrence sequence.
    TO EXIT THE PROGRAM, TYPE <CTRL + C>''')
    print('__________________________________________________________________________________________')


def input_coeffs_inits():
    '''User inputs data to build a sequence'''
    nums = '0123456789-'

    def conduct_eq(coeffslst: List[str]):
        equation = ''
        for num, coef in enumerate(coeffslst):
            if len(coeffslst) == 1:
                equation += f'{coef} * a[n] = 0'
            elif num == 0:
                if int(coef) == 0:
                    equation += ''
                elif int(coef) > 0:
                    equation += f'{coef} * a[n] ='
                else:
                    equation += f'{coef} * a[n] ='
            else:
                if int(coef) == 0:
                    equation += ' 0'
                    # pass
                elif int(coef) > 0:
                    equation += f' + {coef} * a[n - {num}]'
                else:
                    equation += f' - {abs(int(coef))} * a[n - {num}]'
        equation = equation.replace('= +', '=')
        return equation

    def variables():
        '''A function to input coefficients.'''
        print("    Enter the correct coefficients:")

        coeffslst = input('>>> ').split()
        coeffsstr = ''.join(coeffslst)
        assertlst = [i not in nums for i in coeffsstr]

        return assertlst, coeffslst

    assertlst, coeffslst = variables()
    while True in assertlst:
        if True in assertlst:
            assertlst, coeffslst = variables()
            # break
    equation = conduct_eq(coeffslst)
    print('    Our program received this:',
          equation,
          '''
    Is it the exact equation?
    Press t or f''')

    asserteq = ''
    while asserteq != 't' or asserteq != 'f':
        asserteq = input('>>> ')
        if asserteq == 'f':
            input_coeffs_inits()
        elif asserteq == 't':
            break
    for idx, elem in enumerate(coeffslst):
        if idx == 0:
            coeffslst[idx] = int(elem)
        else:
            coeffslst[idx] = -1 * int(elem)
    # return coeffslst
    print("    Now the last step.")
    print(f'    Enter initial values for the members of sequence.')
    print("""    Example for three values:
    ___________________________________________________________
    >>> 0 1 3
    Program perceives it as: a[0] = 0 ; a[1] = 1 ; a[2] = 3
    ___________________________________________________________""")
    print(f'    Enter first {len(coeffslst) - 1} initial values:')

    lsttemp = ''
    if len(coeffslst) == 1:
        return print("No cases")
    lstvalue = []
    while len(lsttemp) != len(coeffslst) - 1:
        while True:
            try:
                lsttemp = input(">>> ").split()
                for value in lsttemp:
                    lstvalue.append(int(value))
                break
            except:
                continue
    return coeffslst, lstvalue


def perform_task():
    '''Performs tasks.'''
    print('___________________________________________________________\
_______________________________')
    print('    What task do you want us to perform?')
    print('    1) Calculate the n\'th member of the sequence - press 1')
    print('    2) Calculate first n members of the sequence - press 2')
    print('    3) To find the general view of the sequence - press 3')
    task = input('>>> ')
    assert task == '1' or task == '2' or task == '3'
    print('_____________________________________________________________\
_____________________________')
    if task == '1' or task == '2':
        print('    What algorithm do you want us to use?')
        print('    1) Use the general view of the sequence - press 1')
        print('    2) Use the matrix multiplying (O(k + log(n))) - press 2')
        print('    3) Compare the speed of both above - press 3')
        method = input('>>> ')
        assert method == '1' or method == '2' or method == '3'
    print('____________________________________________________________\
______________________________')
    if task == '1' or task == '2':
        print('    Enter the n number:')
        number = int(input('>>> '))
    # Task1
    if task == '1':
        coeffs, initials = input_coeffs_inits()
        roots = solve_equation(coeffs)
        print('    The n\'th member:')
        if method == '1':
            print('\t', calc_nth_member(get_general_view(
                roots, solve_linalg_system(roots, initials)), number))
        elif method == '2':
            coeffs.reverse()
            print('\t', log_calculation(
                opposite_coeffs(coeffs), initials, number))
        else:
            print(
                f'    Time consumption of first method is \
{runtime(calc_nth_member, get_general_view(roots, solve_linalg_system(roots, initials)), number)} seconds.')
            print(
                f'    Time consumption of second method is \
{runtime(log_calculation, opposite_coeffs(coeffs), initials, number)} seconds.')
    # Task 2
    if task == '2':
        coeffs, initials = input_coeffs_inits()
        print('    First n members:')
        if method == '1':
            print('    ', first_n_elements(coeffs, initials, number))
        elif method == '2':
            coeffs.reverse()
            print('    ', first_n_elements_log(
                opposite_coeffs(coeffs), initials, number))
        else:
            print(
                f'    Time consumption of first method is \
{runtime(first_n_elements, coeffs, initials, number)} seconds.')
            print(
                f'    Time consumption of second method is\
 {runtime(first_n_elements_log, opposite_coeffs(coeffs), initials, number)} seconds.')
    # Task 3
    if task == '3':
        coeffs, initials = input_coeffs_inits()
        print('    The general view of the reccurence equation:')
        print(solve_recurrence_equation(coeffs, initials))
    print('_________________________________________________________\
_________________________________')


def correct_roots(roots: list, epsilon=0.0001):
    '''
        Corrects the given roots to integers, if can.
        >>> correct_roots([1.9999999, 2.00000001])
        [2, 2]
        >>> correct_roots([1.001, 9.99999993, 2.000001, 5.9999999999,\
               58.00000000001])
        [1.001, 10, 2, 6, 58]
    '''
    result = []
    for each in roots:
        if abs(each - round(each)) < epsilon:
            result.append(round(each))
        else:
            result.append(each)

    return result


def solve_linalg_system(roots: list, initials: list):
    '''
        Solves the system of linear equations.
        >>> solve_linalg_system([1, 3], [2, 7])
        [-0.5, 2.5]
        >>> solve_linalg_system([2, 2, 3], [4, 10, 40])
        [-12.0, -7.0, 16.0]
    '''
    equations = []
    results = initials
    # Building a system of len(initials) equations:
    for num in range(len(initials)):
        coeffs = []
        for i, root in enumerate(roots):
            if root in roots[:i]:
                coeff = (root ** num) * num ** roots[:i].count(root)
            else:
                coeff = root ** num
            coeffs.append(coeff)
        equations.append(coeffs)
    result = np.linalg.solve(equations, results)

    return list(result)


def get_general_view(roots: list, coeffs: list):
    '''
        Returns the general formula of the homogeneous
        recurrence equation.
        >>> get_general_view([2, 2, 3], [-12.0, -7.0, 16.0])
        '-12.0 * (2)**n - 7.0 * (2)**n * n**1 + 16.0 * (3)**n'
        >>> get_general_view([2, 2], [1, 5])
        '1 * (2)**n + 5 * (2)**n * n**1'
    '''
    result = ''
    for i, root in enumerate(roots):
        if root in roots[:i]:
            result += f'{coeffs[i]} * ({root})**n * n**{roots[:i].count(root)} + '
        else:
            result += f'{coeffs[i]} * ({root})**n + '
    result = result.replace('+ -', '- ')

    return result[:-3]


def solve_recurrence_equation(coeffs: list, initials: list):
    '''
        Returns the final formula of the recurrence sequence
        without recurrence variables.
    '''
    roots = solve_equation(coeffs)

    return get_general_view(roots, solve_linalg_system(roots, initials))
# ==================|Task 2|==================


def solve_equation(coeffs: list):
    '''
        Finds the roots of the equation. Equation is
        represented by coefficients near the variable
        in the corresponding degree.
        >>> solve_equation([1, 5, 6])
        [-3, -2]
        >>> solve_equation([1, -7, -2, 46, 65, 25])
        [-1, -1, -1, 5, 5]
    '''
    result = []
    function_checker = False
    # Reversing the list of coefficients for np
    coeffs.reverse()
    roots = np.polynomial.Polynomial(coeffs)
    list_roots = list(roots.roots())  # create list with roots

    for elem in list_roots:
        if 'j' in str(elem):
            result = real_roots(list_roots)
            function_checker = True
            break
    if len(result) == 0 and not function_checker:
        return correct_roots(list_roots)

    return result


def real_roots(roots: list, min_grade=-1.32):
    '''
        Deletes 'j' from root (the element of roots list),
        if it is close to real number and does nothing
        with root otherwise. The precision of verification is
        up to min_grade value: if it's too small - many roots will
        be lost, if it's too big - the risk of detection of complex
        root as a real will occur.
        Returns the 'cleared' roots - see correct_roots() definition.
        >>> real_roots([1+0.00001j, 2-0.1j])
        [1]
    '''
    finished_lst = []
    for item in roots:
        item = complex(item)
        if abs(item.imag) < 10**min_grade:
            finished_lst.append(item.real)

    return correct_roots(finished_lst)


# ==================|Task 3|==================


def calc_nth_member(formula: str, number: int, verbose=False):
    '''
        Evaluates the number'th member of the sequence,
        described by formula.
        >>> calc_nth_member('2**n+n*2**n', 3)
        32
    '''
    if verbose:
        start = time()
    result = correct_roots([eval(formula.replace('n', f'({number})'))])[0]

    return result if not verbose else (result, time() - start)


def first_n_elements(coeffs, initials, number: int, verbose=False):
    '''Evaluates first n elements'''
    if verbose:
        start = time()
    result = []
    general_view = solve_recurrence_equation(coeffs, initials)
    for num in range(number):
        result.append(calc_nth_member(general_view, num))

    return result if not verbose else (result, time() - start)


# ==================|Task 4|==================


def opposite_coeffs(coeffs: list):
    '''Opposite coeffs.'''
    result = []
    for each in enumerate(coeffs):
        if each[0] == 0:
            result.append(each[1])
        else:
            result.append(-each[1])

    return result


def matrix_power(matrix, power):
    '''
        Returns matrix in appropriate power.
        >>> matrix_power(np.array([[3.0, -1.0, 0.0, 9.0], [1, 0, 0, 0], \
             [0, 1, 0, 0], [0, 0, 1, 0]]), 4)
        array([[ 64.,   6.,  72., 189.],
               [ 21.,   1.,  27.,  72.],
               [  8.,  -3.,   9.,  27.],
               [  3.,  -1.,   0.,   9.]])
        >>> matrix_power(np.array([[5, 7, 0.0, -20], [1, 0, 0, 0], \
             [0, 1, 0, 0], [0, 0, 1, 0]]), 4)
        array([[ 1179.,  1265.,  -640., -3900.],
               [  195.,   204.,  -100.,  -640.],
               [   32.,    35.,   -20.,  -100.],
               [    5.,     7.,     0.,   -20.]])
    '''
    if power == 1:
        return matrix
    if power % 2 == 1:
        return matrix_power(matrix, power - 1).dot(matrix)
    matrix = matrix_power(matrix, power / 2)

    return matrix.dot(matrix)


def log_calculation(coef: list, initials: list, num: int, verbose=False):
    '''
        Function use matrix to calculate n-th member.
        >>> log_calculation([1, 3, -1, 0, 9], [-1, 3, 4, 1], 7)
        115.0
        >>> log_calculation([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1111], \
            [-1, 3, 4, 1, 0, 0, 6, 89, 99, 10], 10)
        -899.0
        >>> log_calculation([1, 1, 1, 0, 9], [1, 0, 0, 0], 4)
        9.0
        >>> log_calculation([4, 4, -1], [1, 0], 2)
        -0.25
    '''
    if verbose:
        start = time()
    if num == 0:
        return initials[0]
    coef_matrix = []
    initials.reverse()
    coef_matrix.append(coef[1:])
    coef_amount = len(coef_matrix[0])
    coef_matrix[0][0] /= coef[0]

    for i in range(coef_amount - 1):
        matrix_part = [0] * coef_amount
        matrix_part[i] = 1
        coef_matrix.append(matrix_part)
        coef_matrix[0][i + 1] /= coef[0]
    new_coef = matrix_power(np.array(coef_matrix),
                            num).dot(np.array(initials))

    return new_coef[-1] if not verbose else (new_coef[-1], time() - start)


def first_n_elements_log(coef: list, initials: list,
                         number: int, verbose=False):
    '''First n elements log.'''
    if verbose:
        start = time()
    result = []
    for num in range(number):
        result.append(log_calculation(coef, initials, num))

    return result if not verbose else (result, time() - start)


# ==================|Task 5|==================


def runtime(func, *args):
    '''
        Evaluates function runtime.
        >>> round(runtime(print, 10, 20))
        10 20
        0
    '''
    start = time()
    func(*args)

    return time() - start


def main():
    '''The main() function.'''
    main_info_start()
    while True:
        try:
            perform_task()
        except KeyboardInterrupt:
            print('\nThanks for choosing us. Bye!')
            print('Ohurchiki Inc, 2021. All rights reserved®.')
            break
        except Exception as err:
            print(err)
            print('You did something wring. Please, try again.')


if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    main()
