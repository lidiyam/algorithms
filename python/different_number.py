def get_different_number(arr):
    n = len(arr)
    temp = 0
    
    for i in range(n):  # count sort: O(n)
        temp = arr[i]
        while temp < n and arr[temp] != temp:   # every number is at most moved once
            # swap(temp, arr[temp])
            t = arr[temp]
            arr[temp] = temp
            temp = t
        
    for i in range(n):
        if arr[i] != i:
            return i
    return n


if __name__ == '__main__':
    print get_different_number([7,1,3,0])