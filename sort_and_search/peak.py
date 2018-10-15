# Find peak in the array in O(log n)

def find_peak(A, l, h):
	mid = l + (h-l) / 2

	if h == l:
		print(A[l])

	if h-l == 1:
		print(max(A[l], A[h]))

	while l <= h:

	i = mid
	if i != l and i != h:
		left = A[i-1]
		right = A[i+1]
		if A[i] >= left and A[i] >= right:
			print A[i]
			find_peak(A,l,i-2)
			find_peak(A,i+2,h)
	elif i != l:
		left = A[i-1]
		if A[i] >= left:
			print A[i]
			find_peak(A,l,i-2)
	elif i != h:
		right = A[i+1]
		if A[i] >= right:
			print A[i]
			find_peak(A,i+2,h)
	else:
		print A[i]

A = [3, 1, 5, 2, 6]
#find_peak(A,0,4)

B = [5, 3, 6, 2, 1]
find_peak(B,0,4)