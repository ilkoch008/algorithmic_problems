IPV4 = "IPv4"
IPV6 = "IPv6"
ERROR = "Error"

v4_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
v6_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'}


def ok_v4(num: str):
    if len(num) > 3 or (num[0] == '0' and num != '0') or int(num) > 255:
        return False
    else:
        return True


def string_matches_template(s: str, template: str,  char_set: set) -> bool:
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
            if template[j] == s[i]:
                current[j] = previous[j-1]
            elif template[j] == '?' and s[i] in char_set:
                current[j] = previous[j - 1]
            elif template[j] == '*' and s[i] in char_set:
                current[j] = current[j-1] or previous[j-1] or previous[j]
            else:
                current[j] = False
    return current[-1]


# return IPV4, IPV6 or ERROR constant
def check_ip_address(ip_to_check: str) -> str:
    if string_matches_template(ip_to_check, '?*.?*.?*.?*', v4_set):
        nums = ip_to_check.split('.')
        for num in nums:
            if not ok_v4(num):
                return ERROR
        return IPV4
    elif string_matches_template(ip_to_check, '?*:?*:?*:?*:?*:?*:?*:?*', v6_set):
        nums = ip_to_check.split(':')
        for num in nums:
            if len(num) > 4:
                return ERROR
        return IPV6
    return ERROR


ip_to_check = input()
print(check_ip_address(ip_to_check))
