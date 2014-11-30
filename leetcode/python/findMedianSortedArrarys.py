class Solution:

    # @return a float
    def findMedianSortedArrays(self, A, B):
        if len(A) <= len(B):
            small, big = A, B
        else:
            small, big = B, A
        m, n = len(small), len(big)
        if n == 0:
            return None
        elif m == 0:
            if n & 1:
                return big[(n - 1) // 2]
            else:
                return (big[n // 2] + big[n//2 - 1]) / 2.0
        totalLen, halfLen = m + n, (m + n) // 2
        mins, maxs = 0, m
        # mina = max(0, (len(A) - len(B)) // 2)
        # maxa = min(len(A), (len(A) + len(B)) // 2)
        while mins + 1 != maxs:
            median = (mins + maxs) // 2
            b = halfLen - median
            if small[median - 1] <= big[b - 1]:
                mins = median
            else:
                maxs = median
        # if A[mins] <= B[halfLen - maxs]:
        #     a = maxs
        # else:
        #     a = mins
        if small[maxs - 1] > big[halfLen - mins - 1]:
            a = mins
        else:
            a = maxs
        b = halfLen - a
        tmin, tmax = None, None
        if a < m and b < n:
            tmax = min(small[a], big[b])
        elif b == n:
            tmax = small[a]
        else:
            tmax = big[b]
        if totalLen & 1:
            return tmax
        if a and b:
            tmin = max(small[a - 1], big[b - 1])
        elif a:
            tmin = small[a - 1]
        else:
            tmin = big[b - 1]
        return (tmin + tmax) / 2.0

