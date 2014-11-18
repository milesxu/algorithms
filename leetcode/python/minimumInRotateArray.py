class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        if len(num) < 3:
            return min(num[0], num[-1])
        quantile, minn, found = [0, len(num)], num[0], False
        while quantile:
            temp, quantile = quantile[:], []
            for i, p in enumerate(temp[:-1]):
                q = temp[i + 1]
                if num[p] < num[q - 1]:
                    minn, found = min(minn, num[p]), True
                elif num[p] > num[q - 1]:
                    l, r = p, q
                    while l + 1 < r:
                        mid = (l + r) // 2
                        if num[mid] >= num[l]:
                            l = mid
                        else:
                            r = mid
                    return num[r]
                elif p + 1 < q and not found:
                    mid = (p + q) // 2
                    if not quantile:
                        quantile.append(p)
                    quantile += [mid, q]
        return minn

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([-1, -1, -1, -1]))
