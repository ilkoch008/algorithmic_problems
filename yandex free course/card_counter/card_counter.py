def get_card_count(n, k, cards) -> int:
    res = sum(cards[:k])
    prev_val = res
    for i in range(1, k+1):
        prev_val = prev_val + cards[n-i] - cards[k-i]
        res = max(res, prev_val)
    return res


n = int(input())
k = int(input())
cards = list(map(int, input().split()))

print(get_card_count(n, k, cards))