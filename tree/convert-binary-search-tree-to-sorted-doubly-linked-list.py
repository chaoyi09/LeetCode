class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node | None') -> 'Node | None':
        if not root:
            return None

        dummy = Node(0) 
        prev = dummy
        cur = root

        while cur:
            if not cur.left:
                prev.right = cur
                cur.left = prev
                prev = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    prev.right = cur
                    cur.left = prev
                    prev = cur
                    cur = cur.right

        head = dummy.right
        head.left = prev
        prev.right = head
        return head
