
from typing import List
from heapq import heappush, heappop
from sortedcontainers import SortedList

class Solution:
    def busiestServers(
        self, k: int, arrival: List[int], load: List[int]
    ) -> List[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Release servers that have finished
            while busy and busy[0][0] <= time:
                finish, server = heappop(busy)
                available.add(server)

            # Drop request if all servers are busy
            if not available:
                continue

            # Preferred server is i % k
            preferred = i % k

            # Find first available server >= preferred
            pos = available.bisect_left(preferred)

            # Wrap around if needed
            if pos == len(available):
                pos = 0

            server = available.pop(pos)

            # Count successfully handled requests
            count[server] += 1

            # Mark server as busy
            heappush(busy, (time + load[i], server))

        max_requests = max(count)

        return [
            i for i in range(k)
            if count[i] == max_requests
        ]
