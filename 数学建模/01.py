# 请关闭中文输入法，用英文的字母和标点符号。
# 如果你想运行系统测试用例，请点击【执行代码】按钮，如果你想提交作答结果，请点击【提交】按钮，
# 注意：除答案外，请不要打印其他任何多余的字符，以免影响结果验证
# 本OJ系统是基于 OxCoder 技术开发，网址：www.oxcoder.com
# 模版代码提供基本的输入输出框架，可按个人代码习惯修改

class Solution:
    def __init__(self) -> None:
        pass

    def solution(self, n, arr):
        result = None

        # TODO: 请在此编写代码
        a=arr
        for i in range(len(a) - 1):
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    m = a[i]
                    a[i] = a[j + 1]
                    a[j + 1] = m
        result = a

        return result


if __name__ == "__main__":
    n = int(input().strip())

    arr = [int(item) for item in input().strip().split()]

    sol = Solution()
    result = sol.solution(n, arr)

    print(result)

