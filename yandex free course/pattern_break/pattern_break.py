def string_matches_template(s: str, template: str) -> bool:
    s, template = ' ' + s, ' ' + template
    t_len = len(template)
    previous = [False for _ in range(t_len)]
    current = [False for _ in range(t_len)]
    current[0] = True
    for j in range(1, t_len):
        if template[j] == '*':
            current[j] = current[j - 1]

    if current[0] == False:
        return False
    for i in range(1, len(s)):
        previous, current = current, previous
        for j in range(0, t_len):
            if template[j] in {s[i], '?'}:
                current[j] = previous[j-1]
            elif template[j] == '*':
                current[j] = current[j-1] or previous[j-1] or previous[j]
            else:
                current[j] = False
    return current[-1]


template = input()
string_to_check = input()
if string_matches_template(string_to_check, template):
    print('YES')
else:
    print('NO')
