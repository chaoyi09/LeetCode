import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = []
        for s, e in intervals:

            if heap and heap[0] <= s:
                heapq.heapreplace(heap, e)
            else:
                heapq.heappush(heap, e)
        return len(heap)