def fact_rec(n):
    if(n == 1):
        return 1
    return(n * fact_rec(n - 1))

def fact_it(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f



n = int(input('Inserire n: '))

print(fact_rec(n))
print(fact_it(n))