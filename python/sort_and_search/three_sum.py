class Solution(object):
    def twoSum(self, nums, target, i):
        j = len(nums) - 1
        res = []
        while i < j:
            total = nums[i] + nums[j]
            if total == target:
                pair = [nums[i], nums[j]]
                res.append(pair)
                i += 1
                j -= 1
            elif total < target:
                i += 1
            else:
                j -= 1
        return res
            
    def threeSum(self, nums2):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums2)
        for i, num in enumerate(nums):
            doubles = self.twoSum(nums, -num, i+1)
            for two in doubles:
                two.insert(0, num)
                result.append(two)
            result = [[num].extend(two) for two in doubles]
        return result  

if __name__ == '__main__':
    print Solution().threeSum([3,0,-2,-1,1,2])
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([0,0])