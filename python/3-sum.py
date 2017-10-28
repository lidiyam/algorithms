
# Time: O(n), Space: O(n)
def two_sum(arr, m):
    d = {}
    for i in xrange(len(arr)):
        if m - arr[i] in d:
            return (d[m-arr[i]], i)
        else:
            d[arr[i]] = i
    return (-1, -1)


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
        (j, k) = two_sum(arr, m-arr[i])
        if (j, k) != (-1, -1):
            return (i, j, k)
        else:
            continue
    return (-1, -1, -1)



triple = three_sum([2,4,7,9,11,30], 38)
print triple


