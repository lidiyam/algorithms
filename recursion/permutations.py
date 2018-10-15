class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for i, num in enumerate(nums):
            rest = self.permute(nums[:i] + nums[i+1:])
            for lst in rest:
                lst.insert(0, num)
                result.insert(0,lst)
        return result

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for i, num in enumerate(nums):
            rest = self.permuteUnique(nums[:i] + nums[i+1:])
            for lst in rest:
                lst.insert(0, num)
                if lst not in result:
                    result.insert(0,lst)
        return result

    # In every level use a for loop to pick an entry in the array, 
    # delete it from the array, and then do this recursively until the array is empty. 
    # Add permutation to the result list.
    # def permute(self, nums):
    #     lst = []
    #     self.backtrack(lst, [], nums)
    #     return lst


    # def backtrack(self, lst, tempList, nums):
    #     if len(tempList) == len(nums):
    #         lst.append(tempList)
    #         return
    #     for i, num in enumerate(nums):
    #         if num in tempList: continue
    #         tempList.append(num)
    #         self.backtrack(lst, tempList, nums)
    #         tempList = tempList[:len(tempList)]


if __name__ == '__main__':
    #print Solution().permute([1,2,3])
    print Solution().permuteUnique([1,1,2])