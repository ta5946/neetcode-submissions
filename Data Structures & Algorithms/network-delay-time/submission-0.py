class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((t, v))

        heap = [(0, k)]  # (current time, node)
        visited = set()
        result = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            result = time
            for t, neighbor in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + t, neighbor))

        return result if len(visited) == n else -1
