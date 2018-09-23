import sympy

A = sympy.Matrix([[1, 2], [2, -1]])
B = sympy.Matrix([[1, 0, 3], [2, 1, 1]])
C = sympy.Matrix([[1, 2], [3, 1], [2, -1]])
D = sympy.Matrix([[1, 0, 3], [1, 1, -2], [2, -1, 1]])
E = sympy.Matrix([[1], [2], [-1]])
F = sympy.Matrix([[1, 2, 3]])

print(A*B)
print(D**2)
print(D*C)
print(C*B)
print(B*C)
print(F*E)
print(E*F)
print()

C = sympy.Matrix([[2, 3], [1, 2]])
D = sympy.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
E = sympy.Matrix([[3, 0, 2], [2, -1, -2], [-1, 2, 6]])

print(A**-1)
print(C**-1)
print(D**-1)
print()
print((A**-1)*sympy.Matrix([[1], [-2]]))
print((D**-1)*E)
