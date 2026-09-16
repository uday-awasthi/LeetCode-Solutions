
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        if root is None:
            return None

        curr = root

        while curr is not None:
            if curr.val == val:
                return curr

            elif val < curr.val:
                # Search in the left subtree
                curr = curr.left

            else:
                # Search in the right subtree
                curr = curr.right

        return None