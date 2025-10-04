class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)

        while j < m:
            ch = abbr[j]

            if ch.isalpha():

                if i >= n or word[i] != ch:
                    return False

                i += 1
                j += 1

            else:
                if ch == '0':
                    return False

                num = 0

                while j < m and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1

                i += num
                if i > n:
                    return False
                
        return i == n