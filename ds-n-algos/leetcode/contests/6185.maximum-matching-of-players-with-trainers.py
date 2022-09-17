# @author: yprakash

class Solution(object):
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
