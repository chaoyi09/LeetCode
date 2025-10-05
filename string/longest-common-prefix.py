class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        out = []

        for column in zip(*strs):
            if len(set(column)) == 1:
                out.append(column[0])
            else:
                break
        return "".join(out)