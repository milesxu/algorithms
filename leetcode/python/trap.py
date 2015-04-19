class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        stack, result, i, h = [], 0, 0, 0
        while i < len(A):
            if not (A[i] and stack):
                stack.append(i)
                i += 1
                i, h = i + 1, 0
            elif not stack:
                stack.append(i)
                i += 1
            elif A[i] < A[stack[-1]]:
                result += (i - stack[-1] - 1) * (A[i] - h)
                stack.append(i)
                i += 1
            elif A[i] == A[stack[-1]]:
                result += (i - stack[-1] - 1) * (A[i] - h)
                stack[-1], i = i, i + 1
            else:
                result += (i - stack[-1] - 1) * (A[stack[-1]] - h)
                h = A[stack.pop()]
        return result

    def trap1(self, A):
        i, j, edge, result = 0, len(A) - 1, 0, 0
        while i <= j:
            edge = max(edge, min(A[i], A[j]))
            result += edge - min(A[i], A[j])
            if A[i] <= A[j]:
                i += 1
            else:
                j -= 1
        return result

    def trap2(self, A):
        stack, result, i = [], 0, 0
        while i < len(A):
            if not stack or A[i] <= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                j = stack.pop()
                if stack and A[stack[-1]] > A[j]:
                    result += (min(A[stack[-1]], A[i]) - A[j]) * (
                        i - stack[-1] - 1)
        return result


if __name__ == '__main__':
    tp = Solution()
    print(tp.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(tp.trap2(
        [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8,
         1, 3]))
