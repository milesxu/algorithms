def lexcialNext(lst):
    j = len(lst) - 2
    while lst[j] >= lst[j + 1] and j >= 0:
        j -= 1
    if j < 0:
        return False
    k = len(lst) - 1
    while lst[j] >= lst[k]:
        k -= 1
    lst[j], lst[k] = lst[k], lst[j]
    l, m = j + 1, len(lst) - 1
    while l < m:
        lst[l], lst[m] = lst[m], lst[l]
        l += 1
        m -= 1
    return True


def permute(lst):
    plst = sorted(lst)
    print(plst)
    while lexcialNext(plst):
        print(plst)


if __name__ == '__main__':
    permute([3, 4, 6, 3])
