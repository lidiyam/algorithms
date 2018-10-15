

# arr: array of integers representing length of each word, k: max sum count
# return the length of the longest phrase, chars count is <= k
# e.g. "I am Bob": arr = [1, 2, 3], k = 3 => 2 for [1, 2]
def max_length(arr, k):
    max_len = 0
    for i in range(0, len(arr)):
        sub_sum = 0
        for j in range(i, len(arr)):
            sub_sum += arr[j]
            if sub_sum > k:
                sub_sum = 0

    return max_len


if __name__ == '__main__':
    arr = [1, 2, 3]
    k = 3
    print max_length(arr, k)