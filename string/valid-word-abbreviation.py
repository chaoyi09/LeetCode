class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)

        while j < m:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1
                i += num
                if i > n:
                    return False
            else:
                if i >= n or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == n