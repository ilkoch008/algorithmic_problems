def bis(arr, x):
    left = 0
    right = len(arr) - 1
    mid = None
    mid_val = None
    while left <= right:
        mid = (left + right) >> 1
        mid_val = arr[mid]
        if mid_val < x:
            left = mid + 1
        else:  # mid_val > x:
            right = mid - 1
    if mid_val < x:
        return mid
    else:  # mid_val > x:
        return max(0, mid-1)


class HistoricalArray:
    def __init__(self, size) -> None:
        self.maps = [{0: 0} for _ in range(size)]
        self.current_era_num = 0
        self.current_era_id = 0
        self.id_num_map = {self.current_era_id: self.current_era_num}

    def set(self, index, value) -> None:
        self.maps[index][self.current_era_num] = value

    def get(self, index, era_id) -> int:
        era_num = self.id_num_map[era_id]
        current_index_map = self.maps[index]
        if era_num in current_index_map:
            return current_index_map[era_num]
        else:
            nums = list(current_index_map.keys())
            return current_index_map[nums[bis(nums, era_num)]]

    def begin_new_era(self, era_id) -> None:
        self.current_era_num += 1
        self.current_era_id = era_id
        self.id_num_map[self.current_era_id] = self.current_era_num


size = int(input())
q = int(input())
historical_array = HistoricalArray(size)
for i in range(q):
    query = input().split()
    query_type = query[0]
    if query_type == "set":
        historical_array.set(int(query[1]), int(query[2]))
    elif query_type == "begin_new_era":
        historical_array.begin_new_era(int(query[1]))
    else:
        print(historical_array.get(int(query[1]), int(query[2])))
