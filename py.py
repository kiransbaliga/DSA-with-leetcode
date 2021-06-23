import itertools

s='green'
l1= list(itertools.combinations(s,1))
l2= list(itertools.combinations(s,2))
l3= list(itertools.combinations(s,3))
l4= list(itertools.combinations(s,4))

for i in l1:
    print(*i)
for i in l2:
    print(*i)
for i in l3:
    print(*i)
for i in l4:
    print(*i)
print("green")