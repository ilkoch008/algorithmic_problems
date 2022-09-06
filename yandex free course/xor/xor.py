from typing import List


def get_max_xor(numbers: List[int]) -> int:
    maxx = 0
    mask = 0
    se = set()
    for i in range(30, -1, -1):
        mask |= (1 << i)
        new_maxx = maxx | (1 << i)
        for num in numbers:
            se.add(num & mask)
        for prefix in se:
            if (new_maxx ^ prefix) in se:
                maxx = new_maxx
                break
        se.clear()
    return maxx


n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))
