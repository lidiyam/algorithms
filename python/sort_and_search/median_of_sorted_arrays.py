

class Solution(object):
    # O(n)
    def merge_arrays(self, arr1, arr2, result):
        if not arr1 and not arr2:
            return result
        if not arr1:
            return result + arr2
        if not arr2:
            return result + arr1
        if arr1[0] <= arr2[0]:
            popped = arr1.pop(0)
            result.append(popped)
            return self.merge_arrays(arr1, arr2, result)
        else:
            popped = arr2.pop(0)
            result.append(popped)
            return self.merge_arrays(arr1, arr2, result)

    def median_of_arrays(self, arr1, arr2):
        length = len(arr1) + len(arr2)
        if length == 0:
            return 0
        sorted_arr = self.merge_arrays(arr1, arr2, [])
        return self.median(sorted_arr)

    def median(self, arr):
        size = len(arr)
        if size % 2 == 0:
            return (arr[size/2 - 1] + arr[size/2]) / 2.0
        else:
            return arr[size/2]

    # O(log n)
    def median_sorted_arrays(self, arr1, arr2):
        if not arr1 or len(arr1) != len(arr2):
            raise Exception
        if len(arr1) == 1:
            return (arr1[0] + arr2[0]) / 2.0
        if len(arr1) == 2:
            return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2.0
        med1 = self.median(arr1)
        med2 = self.median(arr2)
        if med1 == med2:
            return med1
        if med1 > med2:
            end1 = len(arr1) / 2 + 1
            start2 = (len(arr2) - 1) / 2
            return self.median_sorted_arrays(arr1[0:end1], arr2[start2:len(arr2)])
        else:
            start1 = (len(arr1) - 1) / 2
            end2 = len(arr2) / 2 + 1
            return self.median_sorted_arrays(arr1[start1:len(arr1)], arr2[0:end2])




if __name__ == '__main__':
    arr1 = [1, 2, 3, 5]
    arr2 = [0, 0, 9, 9]
    print Solution().median_sorted_arrays(arr1, arr2)