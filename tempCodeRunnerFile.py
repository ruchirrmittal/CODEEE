def fib():
    current,prev=0,1
    
    while True:
        current,prev=current + prev, current
        yield current

ser=fib()

for i in range(10):
    print(next(ser))