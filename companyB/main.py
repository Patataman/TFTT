def solution(strings):
    Bs = strings.count("B")
    if Bs >= (len(strings) / 2 + 1):
        return -1
    else:
        for i, c in enumerate(strings):
            if c == "B":
                break
        moved = strings[i:] + "."*i
        new_bucket = ""
        moved_char = False
        for i, c in enumerate(moved):
            if moved[i] == "B":
                new_char = "B"
                if i > 0:
                    if new_bucket[i-1] == "B":
                        new_char = "."
            else:
                new_char = "."
                if new_bucket[i-1] == ".":
                    new_char = "B"
            new_bucket += new_char
            if new_bucket.count("B") == Bs:
                break
        if len(new_bucket) < len(strings):
            new_bucket += "."*(len(strings) - len(new_bucket))
        old_bs, new_bs = 0, 0
        diff = 0
        for old_c, new_c in zip(moved, new_bucket):
            if old_c == "B":
                old_bs += 1
            if new_c == "B":
                new_bs += 1
            if old_c != new_c:
                diff += 1
            if new_bs == old_bs == Bs:
                break
        return diff // 2

tests = [
    ["..BB", 1],
    ["BBBB", -1],
    ["...B.B...", 0],
    ["BB...B", 2],
    ["B.B.B..B", 1],
    ["BB.BB..B", -1],
    ["BB..B", 1],
    ["BB....B..", 2],
    ["B..B...BB.B", 3]
]
for string, diff in tests:
    _diff = solution(string)
    print(string, diff, _diff)
