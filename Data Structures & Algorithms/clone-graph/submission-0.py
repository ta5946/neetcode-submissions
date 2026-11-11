class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = self.cloneNode(node, {})
        return clone

    def cloneNode(self, node: Optional['Node'], cloned: dict) -> Optional['Node']:
        if not node:
            return None
        if node in cloned:
            return cloned[node]
        clone = Node(node.val)
        cloned[node] = clone
        for n in node.neighbors:
            c = self.cloneNode(n, cloned)
            clone.neighbors.append(c)
        return clone
