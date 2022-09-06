import heapq


def get_energy_for_union(stones):
    heapq.heapify(stones)
    res = 0
    while len(stones) > 1:
        new_pile = heapq.heappop(stones) + heapq.heappop(stones)
        res += new_pile
        heapq.heappush(stones, new_pile)
    return res


n = int(input())
stones = list(map(int, input().split()))

print(get_energy_for_union(stones))