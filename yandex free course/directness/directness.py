from typing import List, Tuple


def is_on_one_line(points: List[Tuple[int]]) -> bool:
    l = len(points)
    if l < 2:
        return True
    else:
        x1, y1 = points[0]
        i = 1
        x2, y2 = x1, y1
        while i < l and x1 == x2 and y1 == y2:
            x2, y2 = points[i]
            i += 1
        for j in range(i, l):
            x, y = points[j]
            if (x-x1)*(y2-y1) != (y-y1)*(x2-x1):
                return False
        return True


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

if is_on_one_line(points):
    print('YES')
else:
    print('NO')
