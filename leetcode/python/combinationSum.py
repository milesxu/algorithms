class Solution:

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))

        def binarysearch(end, num):
            start = 0
            while start < end:
                mid = (start + end + 1) >> 1
                if candidates[mid] > num:
                    end = mid - 1
                else:
                    start = mid
            return start

        result, i = [], binarysearch(len(candidates) - 1, target)
        stack, residue = [i], target - candidates[i]
        while stack:
            if residue > 0:
                j = stack[-1]
                if residue >= candidates[j]:
                    n, residue = divmod(residue, candidates[j])
                    stack += [j] * n
                else:
                    k = binarysearch(j, residue)
                    stack.append(k)
                    residue -= candidates[k]
            else:
                if residue == 0:
                    result.append([candidates[p] for p in reversed(stack)])
                while stack:
                    j = stack.pop()
                    residue += candidates[j]
                    if j:
                        stack.append(j - 1)
                        residue -= candidates[j - 1]
                        break
        return result

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)

        def binarysearch(end, num):
            start = 0
            while start < end:
                mid = (start + end + 1) >> 1
                if candidates[mid] > num:
                    end = mid - 1
                else:
                    start = mid
            return start

        result, i = [], binarysearch(len(candidates) - 1, target)
        stack, residue = [i], target - candidates[i]
        while stack:
            i = stack[-1]
            if residue > 0 and i:
                k = min(binarysearch(i, residue), i - 1)
                stack.append(k)
                residue -= candidates[k]
            else:
                if residue == 0:
                    result.append([candidates[p] for p in reversed(stack)])
                while stack:
                    j = stack.pop()
                    residue, k = residue + candidates[j], j - 1
                    while k >= 0 and candidates[k] == candidates[k + 1]:
                        k -= 1
                    if k > -1:
                        stack.append(k)
                        residue -= candidates[k]
                        break
        return result


if __name__ == '__main__':
    comb = Solution()
    print(comb.combinationSum([1], 2))
    print(comb.combinationSum([1], 1))
    print(comb.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6))
