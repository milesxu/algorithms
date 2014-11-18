class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        arr, prdt, nzNum, zNum, maxp = [], 0, 0, 0, A[0]
        if len(A) == 1:
            return A[0]
        A.append(0)
        for i, p in enumerate(A):
            if p:
                nzNum += 1
                if prdt:
                    prdt *= p
                else:
                    prdt = p
                if p < 0:
                    arr.append((prdt, p))
            else:
                zNum += 1
                if prdt > 0:
                    maxp = max(maxp, prdt)
                else:
                    if nzNum < 2:
                        maxp = max(maxp, 0)
                    else:
                        right = prdt // arr[-1][0]
                        left = arr[0][0] // arr[0][1]
                        if len(arr) == 1:
                            maxp = max(maxp, right, left)
                        else:
                            mid1 = prdt // arr[0][0]
                            mid2 = arr[-1][0] // arr[-1][1]
                            maxp = max(maxp, left, right, mid1, mid2)
                prdt, nzNum, arr = 0, 0, []
        return maxp
