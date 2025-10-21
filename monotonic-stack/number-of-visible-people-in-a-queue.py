class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            visible_count = 0

            while stack and stack[-1] < heights[i]:
                stack.pop()
                visible_count += 1
            
            if stack:
                visible_count += 1
            
            answer[i] = visible_count

            stack.append(heights[i])

        return answer