from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    tracker = []

    def get_nodes(root: TreeNode):
        if root is None:
            return
        get_nodes(root.left)
        tracker.append(root.val)
        get_nodes(root.right)

    get_nodes(root)
    return tracker

