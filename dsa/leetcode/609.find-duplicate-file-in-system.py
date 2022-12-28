# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/803660912/
    def findDuplicate(self, paths):
        texts = {}
        for path in paths:
            subs = path.split(' ')
            for s in subs[1:]:
                file_name = subs[0] + '/' + s[:s.find("(")]
                content = s[s.find("(")+1:s.find(")")]

                if content not in texts:
                    texts[content] = []
                texts[content].append(file_name)

        return [texts[content] for content in texts if len(texts[content]) >= 2]
