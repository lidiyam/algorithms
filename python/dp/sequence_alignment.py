def match(xi, yj, match_v):
		if xi != yj: return match_v
		return 0

def dp_alignmt(A, X, Y, gap, match_v):
	m = len(X)
	n = len(Y)

	if m == 0 and n == 0: return []

	for i in range(m+1):
		A[i][0] = i*gap

	for j in range(n+1):
		A[0][j] = j*gap

	for i in range(1,m+1):
		for j in range(1,n+1):
			A[i][j] = min(A[i-1][j-1] + match(X[i-1],Y[j-1], match_v), A[i-1][j] + gap, A[i][j-1] + gap)

	return A[m][n]


def dp_alignmt_reconst(A, X, Y, gap, match_v):
	i = len(X)
	j = len(Y)
	B = []

	X = ' ' + X
	Y = ' ' + Y

	while i > 0 and j > 0:
		if A[i][j] == A[i-1][j-1] + match(X[i],Y[j],match_v):
			B.insert(0, (X[i], Y[j]))
			i -= 1
			j -= 1
		elif A[i][j] == A[i-1][j] + gap:
			B.insert(0, (X[i], '-'))
			i -= 1
		else:
			B.insert(0, ('-', Y[j]))
			j -= 1

	while i > 0:
		B.insert(0, (X[i], '-'))
		i -= 1

	while j > 0:
		B.insert(0, ('-', Y[j]))
		j -= 1

	return B


if __name__ == '__main__':
	X = raw_input()
	Y = raw_input()
	gap = int(raw_input())
	match_v = int(raw_input())

	A = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
	min_c = dp_alignmt(A, X, Y, gap, match_v)
	B = dp_alignmt_reconst(A, X, Y, gap, match_v)

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

