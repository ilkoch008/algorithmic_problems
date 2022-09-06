def string_matches_template(s: str, template: str) -> bool:
    stack = []
    t_len = len(template)
    s_len = len(s)
    stack.append((0, 0))
    while len(stack) > 0:
        s_i, t_i = stack[-1]
        stack.pop()
        while (s_i < s_len and t_i < t_len) and (s[s_i] == template[t_i] or template[t_i] == '?'):
            s_i += 1
            t_i += 1
        if t_len > t_i and template[t_i] == '*':
            while t_i < t_len:
                if template[t_i] != '*':
                    break
                t_i += 1
            for j in range(s_len, s_i-1, -1):
                stack.append((j, t_i))
        elif s_i == s_len and t_i == t_len:
            return True
    return False


template = input()
string_to_check = input()
if string_matches_template(string_to_check, template):
    print('YES')
else:
    print('NO')