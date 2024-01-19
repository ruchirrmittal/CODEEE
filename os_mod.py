import os

# os.mkdir("random_val")

# for i in range(1,100):
#     os.mkdir(f"random_val/day{i+1}")

# for i in range(0,100):
#     os.rename(f"random_val/day{i+1}",f"random_val/tutorial{i+1}")

folders=os.listdir("random_val")

for f in folders:
    print(f)