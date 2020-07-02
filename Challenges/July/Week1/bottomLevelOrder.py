class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = [root]
        while q :
            ans.append([x.val for x in q])
            q = [x for n in q for x in (n.left, n.right) if x]
        return ans[::-1]
