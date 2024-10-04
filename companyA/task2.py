opts = []
opts4 = []
opts5 = []
for i in range(97, 97+26):
    for j in range(97, 97+26):
        if i == j:
            continue
        for z in range(97, 97+26):
            if i > j and j > z:
                continue
            if i < j and j < z:
                continue
            if j == z or i == z:
                continue
            a = f"{chr(i)}{chr(j)}{chr(z)}"
            opts.append(a)
print(len(opts))

for i in range(97, 97+26):
    for j in range(97, 97+26):
        if i == j:
            continue
        for z in range(97, 97+26):
            if i > j and j > z:
                continue
            if i < j and j < z:
                continue
            # if j == z or i == z:
            #     continue
            for w in range(97, 97+26):
                auxA = a+chr(w)
                if auxA[:2] == auxA[2::-1]:
                    continue
                if z > w:
                    continue
                if j <= z and z < w:
                    continue
                if w == z:
                    continue

                a = f"{chr(i)}{chr(j)}{chr(z)}{chr(w)}"
                opts4.append(a)

print(len(opts4))

