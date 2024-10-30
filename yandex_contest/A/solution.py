with open("input.txt", "r") as data_file:
    N, T = map(int, data_file.readline().split())
    nums = list(map(int, data_file.readlines()))

res = sum(nums[0:T])
p_res = res
res_i = 0

for i in range(N-T):
    p_res = p_res-nums[i]+nums[i+T]
    if p_res < res:
        res = p_res
        res_i = i+1

print(res_i+1)