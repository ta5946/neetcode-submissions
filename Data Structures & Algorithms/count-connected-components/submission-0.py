class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = [[i] for i in range(n)]
        for e in edges:
            for c in components:
                if e[0] in c:
                    sc = c
                if e[1] in c:
                    lc = c
            if sc is not lc:
                components.remove(lc)
                sc.extend(lc)
        return len(components)
