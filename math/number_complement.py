
class Solution():

    def findComplement(self, num):
        result = []
        while num != 0:
            r = num % 2
            result.insert(0, r)
            num = num / 2
        power = len(result)-1
        final = 0
        for n in result:
            n = 0 if n == 1 else 1
            final += n * 2**power
            power -= 1
        return final


if __name__ == '__main__':
    print Solution().findComplement(5)