class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            distances.append((self.distance(p[0], p[1]), p))
        distances = sorted(distances, key=lambda d: d[0])
        return [p for _, p in distances[:k]]

    def distance(self, x, y):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
