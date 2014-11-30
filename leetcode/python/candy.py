class Solution:

    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        minCandy, index, compensate = [1] * len(ratings), 0, 0

        def backIncrease():
            n = 0
            while n < compensate:
                    if minCandy[index - n - 1] <= minCandy[index - n]:
                        minCandy[index - n - 1] = minCandy[index - n] + 1
                        n += 1
                    else:
                        break

        while index < len(ratings) - 1:
            if ratings[index] > ratings[index + 1]:
                compensate += 1
            else:
                if ratings[index] < ratings[index + 1]:
                    minCandy[index + 1] = minCandy[index] + 1
                backIncrease()
                compensate = 0
            index += 1
        backIncrease()
        return sum(minCandy)
