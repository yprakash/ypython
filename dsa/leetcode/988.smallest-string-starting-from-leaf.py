# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/835583277/
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def smallest(answer, prefix, node):
            prefix = chr(97 + node.val) + prefix

            if node.left:
                smallest(answer, prefix, node.left)
            if node.right:
                smallest(answer, prefix, node.right)
            elif not node.left:  # its leaf node
                if not answer:
                    answer.append(prefix)
                elif prefix < answer[0]:
                    answer[0] = prefix

        answer = []
        smallest(answer, '', root)
        return answer[0]
