class Solution:

    # @param A, a list of integers
    # @return an integer

    # cannot be used on arrays that have duplicate items.
    def firstMissingPositive1(self, A):
        minp, maxp, np, total = None, None, 0, 0
        for p in A:
            if p > 0:
                if minp is None or minp > p:
                    minp = p
                if maxp is None or maxp < p:
                    maxp = p
                np, total = np + 1, total + p
        if minp is None or minp > 1:
            return 1
        n = maxp - minp + 1 - np
        if not n:
            return maxp + 1
        while n > 1:
            miss = ((maxp - minp + 1) * (maxp + minp) >> 1) - total
            maxp, np, total = (miss - (n * (n - 1) >> 1)) // n, 0, 0
            for p in A:
                if 0 < p <= maxp:
                    np, total = np + 1, total + p
            n = maxp - minp + 1 - np
        return ((maxp - minp + 1) * (maxp + minp) >> 1) - total

    def firstMissingPositive(self, A):
        for i in range(len(A)):
            while 0 < A[i] <= len(A) and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
        for i, p in enumerate(A):
            if p != i + 1:
                return i + 1
        return len(A) + 1

    def first_missing_positive(self, A):
        if not A:
            return 1
        num = 0
        for p in A:
            if p > 0:
                num |= (1 << (p - 1))
        i = 0
        while num & (1 << i):
            i += 1
        return i + 1


if __name__ == '__main__':
    fmp = Solution()
    print(fmp.firstMissingPositive([10, 4, 16, 54, 17, -7, 21, 15, 25, 31, 61,
                                    1, 6, 12, 21, 46, 16, 56, 54, 12, 23, 20,
                                    38, 63, 2, 27, 35, 11, 13, 47, 13, 11, 61,
                                    39, 0, 14, 42, 8, 16, 54, 50, 12, -10, 43,
                                    11, -1, 24, 38, -10, 13, 60, 0, 44, 11,
                                    50, 33, 48, 20, 31, -4, 2, 54, -6, 51, 6]))
