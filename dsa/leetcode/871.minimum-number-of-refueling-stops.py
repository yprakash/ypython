# @author: yprakash

class Solution(object):
    # https://leetcode.com/submissions/detail/778812537/
    # Accepted
    def minRefuelStops(self, target, startFuel, stations):
        n = len(stations)
        dp = [0] * (n+1)
        dp[0] = startFuel

        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] < stations[i][0]:
                    break
                if dp[j+1] < dp[j] + stations[i][1]:
                    dp[j+1] = dp[j] + stations[i][1]

        for i, fuel in enumerate(dp):
            if fuel >= target:
                return i

        return -1

    # https://leetcode.com/submissions/detail/778795803/
    # Wrong Answer
    def minRefuelStops2(self, target, startFuel, stations):
        # stops = self.min_refuel_stops(stations, target, 0, 0, startFuel)
        # return -1 if stops > len(stations) else stops
        stations.append([target, 0])  # append target as station
        stops = len(stations)
        fuel = [0] * stops  # accumulated fuel array
        stops = [stops] * stops
        j = 0
        while j < len(stations) and startFuel >= stations[j][0]:
            stops[j] = 0
            fuel[j] = startFuel
            j += 1  # should be the last statement

        for i in range(len(stops)):
            # when we stop and refuel at i-th station
            # find how many next stations we can reach from i
            for j in range(i+1, len(stops)):
                if fuel[i] + stations[i][1] < stations[j][0]:
                    # If accumulated fuel till i is not sufficient to reach j
                    break
                if stops[j] > 1 + stops[i]:
                    stops[j] = 1 + stops[i]
                    fuel[j] = fuel[i] + stations[i][1]

        print(fuel)
        print(stops)
        print(stations)
        return -1 if stops[-1] >= len(stations) else stops[-1]

    # https://leetcode.com/submissions/detail/778451339/
    # Wrong Answer: Recursive recurrence relation
    def min_refuel_stops1(self, stations, target, index, prev_pos, curr_fuel):
        if target <= curr_fuel:
            return 0
        if index >= len(stations) or curr_fuel < stations[index][0]:
            # If current fuel is not sufficient to reach current position
            return 2 + len(stations)  # return some impossible number bigger than no.of stations

        dont_stop = self.min_refuel_stops(stations, target, index+1, prev_pos, curr_fuel)  # as if there is NO station
        stop_here = 1 + self.min_refuel_stops(stations, target, index+1, stations[index][0],
                                              curr_fuel + stations[index][1] + (prev_pos - stations[index][0]))
        return min(stop_here, dont_stop)


if __name__ == "__main__":
    testcases = [
        [1, 1, []],  # 0
        [100, 1, [[10, 100]]],  # -1
        [100, 50, [[25, 25], [50, 50]]],  # 1
        [100, 25, [[25, 25], [50, 25], [75, 25]]],  # 3
        [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]],  # 2
        [1000, 83, [[47, 220], [65, 1], [98, 113], [126, 196], [186, 218],
                    [320, 205], [686, 317], [707, 325], [754, 104], [781, 105]]]  # 4
    ]
    obj = Solution()
    for testcase in testcases:
        print(obj.minRefuelStops(testcase[0], testcase[1], testcase[2]))
