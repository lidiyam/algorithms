def dp_alignmt(A, X, Y, gap, match):
	m = len(X)
	n = len(Y)

	for i in range(m):
		A[i][0] = i*gap

	for j in range(n):
		A[0][j] = j*gap

	for i in range(m):
		for j in range(n):
			A[i][j] = min(A[i-1][j-1] + match(X[i],Y[j]), A[i-1][j] + gap, A[i][j-1] + gap)

	return A[m-1][n-1]


def dp_alignmt_reconst(A, X, Y, gap, match):
	i = len(X) - 1
	j = len(Y) - 1
	B = []

	while i >= 0 and j >= 0:
		if A[i][j] == A[i-1][j-1] + match(X[i],Y[j]):
			B.insert(0, (X[i], Y[j]))
			i -= 1
			j -= 1
		elif A[i][j] == A[i-1][j] + gap:
			B.insert(0, (X[i], '-'))
			i -= 1
		else:
			B.insert(0, ('-', Y[j]))
			j -= 1

	return B


if __name__ == '__main__':
	X = raw_input()
	Y = raw_input()
	gap = int(raw_input())
	match_v = int(raw_input())

	#X = 'AGGAATT'
	#Y = 'AGGCTT'
	#gap = 1

	def match(xi, yj):
		if xi != yj: return match_v
		return 0

	A = [[0]*len(Y) for _ in range(len(X))]
	min_c = dp_alignmt(A, X, Y, gap, match)
	B = dp_alignmt_reconst(A, X, Y, gap, match)

	a, m, b = '', '', ''
	for i, j in B:
		a += i
		b += j
		if i == j:
			m += '|'
		else:
			m += ' '

	print a
	print m
	print b

