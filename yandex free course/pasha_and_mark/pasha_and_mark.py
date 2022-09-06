def is_pasha_wins(n: int) -> bool:
    return n % 2 == 0


x = int(input())
if is_pasha_wins(x):
    print('Pasha')
else:
    print('Mark')
