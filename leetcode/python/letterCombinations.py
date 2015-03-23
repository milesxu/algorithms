class Solution:

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        dint = int(digits)
        dint, r = divmod(dint, 10)
        result = [p for p in letters[r - 2]]
        while dint:
            dint, r = divmod(dint, 10)
            result = [p + q for p in letters[r - 2] for q in result]
        return result
