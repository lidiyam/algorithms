import sys


class Solution(object):

    def reverse_integer(self, x):
        if x < 0:
            return -self.reverse_integer(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x = x / 10
        return result if result <= sys.maxint else 0  # Handle overflow


if __name__ == '__main__':
    result = Solution().reverse_integer(-123)
    print result