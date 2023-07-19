# coding=utf-8
from scipy.optimize import linprog


c = [-2, -3, 5]
A = [[-2, 5, -1], [1, 3, 1]]
b = [-10, 12]
Aeq = [[1, 1, 1]]
beq = [7]
x = linprog(c, A, b, Aeq, beq, method="highs", bounds=[[0, None], [0, None], [0, None]])
print(x.fun)
