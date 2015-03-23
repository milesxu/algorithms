class Solution:

    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        n = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if n < i:
                    A[n] = A[i]
                n += 1
        return n
