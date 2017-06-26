class MaxSubArray:

    """get the sub array that has the greatest sum"""

    def divideSolution(self, Arr):

        def maxCross(low, mid, high):
            lMax, lIndex, curSum = Arr[mid], mid, 0
            for i in range(mid - 1, low - 1, -1):
                curSum += Arr[i]
                if lMax < curSum:
                    lMax = curSum
                    lIndex = i
            rMax, rIndex, curSum = Arr[mid + 1], mid + 1, 0
            for i in range(mid + 2, high):
                curSum += Arr[i]
                if rMax < curSum:
                    rMax = curSum
                    rIndex = i
            return [lIndex, rIndex], lMax + rMax

        def recursion(low, arlen):
            if arlen == 1:
                return [low], Arr[low]
            else:
                mid = arlen / 2
                lInterval, lMax = recursion(low, mid)
                rInterval, rMax = recursion(low + mid, arlen - mid)
                mInterval, mMax = maxCross(low, mid - 1, low + arlen)
                if lMax >= rMax and lMax >= mMax:
                    return lInterval, lMax
                elif rMax >= lMax and rMax >= mMax:
                    return rInterval, rMax
                else:
                    return mInterval, mMax

        interval, amax = recursion(0, len(Arr))
        return amax

    def linearSolution1(self, Arr):
        maxSum, boundSum = Arr[0], Arr[0]
        maxInterval, boundInterval = [0], [0]
        for i in range(1, len(Arr)):
            if boundSum < 0:
                boundSum = Arr[i]
                boundInterval = [i]
            else:
                boundSum += Arr[i]
                boundInterval.append[i]
            if maxSum < boundSum:
                maxSum, maxInterval = boundSum, boundInterval
        return maxSum

    def linearSolution2(self, Arr):
        curSum, maxSum, maxNeg, numNeg = 0, 0, 0, 0
        for v in Arr:
            if v >= 0:
                curSum += v
            else:
                numNeg += 1
                if maxNeg == 0 or maxNeg < v:
                    maxNeg = v
                if curSum < abs(v):
                    curSum = 0
                else:
                    curSum += v
            if curSum > maxSum:
                maxSum = curSum
            if maxSum == 0 and len(Arr) == numNeg:
                maxSum = maxNeg
        return maxSum

if __name__ == '__main__':
    msa = MaxSubArray()
    print(msa.divideSolution([-2, -3, 1]))
