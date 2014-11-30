class Solution:

    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        temp = 0
        for p in A:
            temp ^= p
        return temp

    # @param A, a list of integer
    # @return an integer
    def singleNumber1(self, A):
        one, two, three = 0, 0, 0
        for p in A:
            three = two & p
            two = (two | (one & p)) & (~three)
            one = (one | p) & (~three)
        return one

    # @param A, a list of integer
    # @return an integer
    def singleNumber2(self, A):
        one, two, mask = 0, 0, 0
        for p in A:
            mask = ~(one & two)
            two |= (one & p)
            one ^= p
            two &= mask
            one &= mask
        return one
