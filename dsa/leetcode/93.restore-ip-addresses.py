# @author: yprakash
# https://leetcode.com/problems/restore-ip-addresses/submissions/882149198/

class Solution:
    def restoreIpAddresses(self, s: str):
        ips = []
        if not s or len(s) > 12:
            return ips

        def bt(i, ints):
            if i == len(s):
                if len(ints) == 4:
                    ips.append('.'.join(map(str, ints)))
                return

            # case 1: append curr digit to last number
            last = ints[-1]
            if last > 0 and 10 * last + int(s[i]) <= 255:
                ints[-1] = 10 * last + int(s[i])
                bt(i+1, ints)
                ints[-1] = last

            # case 2: add new number in ints
            if len(ints) < 4:
                bt(i+1, ints + [int(s[i])])

        bt(1, [int(s[0])])
        return ips
