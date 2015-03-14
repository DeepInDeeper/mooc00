def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fb(n-2)
    while True:
        #fib(n) =fibn_1 +fibn_2
        next = fibn_1+fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
# fib = genFib()
# for n in fib:
#   print n
