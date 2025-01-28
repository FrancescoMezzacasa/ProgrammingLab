def comune(l1, l2):
    check = 0
    for i in l1:
        if(i in l2):
            check = 1

    return check

l1 = [1, 2, 3, 4]
l2 = [7, 5, 6, 7]

print(comune(l1, l2))