# 分支定界.py
# coding=utf-8
import sys
import math
from scipy.optimize import linprog


def integerPro(c, A, b, Aeq, beq, t=1.0E-12):
    res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq)

    if (res.success != True):
        bestX = [sys.maxsize] * len(c)
    else:
        bestX = res.x
    bestVal = sum([x * y for x, y in zip(c, bestX)])
    # 停止条件 & bound
    if all(((x - math.floor(x)) < t or (math.ceil(x) - x) < t) for x in bestX):
        return (bestVal, bestX)
    else:
        # 进行branch，这里简单选择第一个非整数变量
        ind = [i for i, x in enumerate(bestX) if (x - math.floor(x)) > t \
               and (math.ceil(x) - x) > t][0]
        # branch出两个子问题
        newCon1 = [0] * len(A[0])
        newCon2 = [0] * len(A[0])
        newCon1[ind] = -1
        newCon2[ind] = 1
        newA1 = A.copy()
        newA2 = A.copy()
        newA1.append(newCon1)
        newA2.append(newCon2)
        newB1 = b.copy()
        newB2 = b.copy()
        newB1.append(-math.ceil(bestX[ind]))
        newB2.append(math.floor(bestX[ind]))
        r1 = integerPro(c, newA1, newB1, Aeq, beq)
        r2 = integerPro(c, newA2, newB2, Aeq, beq)
        # tree search，这里使用width first
        if r1[0] < r2[0]:
            return r1
        else:
            return r2


c = [3, 4, 1]
A = [[-1, -6, -2], [-2, 0, 0]]
b = [-5, -3]
Aeq = [[0, 0, 0]]
beq = [0]
print(integerPro(c, A, b, Aeq, beq))
