from collections import defaultdict
import collections
from functools import reduce


class Solution:

    # @param strs, a list of strings
    # @return a list of strings

    def anagrams(self, strs):
        result, cache = [], {}
        for p in strs:
            anagram = p[::-1]
            if p not in cache:
                if anagram in cache:
                    result += [anagram, p]
                cache[p] == 1
            elif p == anagram and cache[p] == 1:
                result += [anagram, p]
                cache[p] += 1
        return result

    def anagrams1(self, strs):
        cache = defaultdict(list)
        for p in strs:
            cache[''.join(sorted(list(p)))].append(p)
        return [s for v in cache.values() if len(v) > 1 for s in v]

    def anagrams2(self, strs):
        dic = defaultdict(list)
        map(lambda item: dic[''.join(sorted(item))].append(item), strs)
        return [x for key in dic.keys() for x in dic[key] if len(dic[key]) > 1]

    def anagrams3(self, strs):
        count = collections.Counter([tuple(sorted(str)) for str in strs])
        return filter(lambda x: count[tuple(sorted(x))] > 1, strs)

    def anagrams4(self, strs):
        result, cache = [], {}
        for p in strs:
            temp = tuple(sorted(p))
            if temp in cache:
                result.append(p)
                if cache[temp] is not None:
                    result.append(cache[temp])
                    cache[temp] = None
            else:
                cache[temp] = p
        return result

    def anagrams5(self, strs):
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        result, cache = [], {}
        for p in strs:
            temp = reduce(lambda x, y: x * y,
                          [prime[ord(q) - ord('a')] for q in p]) if p else 1
            if temp in cache:
                result.append(p)
                if cache[temp] is not None:
                    result.append(cache[temp])
                    cache[temp] = None
            else:
                cache[temp] = p
        return result
