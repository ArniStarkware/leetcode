from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        fathers_for_left_kids = []
        cur = None
        for n in preorder:
            if not cur:
                cur = TreeNode(val= n)
                root = cur
                fathers_for_left_kids.append(cur)
            elif n < fathers_for_left_kids[-1].val:
                cur.left = TreeNode(val= n)
                cur = cur.left
                fathers_for_left_kids.append(cur)
            else:
                while fathers_for_left_kids and n > fathers_for_left_kids[-1].val:
                    cur = fathers_for_left_kids.pop()
                    # By Lucky chance, this is perfect.
                cur.right = TreeNode(val= n)
                cur = cur.right
                # Shit
                fathers_for_left_kids.append(cur)
        return root




# Best time solution from online:

class Solution:
    def bstFromPreorder(self, pre_order: List[int]) -> TreeNode:
        iterator = iter(pre_order)
        root = current = TreeNode(next(iterator))
        # Using an iterator is a nice treak, when the first elment of the iterable has some specific behavior.
        for val in iterator:
            node = TreeNode(val)
            if node.val < current.val:
                node.right = current
                current.left = current = node
            else:
                while current.right is not None and node.val > current.right.val:
                    current.right, current = None, current.right

                node.right = current.right
                current.right = current = node

        while current.right is not None:
            current.right, current = None, current.right

        return root


# a nice solution that uses very little space complexity
# will this not have terrible space complexity in extream situations?
# Well, what are the extream situations and how does python deals with them...
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        #important
        
        if not preorder:
            return None
        
        val = preorder.pop(0)        
        root = TreeNode(val)
        
        i = 0
        
        while i < len(preorder):            
            if val < preorder[i]:
                break
            i += 1
            
        root.left = self.bstFromPreorder(preorder[:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        return root
            
            