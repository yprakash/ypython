# @author: yprakash
import copy


class Solution(object):
    # https://leetcode.com/submissions/detail/807183495/
    def pathSum(self, root, targetSum):
        result = []
        if not root:
            return result

        def path_sum(node, path, parent_sum):
            parent_sum += node.val
            path.append(node.val)
            if node.left:
                path_sum(node.left, path, parent_sum)

            if node.right:
                path_sum(node.right, path, parent_sum)
            elif not node.left:  # if leaf node
                if parent_sum == targetSum:
                    result.append(copy.deepcopy(path))

            path.pop()  # list.pop(0) is O(n) but list.pop() is O(1)

        path_sum(root, [], 0)
        return result
