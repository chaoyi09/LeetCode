class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        res: List[str] = []
        path: List[str] = []

        def dfs(i: int, cnt: int) -> None:
            if i == n:
                if cnt > 0:
                    path.append(str(cnt))
                res.append("".join(path))
                if cnt > 0:
                    path.pop()
                return

            dfs(i + 1, cnt + 1)

            if cnt > 0:
                path.append(str(cnt))
            path.append(word[i])

            dfs(i + 1, 0)

            path.pop()
            if cnt > 0:
                path.pop()

        dfs(0, 0)
        return res