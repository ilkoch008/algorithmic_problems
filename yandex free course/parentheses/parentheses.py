from typing import List


square_open = 1
square_close = 2
round_open = 3
round_close = 4


def generate(cur_str: str, max_len: int, stack):
    if len(cur_str) == max_len and len(stack) == 0:
        yield cur_str
    elif len(cur_str) < max_len:
        if square_open not in stack:
            yield from generate(cur_str + '(', max_len, stack + [round_open])
            yield from generate(cur_str + '[', max_len, stack + [square_open])
            if len(stack) > 0:
                s_copy = stack.copy()
                s_copy.pop()
                yield from generate(cur_str + ')', max_len, s_copy)
        else:
            yield from generate(cur_str + '[', max_len, stack + [square_open])
            s_copy = stack.copy()
            s_copy.pop()
            yield from generate(cur_str + ']', max_len, s_copy)


def generate_sequences(n: int) -> List[str]:
    if n % 2 != 0 or n == 0:
        return []
    else:
        res = list(generate('', n, []))
        return res


n = int(input())
sequnces = generate_sequences(n)
for seq in sequnces:
    print(seq)
