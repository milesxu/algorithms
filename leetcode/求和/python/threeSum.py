import sys

class Solution:

    # @return a list of lists of length 3, [[val1,val2,val3]]

    def threeSum(self, num):
        nopositive, positive, zero = [], [], 0
        for p in num:
            if p < 0:
                nopositive.append(p)
            elif p > 0:
                positive.append(p)
            else:
                zero += 1
        if len(num) < 3 or (not (nopositive and positive) and zero < 3):
            return []
        result = set()
        if zero:
            nopositive.append(0)
            if zero >= 3:
                result.add((0, 0, 0))

        def compose(src, dest):
            tempset = set(dest)
            for i, p in enumerate(src[0: len(src) - 1]):
                for j in range(i + 1, len(src)):
                    if -(p + src[j]) in tempset:
                        result.add(tuple(sorted([p, src[j], -(p + src[j])])))

        compose(nopositive, positive)
        compose(positive, nopositive)
        return [list(p) for p in result]

    def threeSum3(self, num):
        sortnum, result, i = sorted(num), [], 0
        while i < len(num) and sortnum[i] <= 0:
            if i and sortnum[i] == sortnum[i - 1]:
                i += 1
                continue
            target = -sortnum[i]
            j, k = i + 1, len(num) - 1
            while j < k:
                test = sortnum[j] + sortnum[k]
                if test == target:
                    result.append([sortnum[i], sortnum[j], sortnum[k]])
                    j += 1
                    k -= 1
                    while j < k and sortnum[j] == sortnum[j - 1]:
                        j += 1
                    while j < k and sortnum[k] == sortnum[k + 1]:
                        k -= 1
                elif test < target:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result

    def threeSum1(self, num):
        sortnum, result, i = sorted(num), [], 0
        while i < len(sortnum) - 2 and sortnum[i] <= 0:
            if sortnum[-1] + sortnum[-2] + sortnum[0] < 0:
                sortnum.pop(0)
            elif sortnum[0] + sortnum[1] + sortnum[-1] > 0:
                sortnum.pop()
            elif i and sortnum[i - 1] == sortnum[i]:
                i += 1
            else:
                start, end = i + 1, len(sortnum) - 1
                while start < end and sortnum[end] >= 0:
                    tempsum = sortnum[start] + sortnum[end]
                    if tempsum > -sortnum[i] \
                            or (end < len(sortnum) - 1
                                and sortnum[end] == sortnum[end + 1]):
                        end -= 1
                    elif tempsum < -sortnum[i]:
                        start += 1
                    else:
                        result.append([sortnum[i],
                                       sortnum[start], sortnum[end]])
                        start, end = start + 1, end - 1
                i += 1
        return result
        # for i, p in enumerate(sortnum[: len(num) - 1]):
        #     if i and sortnum[i - 1] == p:
        #         continue
        #     if p > 0:
        #         break
        #     start, end = i + 1, len(num) - 1
        #     while start < end:
        #         tempsum = sortnum[start] + sortnum[end]
        #         if end < len(num) - 1 and sortnum[end] == sortnum[end + 1]:
        #             end -= 1
        #         elif tempsum > -p:
        #             end -= 1
        #         elif tempsum < -p:
        #             start += 1
        #         else:
        #             result.append(sorted([p, sortnum[start], sortnum[end]]))
        #             start, end = start + 1, end - 1
        # return result

    def threeSum2(self, num):
        sortnum, result, i = sorted(num), [], 0
        while i < len(sortnum) - 2 and sortnum[i] <= 0:
            if i and sortnum[i] == sortnum[i - 1]:
                i += 1
                continue
            j, end = i + 1, len(num) - 1
            while j < end:
                if j > i + 1 and sortnum[j] == sortnum[j - 1]:
                    j += 1
                    continue
                start, tempsum = j + 1, -(sortnum[i] + sortnum[j])
                while start < end:
                    temp = (start + end) // 2
                    if sortnum[temp] < tempsum:
                        start = temp + 1
                    else:
                        end = temp
                        if sortnum[end] == tempsum:
                            break
                if sortnum[end] == tempsum:
                    result.append([sortnum[i], sortnum[j], sortnum[end]])
                j += 1
            i += 1
        return result

    # @return an integer
    def threeSumClosest(self, num, target):
        sortnum, dist, result, end0 = sorted(num), sys.maxsize, 0, len(num) - 1
        for i in range(len(num) - 2):
            if i and sortnum[i] == sortnum[i - 1]:
                continue
            start, end = i + 1, end0
            test = target - sortnum[i]
            while start < end:
                if end < len(num) - 1 and sortnum[end] == sortnum[end + 1]:
                    end -= 1
                    continue
                temp = test - sortnum[start] - sortnum[end]
                if temp == 0:
                    return target
                if dist > abs(temp):
                    dist, result, end0 = abs(temp), target - temp, end
                if temp < 0:
                    end -= 1
                else:
                    start += 1
        return result

    def threeSumClosest1(self, num, target):
        sortnum, dist, result, i = sorted(num), None, None, 0
        while i < len(num) - 2:
            if i and sortnum[i] == sortnum[i - 1]:
                i += 1
                continue
            if dist and sortnum[i] > target // 3:
                break
            j, end = i + 1, len(num) - 1
            while j < end:
                if j > i + 1 and sortnum[j] == sortnum[j - 1]:
                    j += 1
                    continue
                start, tempsum = j + 1, target - sortnum[i] - sortnum[j]
                while start < end:
                    temp = (start + end) // 2
                    if sortnum[temp] < tempsum:
                        start = temp + 1
                    else:
                        end = temp
                        if sortnum[end] == tempsum:
                            return target
                dend = tempsum - sortnum[end]
                td, tr = abs(dend), target - dend
                if j < end - 1:
                    pend = tempsum - sortnum[end - 1]
                    if td > abs(pend):
                        td, tr = abs(pend), target - pend
                if dist is None or dist > td:
                    dist, result = td, tr
                j += 1
            i += 1
        return result


if __name__ == '__main__':
    tsum = Solution()
    #print(tsum.threeSum2([3, 0, -2, -1, 1, 2]))
    #print(tsum.threeSum2([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
    #print(tsum.threeSumClosest1([1, 1, 1, 0], -100))
    #print(tsum.threeSumClosest1([1, 2, 4, 8, 16, 32, 64, 128], 82))
    #print(tsum.threeSumClosest1([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
    #print(tsum.threeSumClosest1([-16, -2, 17, -16, 3, -7, -13, 20, -4, 12, 5,
    #                             13, -7, 0, 5, 4, -17, -16, 9, 1, 8, -6, 0, -8,
    #                             16, 10, -6, 9, -4, 12, 16, 5, 19, 2, -9, -17,
    #                             -8, -17, 7, -10, 2, 20, -18, -20, -14, -6, 6,
    #                             17, -10, -8, 18, -15, 7, -9, 13, 13, -13, 3,
    #                             18, 10, 12, 16, -6, -19, -6, -13, 8, -5, 16,
    #                             5, 8, -3, -9, -9, -5, 14, 14, -13, -18, 13,
    #                             15, -3, 9, 14, 18, -14, -14, 1, 20, -4, -6, 0,
    #                             3, 15, 20, 20, 9, 13, -8, -1, -2, 6], -58))
    #print(tsum.threeSum2([0, 0, 0]))
    print(tsum.threeSumClosest([-1, 0, 1, 1, 55], 3))
