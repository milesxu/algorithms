class Solution:

    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        lst1, lst2 = version1.split('.'), version2.split('.')
        while lst1 and not int(lst1[-1]):
            lst1.pop()
        while lst2 and not int(lst2[-1]):
            lst2.pop()
        for p, q in zip(lst1, lst2):
            m, n = int(p), int(q)
            if m > n:
                return 1
            elif m < n:
                return -1
        if len(lst1) > len(lst2):
            return 1
        elif len(lst1) < len(lst2):
            return -1
        return 0
