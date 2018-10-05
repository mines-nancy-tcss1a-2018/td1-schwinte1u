def solve(n):
    sum_digits=0
    indice=2**n
    while indice>0:
        sum_digits += (indice%10)
        indice = indice//10
    return(sum_digits)

print(solve(1000))

assert(solve(15)==26)