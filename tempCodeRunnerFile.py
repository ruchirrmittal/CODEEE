import csv

cer_file='cereal_grains.csv'

with open(cer_file,encoding='utf-8',newline='') as data:
    reader=csv.DictReader(data)
    for row in reader:
        print(row)