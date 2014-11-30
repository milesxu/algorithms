class Solution:

    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if not gas:
            return -1
        start, current, g, c, n = 0, 0, gas[0], cost[0], 1
        while True:
            while n:
                if g < c:
                    g, c = g - gas[start], c - cost[start]
                    start, n = start + 1, n - 1
                    if start == len(gas):
                        return -1
                elif n == len(gas):
                    return start
                else:
                    break
            current += 1
            if current == len(gas):
                current = 0
            g, c, n = g + gas[current], c + cost[current], n + 1
        return -1
