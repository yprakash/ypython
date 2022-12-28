# @author: yprakash

class Solution(object):
    # https://leetcode.com/contest/biweekly-contest-87/submissions/detail/802069539/
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        p, t, res = 0, 0, 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                p += 1
                res += 1

            t += 1
        return res
