from typing import List


def queens(n, i, columns, diagonals1, diagonals2):
    if i < n + 1:
        for j in range(1, n + 1):
            if j not in columns and i+j not in diagonals1 and i-j not in diagonals2:
                new_columns = columns.copy()
                new_diagonals1 = diagonals1.copy()
                new_diagonals2 = diagonals2.copy()
                new_columns[j] = None
                new_diagonals1[i+j] = None
                new_diagonals2[i-j] = None
                yield from queens(n, i + 1, new_columns, new_diagonals1, new_diagonals2)
    else:
        yield list(columns.keys())


def get_all_peaceful_combinations(n) -> List[List[int]]:
    res = list(queens(n, 1, {}, {}, {}))
    return res


n = int(input())
combinations = get_all_peaceful_combinations(n)

print(len(combinations))
for combination in combinations:
    print(*combination)
