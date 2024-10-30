from itertools import combinations


with open("input.txt", "r") as data_file:
    N, T = map(int, data_file.readline().split())
    nums = list(map(int, data_file.readline().split()))

res = 0

print(len(nums))

for p in combinations(nums, 4):
    if sum(p) == T:
        res += 1

print(res)
