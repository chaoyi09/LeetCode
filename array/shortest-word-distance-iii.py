class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = index2 = -1
        min_dist = len(wordsDict)
        same = (word1 == word2)
        prev_index = -1

        for i, word in enumerate(wordsDict):
            if same:
                if word == word1:
                    if prev_index != -1:
                        min_dist = min(min_dist, i - prev_index)
                    prev_index = i

            else:
                if word == word1:
                    index1 = i
                elif word == word2:
                    index2 = i

            if index1 != -1 and index2 != -1:
                min_dist = min(min_dist, abs(index1 - index2))

        return min_dist