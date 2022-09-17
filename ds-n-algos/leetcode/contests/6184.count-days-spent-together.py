# @author: yprakash
from datetime import datetime


class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        alice1 = datetime.strptime(arriveAlice + "-01", "%m-%d-%y")
        alice2 = datetime.strptime(leaveAlice + "-01", "%m-%d-%y")
        bob1 = datetime.strptime(arriveBob + "-01", "%m-%d-%y")
        bob2 = datetime.strptime(leaveBob + "-01", "%m-%d-%y")

        if alice2 < bob1 or bob2 < alice1:
            return 0
        
