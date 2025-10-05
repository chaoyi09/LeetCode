class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        out = []

        turn_word1 = True
        while i < n and j < m:
            if turn_word1:
                out.append(word1[i])
                i += 1
            else:
                out.append(word2[j])
                j += 1
            turn_word1 = not turn_word1

        if i < n:
            out.append(word1[i:])
        if j < m:
            out.append(word2[j:])
        return ''.join(out)