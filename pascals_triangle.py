# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1


def triangle(n):
    p = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = p[i - 1][j - 1] + p[i - 1][j]
        p.append(row)

    for r in p:
        print(r)

triangle(5)
