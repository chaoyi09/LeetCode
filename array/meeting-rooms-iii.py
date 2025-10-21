class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []

        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                earliest_end, room = heapq.heappop(busy)

                new_end = earliest_end + (end - start)
                heapq.heappush(busy, (new_end, room))
            count[room] += 1

        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i