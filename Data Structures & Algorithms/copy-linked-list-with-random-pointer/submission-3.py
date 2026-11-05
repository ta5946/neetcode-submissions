class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy_nodes = []
        index = {}
        current = head
        i = 0
        while current:
            copy_node = Node(current.val, None, None)
            copy_nodes.append(copy_node)
            index[current] = i
            current = current.next
            i += 1

        for i in range(len(copy_nodes) - 1):
            copy_nodes[i].next = copy_nodes[i + 1]

        first = head
        i = 0
        while first:
            if first.random:
                copy_nodes[i].random = copy_nodes[index[first.random]]
            first = first.next
            i += 1

        return copy_nodes[0]
