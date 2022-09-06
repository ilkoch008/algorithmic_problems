def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def get_number_of_good_pairs(numbers) -> int:
    res = 0
    n_dict = {}
    for num in numbers:
        num = num % 200 * sign(num)
        if num in n_dict.keys():
            res += n_dict[num]
            n_dict[num] += 1
        else:
            n_dict[num] = 1
    return res


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
