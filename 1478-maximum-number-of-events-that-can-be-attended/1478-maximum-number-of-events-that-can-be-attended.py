import heapq
from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_day = max(e[1] for e in events)
        events_index = 0
        attended = 0
        min_heap = []

        for day in range (1, max_day+1):
            while events_index < len(events) and events[events_index][0] == day:
                heapq.heappush(min_heap, events[events_index][1])
                events_index+=1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap) 
                attended+=1

        return attended