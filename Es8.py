
def num(l1):
    l2 = []
    diz = {1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove', 0:'zero'}
    for i in l1:
        l2.append(diz[i])

    return l2

l1 = []

for i in range(10):
    l1.append(i)

print(l1)
print(num(l1))


