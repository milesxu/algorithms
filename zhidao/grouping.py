from operator import itemgetter


def grouping(dataDict):
    keys = [p[0] for p in
            sorted(dataDict.items(), key=itemgetter(1), reverse=True)]
    groups, temp, result = [[[] for i in range(8)]], [], []
    for p in keys:
        num, glen = dataDict[p], len(groups)
        while num:
            if num < glen:
                glen -= 1
                continue
            n = num - glen + 1
            for i in range(n):
                groups[glen - 1][i].append(p)
            temp.append(groups[glen - 1][:n])
            del groups[glen - 1][:n]
            num, glen = num - n, glen - 1
        for lst in temp:
            if len(lst[0]) == 4:
                result += lst
            else:
                groups.append(lst)
        temp = []
        groups = [lst for lst in groups if lst and len(lst[0]) < 4]
        groups.sort(key=len)
    return result


if __name__ == '__main__':
    data = {1: 7, 2: 4, 3: 3, 4: 5, 5: 7, 6: 4, 7: 2}
    print(grouping(data))
