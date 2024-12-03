with open('day1.txt') as f:
    a, b = [], []
    for line in f:
        x = line.split(' ')
        a.append(int(x[0]))
        b.append(int(x[-1]))
    print(sum([abs(i-j) for i, j in zip(sorted(a),sorted(b))]))