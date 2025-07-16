def fibo_dp_mem(n):
    mem = [0, 1]
    for i in range(2, n + 1):
        mem[i%2] = mem[0] + mem[1]
    return mem[n%2]

for i in range(10):
    print(fibo_dp_mem(i))