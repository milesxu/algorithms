class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    def pow(self, x, n):
        if not n:
            return 1.0
        temp, m, l, product, lst = x, abs(n), 1, {1: x}, [1]
        while l < m:
            k = m - l
            if k >= l:
                k = l
            elif k not in product:
                a, b = 0, len(lst)
                while a + 1 < b:
                    mid = (a + b) // 2
                    if lst[mid] < k:
                        a = mid
                    else:
                        b = mid
                k = lst[a]
            temp, l = product[l] * product[k], l + k
            product[l] = temp
            lst.append(l)
        if n < 0:
            return (1.0 / product[m])
        else:
            return product[m]
