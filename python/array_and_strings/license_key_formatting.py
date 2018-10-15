def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    s = S.replace("-", "").upper()
    n = len(s)
    start = n % K
    a, l = '', 0
    for i in range(start, n, K):
        if i == 0: continue
        a += s[l:i] + "-"
        l = i
    return a + s[l:]


if __name__ == '__main__':
    print licenseKeyFormatting("r", 3)