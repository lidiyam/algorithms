"""
Print a maximum set of activities that can be done by a
single person, one at a time

n --> Total number of activities
start[]--> An array that contains start time of all activities
finish[] --> An array that contains finish time of all activities
Assume activities are sorted according to their finish time
"""


class Solution():

    def activity_selection(self, start, finish, n):
        result = [0]
        i = 0
        for j in range(1, n-1):
            if start[j] >= finish[i]:
                result.append(j)
                i = j
        return result


if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print Solution().activity_selection(s, f, len(s))