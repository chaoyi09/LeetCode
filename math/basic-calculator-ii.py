
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        num = 0
        last = 0
        ans = 0
        sign = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + ord(ch) - 48
            if not ch.isdigit() or i == len(s) - 1:
                if i == len(s) - 1 and ch.isdigit():

                    pass
                match sign:
                    case '+':
                        ans += last
                        last = num
                    case '-':
                        ans += last
                        last = -num
                    case '*':
                        last = last * num
                    case '/':
                        last = int(last / num)
                sign = ch
                num = 0
        return ans + last
