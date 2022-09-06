let_to_num = {
    ' ': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

diffs = {4, 9, 40, 90, 400, 900}


def check(number):
    counter_I = 0
    counter_X = 0
    counter_C = 0
    counter_M = 0

    n_V = 0
    n_L = 0
    n_D = 0

    for i in range(len(number)):
        if number[i] == 'I':
            counter_I += 1
            if counter_I > 3:
                return True
        else:
            counter_I = 0

        if number[i] == 'X':
            counter_X += 1
            if counter_X > 3:
                return True
        else:
            counter_X = 0

        if number[i] == 'C':
            counter_C += 1
            if counter_C > 3:
                return True
        else:
            counter_C = 0

        if number[i] == 'M':
            counter_M += 1
            if counter_M > 3:
                return True
        else:
            counter_M = 0

        if number[i] == 'V':
            n_V += 1
            if n_V > 1:
                return True

        if number[i] == 'L':
            n_L += 1
            if n_L > 1:
                return True

        if number[i] == 'D':
            n_D += 1
            if n_D > 1:
                return True

    return False


def convert_to_arabic(number: str) -> int:
    if check(number):
        return -1
    l = len(number)
    res = 0
    i = 0
    max_val = 1000
    while i < l:
        if i+1 < l:
            if let_to_num[number[i]] < let_to_num[number[i+1]]:
                val = let_to_num[number[i+1]] - let_to_num[number[i]]
                if val not in diffs:
                    return -1
                else:
                    if val <= max_val:
                        res += val
                        max_val = val
                    else:
                        return -1
                i += 2
            else:
                val = let_to_num[number[i]]
                if val <= max_val:
                    res += val
                    max_val = val
                else:
                    return -1
                i += 1
        else:
            val = let_to_num[number[i]]
            if val <= max_val:
                res += val
                max_val = val
            else:
                return -1
            i += 1

    return res

roman_number = input()
print(convert_to_arabic(roman_number))