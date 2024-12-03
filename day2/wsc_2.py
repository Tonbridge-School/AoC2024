def safe(lst):
    a = set([j-i for i, j in zip(lst[:-1], lst[1:])])
    return True if a.issubset({1,2,3}) or a.issubset({-1,-2,-3}) else False
    
def damp(lst):
    newlst = list(map(lambda x:[item for index, item in enumerate(lst) if index!=x],range(len(lst)))) 
    return True if True in list(map(safe, newlst)) else False

with open('day2.txt') as f:
    s = list(map(lambda x:list(map(int,x.strip().split(' '))),f.readlines()))
    print(sum(list(map(lambda y: 1 if damp(y) else 0,s))))
