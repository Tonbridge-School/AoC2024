import re
with open('day3.txt') as f: print(sum(map(lambda line: sum(map(lambda i: int(i[0])*int(i[1]), re.compile(r'mul\((\d{1,3})\,(\d{1,3})\)').findall(line))), f)))