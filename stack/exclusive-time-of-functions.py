from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0

        for log in logs:
            fid_s, typ, t_s = log.split(':')
            fid, t = int(fid_s), int(t_s)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += t - prev
                stack.append(fid)
                prev = t
            else:  # 'end'
                finished = stack.pop()
                ans[finished] += t - prev + 1
                prev = t + 1

        return ans
