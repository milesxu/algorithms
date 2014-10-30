# Definition for a point
class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param points, a list of Points
    # @return an integer

    def maxPoints(self, points):
        maxp = 2
        for i, p in enumerate(points):
            if i >= len(points) - maxp:
                break
            vectors, maxi, maxj = [], 1, 0
            for j in range(i + 1, len(points)):
                vj = [points[j].x - p.x, points[j].y - p.y]
                if vj[0] == 0 and vj[1] == 0:
                    maxi += 1
                    continue
                elif vj[0] < 0:
                    vj = [-l for l in vj[:]]
                start, end, inserted = 0, len(vectors), False
                while start != end:
                    medium = (start + end) // 2
                    temp = vectors[medium][0] * vj[1] - \
                        vj[0] * vectors[medium][1]
                    if temp == 0:
                        vectors[medium][2] += 1
                        maxj = max(maxj, vectors[medium][2])
                        inserted = True
                        break
                    elif temp < 0:
                        # because (a + a + 1) / 2 == a
                        start = max(medium, start + 1)
                    else:
                        end = medium
                if not inserted:
                    vectors.insert(end, vj + [1])
                    maxj = max(1, maxj)
            maxp = max(maxp, maxi + maxj)
        return min(maxp, len(points))

if __name__ == '__main__':
    lst = [(0, 9), (138, 429), (115, 359), (115, 359), (-30, -102),
           (230, 709), (-150, -686), (-135, -613), (-60, -248), (-161, -481),
           (207, 639), (23, 79), (-230, -691), (-115, -341), (92, 289),
           (60, 336), (-105, -467), (135, 701), (-90, -394), (-184, -551),
           (150, 774)]
    points = [Point(i[0], i[1]) for i in lst]
    s = Solution()
    print(s.maxPoints(points))
