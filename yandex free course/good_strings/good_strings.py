class goodString:
    def __init__(self, data: str):
        self.good_string = []
        for i in range(len(data)):
            self.insert_to_end(data[i])

    def insert_to_end(self, char):
        if len(self.good_string) == 0:
            self.good_string.append(char)
            return
        lc = self.good_string[-1]
        if lc.upper() == char.upper() and lc.lower() == char.lower() and lc != char:
            self.good_string.pop()
        else:
            self.good_string.append(char)

    def get_str(self):
        res = ''
        for c in self.good_string:
            res = res + c
        return res


def convert_to_good_string(probably_bad_string: str) -> str:
    gs = goodString(probably_bad_string)
    return gs.get_str()

probably_bad_string = input()
print(convert_to_good_string(probably_bad_string))