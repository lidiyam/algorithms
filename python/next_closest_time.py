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
    	max_val = [2, 3, 0, 5, 9]
    	nums = set()
    	for c in time:
    		if c == ':': continue
    		nums.add(int(c))

    	digits = sorted(nums)
    	min_digit = str(digits[0])
    	i = 4
    	while i > 0:
    		if i == 2:
    			i -= 1
    		val = int(time[i])
    		for d in digits:
    			if d > val and d <= max_val[i]:
    				time = time[:i] + str(d) + time[i+1:]
    				# append min_digit after index i
    				j = 4
    				while j > i:
    					if j != 2:
    						time = time[:j] + str(min_digit) + time[j+1:]
    					j -= 1
    				return time
    		i -= 1
    				
    	return min_digit + min_digit + ":" + min_digit + min_digit 

if __name__ == '__main__':
	assert Solution().nextClosestTime("19:34") == "19:39"
	assert Solution().nextClosestTime("23:59") == "22:22"
	assert Solution().nextClosestTime("22:19") == "22:21"