class Solution:

    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n = 0
        for i, p in enumerate(A):
            if p != elem:
                if n < i:
                    A[n] = p
                n += 1
        return n
