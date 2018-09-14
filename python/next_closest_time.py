# Time:  O(1)
# Space: O(1)

# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
#
# Ex 3:
# Input: "22:19"
# Output: "22:21"


class Solution(object):        
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        
        Simulate the clock going forward by one minute. 
        Each time it moves forward, if all the digits are allowed, then return the current time.
        """
        HH, MM = time.split(":")
        hh, mm = int(HH), int(MM)
        allowed = set([hh/10, hh%10, mm/10, mm%10])
        curr = hh*60 + mm
        
        def check(t):
            hour = t / 60
            minute = t % 60
            digits = [hour/10, hour%10, minute/10, minute%10]
            for d in digits:
                if d not in allowed:
                    return False
            return True
                    
        for t in range(curr+1, 24*60):
            if check(t):
                return '{0:02d}'.format(t / 60) + ":" + '{0:02d}'.format(t % 60)
        
        for t in range(0, curr+1):
            if check(t):
                return '{0:02d}'.format(t / 60) + ":" + '{0:02d}'.format(t % 60)
        return ""

if __name__ == '__main__':
	assert Solution().nextClosestTime("19:34") == "19:39"
	assert Solution().nextClosestTime("23:59") == "22:22"
	assert Solution().nextClosestTime("22:19") == "22:21"
