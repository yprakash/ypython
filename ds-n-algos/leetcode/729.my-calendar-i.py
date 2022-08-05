# author: yprakash

class MyCalendar(object):
    def __init__(self):
        self.books = []

    # https://leetcode.com/submissions/detail/764351822/
    # Using Naive linear search O(N^2)
    def book(self, start, end):
        for s, e in self.books:
            if s < end and start < e:
                return False

        self.books.append((start, end))
        return True


testcases = [
    [[10, 20], [15, 25], [20, 30]]
]
for testcase in testcases:
    obj = MyCalendar()
    for pair in testcase:
        print(obj.book(pair[0], pair[1]))
    print('============')
