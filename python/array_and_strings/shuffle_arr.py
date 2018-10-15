def shift(A, i, j):
	# shift right by 1
	k = j+1
	while k > i:
		A[k] = A[k-1]
		k -= 1


def shuffle_arr(A, n):
	i = 0
	j = n
	k = n
	while k>0:
		b = A[2*n-k]
		shift(A, i+1, 2*n-k-1)
		A[i+1] = b
		i += 2
		k -= 1


A = [1,3,5,7,2,4,6,8]
shuffle_arr(A, 4)
print A