class Solution:
    def lowestCommonAncestor(self, p, q):
        if p.val > q.val:
            Up = p
            Low = q
        else:
            Up = q
            Low = p
        return self.LCA_Calc(root, Up, Low)

    def LCA_Calc(self, root, Up, Low):
        if root.val == Up.val:
            return root
        elif root.val == Low.val:
            return root
        elif Up.val > root.val:
            if Low.val < root.val:
                return root
            else:
                return self.LCA_Calc(root.right, Up, Low)
        else:
            return self.LCA_Calc(root.left, Up, Low)
