T = int(input())

for _ in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append([m for m in map(int, input().split(' '))])

    elements = [(indexh, indexv, element)for indexh, row in enumerate(matrix) for indexv, element in enumerate(row)]

    inversion = 0

    for column in elements:
        for cell in elements:
            if column[2]>cell[2] and column[0]<=cell[0] and column[1]<=cell[1]:
                inversion += 1

    print(inversion)
