
# Time: O(n), Space: O(n)
def two_sum(arr, m):
    d = {}
    for i in xrange(len(arr)):
        if m - arr[i] in d:
            return (d[m-arr[i]], i)
        else:
            d[arr[i]] = i
    return (-1, -1)

# while i < len(ab) and j >= 0:
#             total = ab[i] + cd[j]
#             if total > 0:
#                 j -= 1
#             elif total < 0:
#                 i += 1
#             else:
#                 x = i
#                 y = j
#                 while x+1 < len(ab) and ab[x+1] == ab[i]:
#                     x += 1
#                 while y > 0 and cd[y-1] == cd[j]:
#                     y -= 1
#                 count_4sum += (x-i+1) * (j-y+1)
#                 i = x + 1
#                 j = y - 1

def threeSum(self, nums2):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums2)
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            i = i+1
            target = -num
            j = len(nums) - 1
            while i < j:
                total = nums[i] + nums[j]
                if total == target:
                    res.append([num, nums[i], nums[j]])
                    while i+1 < j and nums[i] == nums[i+1]:
                        i += 1
                    while j > 0 and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif total < target:
                    i += 1
                else:
                    j -= 1
            
        return res


# Time: O(n)
def two_sum_sorted(arr, m):
    i = 0
    j = len(arr)

    while i <= j:
        s = arr[i] + arr[j]
        if s < m:
            i += 1
        elif s > m:
            j -= 1
        else:
            return (i, j)
    return (-1, -1)


# Find i, j, k such that the sum is m
# Time: O(n^2)
def three_sum(arr, m):
    for i in xrange(len(arr)):
        (j, k) = two_sum_sorted(arr, m-arr[i])
        if (j, k) != (-1, -1):
            return (i, j, k)
        else:
            continue
    return (-1, -1, -1)



triple = three_sum([2,4,7,9,11,30], 38)
print triple


