class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        sign_stack = [1]
        sign = 1

        i, n = 0, len(s)
        while i < n:
            ch = s[i]

            if ch == ' ':
                i += 1
                continue

            if ch == '+':
                sign = sign_stack[-1]
                i += 1

            elif ch == '-':
                sign = -sign_stack[-1]
                i += 1

            elif ch == '(':
                sign_stack.append(sign)
                i += 1

            elif ch == ')':
                sign_stack.pop()
                i += 1

            else:
                if ch.isdigit():
                    num = 0
                    while i < n and s[i].isdigit():
                        num = num * 10 + (ord(s[i]) - 48)
                        i += 1
                    ans += sign * num
                else:
                    i += 1

        return ans
