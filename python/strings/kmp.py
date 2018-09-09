"""
KMP algorithm
- compares the pattern to the text left-to-right
- shifts pattern if mismatch occurs (depends on failure arr)

KMP Failure Array
F[j] = len of largest prefix of P[0..j] that is also a suffix of P[1..j]
built in O(m) time
"""

def failureArray(P):
    m = len(P)
    F = [0]*m
    i = 1
    j = 0
    while i < m:
        if P[i] == P[j]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            F[i] = 0
            i += 1
    return F


def kmp(P, T):
    F = failureArray(P)
    i, j = 0, 0
    while i < len(T):
        if T[i] == P[j]:
            if j == len(P)-1:
                return i - j # match
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = F[j-1]
            else:
                i += 1
    return -1


def main():
    P = "abacaba"
    T = "ababacababaab"
    print(kmp(P, T))


if __name__ == '__main__':
    main()
