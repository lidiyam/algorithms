def modular_pow(n, k, m):
    if m == 1: return 0
    result = 1
    n = n % m
    while k > 0:
        if (k % 2 == 1):
           result = (result * n) % m
        k = k // 2
        n = (n * n) % m
    return result

if __name__ == '__main__':
        print modular_pow(3,8,5)
        print modular_pow(3,6,5)
        print modular_pow(74,6,11)
