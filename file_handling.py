# file=open('Jabberwocky.txt',mode='r')

# for lines in file:
#     print(lines.lstrip())

# file.close()    

### Using With

# with open('Jabberwocky.txt','r') as f1:
#     for lines in f1:
#         print(lines.lstrip())

# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.read()

# print(type(f2))

# for char in f2:
#     print(char,end="")

# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.readlines()

# print(type(f2))

# for lines in f2:
#     print(lines.strip())

# with open('Jabberwocky.txt','r') as f1:
#     while True:
#         f2=f1.readline()
#         print(f2)

# -------------------------------------------

# #important


# with open('Jabberwocky.txt','r') as f1:
#     f2=f1.readline().rstrip()

# print(f2)    

# char="' Twasebv"
# f=f2.strip(char)
# print(f)


# --------------------------

# sen="My name is something and i am happy"

# rem_pre=sen.removeprefix("My")
# rem_suff=sen.removesuffix("happy")
# print(rem_pre)
# print(rem_suff)

# # 
# def rem_pr(str1,st2):
#     if str1.startswith(st2):
#         return str1[len(st2):]
#     else:
#         return str1

# def rem_su(str1,st2):
#     if str1.endswith(st2):
#         return str1[:(len(str1)-len(st2))]
#     else:
#         return str1
    
# n="my name is happy"
# pre="my"
# suf="happy"
# result1=rem_pr(n,pre)
# print(result1)
# result2=rem_su(n,suf)
# print(result2)

# ###############

# country file

# file='country_info.txt'

# with open(file) as f1:
#     f1_c=f1.readline()

#     for rows in f1:
#         data=rows.strip('\n').split('|')
#         print(data)

# headers=f1_c.strip('\n').split('|')
# print(headers)

#---------------------

# file='country_info.txt'
# countries={}
# with open(file) as f1:
#     f1.readline()
#     for rows in f1:
#         data=rows.strip('\n').split('|')
#         country,capital,code,code3,dialing,timezone,currency=data
#         country_dict={
#             'Country':country,
#             'Capital':capital,
#             'Code':code,
#             'Code3':code3,
#             'Dialing':dialing,
#             'Timezone':timezone,
#             'Currency':currency
#         }
        
#         countries[country.casefold()]=country_dict
        
        


# while True:    
#     Name=input("Enter the name of the country \n").casefold()

#     if Name in countries:
#         A1=countries[Name]['Capital']
#         print(f"The Capital of {Name} is {A1}")
#     else:
#         print("Invalid")
#         break



data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_file="plants_file.txt"

# with open(plants_file,mode='w') as f:
#     for plant in data:
#         print(plant,file=f)


# with open(plants_file) as f:
#     for plant in f:
#         print(plant.rstrip())

# write method

# flowers='flowers.txt'

# with open(flowers,mode='w') as fi:
#     for plant in data:
#         fi.write(f"{plant} \n")

# table='tablee.txt'

# with open(table,mode='w') as ta:
#     for i in range(1,4):
#         for j in range(1,11):
#    ta.write(f"{i}x{j}={i*j}\n") #write argument must be a string

#         print((),file=ta)    

# encoding-> utf-8

# with open('Jabberwocky.txt',encoding='utf-8') as f:
#     for lines in f:
#         print(lines.rstrip())

# ////////////////////////////////////////

# JSON

# import json

# languages = [
#     ['ABC', 1987],
#     ['Algol 68', 1968],
#     ['APL', 1962],
#     ['C', 1973],
#     ['Haskell', 1990],
#     ['Lisp', 1958],
#     ['Modula-2', 1977],
#     ['Perl', 1987],
# ]

# with open('test.json','w',encoding='UTF-8') as testfile:
#     json.dump(languages,testfile)

# with open('test.json','r',encoding='UTF-8') as f:
#     data=json.load(f)
#     print(data)

# parsing json file

# import json

# anomal='data.json'

# with open(anomal,'r',encoding="UTF-8") as jf:
#     d=json.load(jf)


# # print(d['description'])

# for year,value in d['data'].items():
#     year,value=int(year),float(value)
#     print(f"YEAR: {year}  {value:6.2f}")

# import json
# import urllib.request

# anomal='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

# with urllib.request.urlopen(anomal) as json_data:
#     file=json_data.read().decode('UTF-8')
#     d=json.loads(file)


# print(d['description'])

# for year,value in d['data'].items():
#     year,value=int(year),float(value)
#     print(f"YEAR: {year}  {value:6.2f}")


# CSV FILE

# import csv

# csv_file='OlympicMedals_2020.csv'

# with open(csv_file,encoding='utf-8',newline='') as medals:
#     headers=medals.readline().strip('\n').split(',')
#     reader=csv.reader(medals)
#     for row in reader:
#         print(row)


import csv

cereals='cereal_grains.csv'

with open(cereals,encoding='utf-8') as cereals_file:
    data=csv.reader(cereals_file,quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        print(row)