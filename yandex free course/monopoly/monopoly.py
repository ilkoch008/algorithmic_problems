import heapq


def get_max_final_capital(buildings, start_capital: int, max_buildings: int) -> int:
    capital = start_capital
    available_heap = []
    for _ in range(max_buildings):
        while len(buildings) > 0 and buildings[0][0] <= capital:
            heapq.heappush(available_heap, -heapq.heappop(buildings)[1])
        if len(available_heap) > 0:
            capital -= heapq.heappop(available_heap)
        else:
            return capital
    return capital


n, k = map(int, input().split())
buildings = []
for i in range(n):
    need_capital, added_capital = map(int, input().split())
    buildings.append((need_capital, added_capital))

heapq.heapify(buildings)
M = int(input())
print(get_max_final_capital(buildings, M, k))
