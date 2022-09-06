from typing import List, Tuple


class SegmentsPack:
    def __init__(self, sequence1: List[Tuple[int]], sequence2: List[Tuple[int]]):
        self.seq1 = sequence1
        self.seq2 = sequence2
        self.n_seg1 = 0
        self.n_seg2 = 0
        self.p_seg1 = 0
        self.p_seg2 = 0
        self.res = []

    def get_next_point(self):
        val1 = self.seq1[self.n_seg1][self.p_seg1]
        val2 = self.seq2[self.n_seg2][self.p_seg2]
        if val1 < val2:
            self.p_seg1 += 1
            self.n_seg1 += int(self.p_seg1/2)
            self.p_seg1 = self.p_seg1 % 2
            return val1
        elif val2 < val1:
            self.p_seg2 += 1
            self.n_seg2 += int(self.p_seg2 / 2)
            self.p_seg2 = self.p_seg2 % 2
            return val2
        else:
            self.p_seg1 += 1
            self.n_seg1 += int(self.p_seg1 / 2)
            self.p_seg1 = self.p_seg1 % 2
            self.p_seg2 += 1
            self.n_seg2 += int(self.p_seg2 / 2)
            self.p_seg2 = self.p_seg2 % 2
            if self.p_seg1 + self.p_seg2 == 1:
                self.res.append((val1, val1))
            return val1

    def get_inter(self):

        current_point = self.get_next_point()
        while self.n_seg1 < len(self.seq1) and self.n_seg2 < len(self.seq2):
            if self.p_seg1 == 1 and self.p_seg2 == 1:
                next_point = self.get_next_point()
                self.res.append((current_point, next_point))
                current_point = next_point
            else:
                current_point = self.get_next_point()
        return self.res


def get_intersection(first_sequence: List[Tuple[int]], second_sequence: List[Tuple[int]]) -> List[Tuple[int]]:
    if len(first_sequence) == 0 or len(second_sequence) == 0:
        return []
    pack = SegmentsPack(first_sequence, second_sequence)
    return pack.get_inter()


def read_sequence() -> List[Tuple[int]]:
    n = int(input())
    sequnce = []
    for i in range(n):
        start, end = map(int, input().split())
        sequnce.append((start, end))
    return sequnce


def print_sequence(sequence: List[Tuple[int]]) -> None:
    for segment in sequence:
        print(segment[0], segment[1])


first_sequence = read_sequence()
second_sequence = read_sequence()
intersection = get_intersection(first_sequence, second_sequence)
print_sequence(intersection)