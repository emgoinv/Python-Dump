import math

#prints n rows of Pascal's Triangle
def pascals_triangle(rows):
    length = len(str(n_choose_k(rows, rows/2)))+2
    print_row = ''
    for n in range(0, rows+1):
        for k in range(0, n+1):
            print_row += pascal_format(length, n_choose_k(n, k))
        print print_row
        print_row = ''

#formats an integer as an length-character str
def pascal_format(length, n):
    result = str(n)
    for x in range(0, length-len(str(n))): result += ' '
    return result

#returns n choose k
def n_choose_k(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
