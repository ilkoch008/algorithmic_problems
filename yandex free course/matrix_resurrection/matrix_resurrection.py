from typing import List
import sys
sys.setrecursionlimit(10**6)


possible_steps = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]


def get_longest_increasing_path_from_cell(cell, matrix, max_path_lengths):
    height = len(matrix)
    width = len(matrix[0])
    i, j = cell
    res = 0
    for step in possible_steps:
        d_i, d_j = step
        next_i = i + d_i
        next_j = j + d_j
        if 0 <= next_i < height and 0 <= next_j < width:
            if matrix[next_i][next_j] > matrix[i][j]:
                if max_path_lengths[next_i][next_j] != 0:
                    res = max(res, max_path_lengths[next_i][next_j])
                else:
                    res = max(res, get_longest_increasing_path_from_cell((next_i, next_j), matrix, max_path_lengths))
    res += 1
    max_path_lengths[i][j] = res
    return res


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
    height = len(matrix)
    width = len(matrix[0])
    max_path_lengths = [[0 for x in range(width)] for y in range(height)]
    res = 0
    for i in range(height):
        for j in range(width):
            if max_path_lengths[i][j] == 0:
                get_longest_increasing_path_from_cell((i, j), matrix, max_path_lengths)
            res = max(res, max_path_lengths[i][j])
    return res

def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

matrix = read_matrix()
print(get_longest_increasing_path(matrix))