table='tablee.txt'

with open(table,mode='w') as ta:
    for i in range(3):
        for j in range(1,10):
            print(f"{i}x{j}={i*j}",file=ta)