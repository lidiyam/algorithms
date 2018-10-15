class Solution(object):

    def binary_arr(self, num):
        arr = []
        while num != 0:
            r = num % 2
            arr.insert(0, r)
            num = num / 2
        return arr

    def hamming_distance(self, num1, num2):
        i_arr = self.binary_arr(num1)
        j_arr = self.binary_arr(num2)
        hamming_dist = 0
        if len(i_arr) > len(j_arr):
            mult = len(i_arr) - len(j_arr)
            j_arr = [0] * mult + j_arr
        elif len(i_arr) < len(j_arr):
            mult = len(j_arr) - len(i_arr)
            i_arr = [0] * mult + i_arr
        for x in range(len(i_arr)):
            if i_arr[x] != j_arr[x]:
                hamming_dist += 1
        return hamming_dist

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                res += self.hamming_distance(nums[i], nums[j])
        return res


if __name__ == '__main__':
    print Solution().totalHammingDistance([4, 14, 2])