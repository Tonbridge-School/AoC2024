import re
p, m = re.compile(r'(mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\))'), re.compile(r'mul\((\d{1,3})\,(\d{1,3})\)')
with open('day3.txt') as f:
    t, x = 0, sum((p.findall(line) for line in f),[])
    predicate = True
    for item in x:
        s = m.findall(item)
        if s == []:
            predicate = False if len(item)>5 else True
        elif predicate:
            t += int(s[0][0])*int(s[0][1])
    print(t)
        
