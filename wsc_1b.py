with open('day1.txt') as f:
    a,b = [], {}
    for line in f:
        x = line.split(' ')
        a.append(int(x[0]))
        b[int(x[-1])] = b[int(x[-1])]+1 if (int(x[-1]) in b) else 1
    print(sum(map (lambda i:i*b[i] if i in b else 0, a)))