words = []

with open("selected_strings.txt") as fd:
    words = fd.read().splitlines()

# Encuentra shagramas
# Para eso la diferencia en cada letra debe ser igual

sorted_words = sorted(words)

same_k = []
for i, w in enumerate(sorted_words):
    w = "".join(sorted(w))
    for w2 in sorted_words[i:]:
        if len(w) != len(w2):
            continue
        w2 = "".join(sorted(w2))
        diff_k = None

        for c1, c2 in zip(w, w2):
            k = ord(c2) - ord(c1)
            if diff_k is None:
                diff_k = k
            if k != diff_k:
                diff_k = None
                break
        if diff_k and diff_k >= 1 and diff_k <= 25:
            same_k.append([w, w2, diff_k])

print(len(same_k), list(same_k)[:10])

word = None
max_w = -1
og_w, k_w, _k = None, None, None
for w0, w1, k in same_k:
    weight0, weight1 = 0, 0
    for c in w0:
        weight0 += ord(c)
    for c in w1:
        weight1 += ord(c)

    if weight0 > weight1:
        weight = weight0
    else:
        weight = weight1

    if weight > max_w:
        max_w = weight
        og_w = w0
        k_w = w1
        _k = k

print(max_w, og_w, k_w, _k)


# words_lN = [w for w in words if len(w) == 10]
# 
# max_w = -1
# word = None
# 
# 
# for w in words_lN:
#     weight = 0
#     for c in w:
#         weight += ord(c)
#     if weight > max_w:
#         max_w = weight
#         word = w
# 
# print(max_w, word)
