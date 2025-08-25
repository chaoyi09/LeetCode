from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        deNum = deque()
        deOp  = deque()

        def calc(a: int, b: int, op: str) -> int:
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b)
            return 0

        opFlag = 0
        i, n = 0, len(s)

        while i < n:
            ch = s[i]
            if ch in "*/":
                opFlag = 1
                deOp.append(ch)
                i += 1
            elif ch in "+-":
                j = i - 1
                while j >= 0 and s[j] == ' ':
                    j -= 1
                if j < 0 or s[j] in "+-*/":
                    sign = -1 if ch == '-' else 1
                    i += 1
                    while i < n and s[i] == ' ':
                        i += 1
                    start = i
                    while i < n and s[i].isdigit():
                        i += 1
                    num = int(s[start:i]) * sign
                    deNum.append(num)
                    if opFlag == 1:
                        opFlag = 0
                        a = deNum.pop()
                        b = deNum.pop()
                        op = deOp.pop()
                        deNum.append(calc(b, a, op))
                else:
                    deOp.append(ch)
                    i += 1
            elif ch == ' ':
                i += 1
            else:
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                deNum.append(num)
                if opFlag == 1:
                    opFlag = 0
                    a = deNum.pop()
                    b = deNum.pop()
                    op = deOp.pop()
                    deNum.append(calc(b, a, op))

        while deOp:
            a = deNum.popleft()
            b = deNum.popleft()
            op = deOp.popleft()
            deNum.appendleft(calc(a, b, op))

        return deNum[0] if deNum else 0
