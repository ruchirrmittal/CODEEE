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

# Quote_nonnumeric is used to not let the numeric data to be returned as string

# import csv

# cereals='cereal_grains.csv'

# with open(cereals,encoding='utf-8') as cereals_file:
#     data=csv.reader(cereals_file,quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         print(row)


# delimiter

# import csv

# with open('country_info.txt',encoding='utf-8',newline='') as fi:
#     country_data=csv.reader(fi)
#     for row in country_data:
#         print(row)

# program above returns each row of the data as a single string and to differentiate it we use delimiter
# import csv

# with open('country_info.txt',encoding='utf-8',newline='') as fi:
#     country_data=csv.reader(fi,delimiter='|')
#     for row in country_data:
#         print(row)


# sniffer class

# import csv

# with open('country_info.txt',encoding='utf-8',newline='') as country_file:
#     sample=country_file.read()
#     country_dialect=csv.Sniffer().sniff(sample)
#     country_file.seek(0)  #this is used because in line 292 the file is completely read until the end and it sends the cursor back to the start
	
#     country_data=csv.reader(country_file,dialect=country_dialect)
#     for row in country_data:
#         print(row)

# print("*" * 80)
# #watch lecture 269 to understand this part given below.

# attributes = [
#     'delimiter',
#     'doublequote',
#     'escapechar',
#     'lineterminator',
#     'quotechar',
#     'quoting',
#     'skipinitialspace',
# ]
 
# # for attribute in attributes:
# #     print(f'{attribute}: {getattr(country_dialect, attribute)}')


# for attribute in attributes:
#     print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')


# writing a csv file

# import csv

# cereals = [
#     ["Barley", 556, 1.7, 32.9, 10.1, 13.8],
#     ["Durum", 339, 5, 27.4, 4.09, 9.7],
#     ["Fonio", 240, 1, 4, 1.7, 0.05],
#     ["Maize", 442, 7.4, 37.45, 6.15, 11.03],
#     ["Millet", 484, 2, 37.9, 13.4, 9.15],
#     ["Oats", 231, 9.2, 35.1, 10.3, 3.73],
#     ["Rice (Brown)", 346, 2.8, 38.1, 9.9, 0.8],
#     ["Rice, (White)", 345, 3.6, 37.6, 5.4, 0.1],
#     ["Rye", 422, 2, 31.4, 18.2, 21.2],
#     ["Sorghum", 316, 3, 37.8, 9.92, 9.15],
#     ["Triticale", 338, 1.81, 36.6, 19, 0.9],
#     ["Wheat", 407, 1.2, 27.8, 12.9, 13.8],
# ]

# column_headings = ["Cereal", "Calories", "Fat", "Protein", "Fibre", "Vitamin E"]

# output_filename = 'my_cereals.csv'


# with open(output_filename,'w',encoding='utf-8',newline='') as cer_file:
#     writer=csv.writer(cer_file,quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(column_headings)   #this prints just one line whereas the rows print multiples
#     writer.writerows(cereals)


# dictreader class in csv

# import csv

# cer_file='cereal_grains.csv'

# with open(cer_file,encoding='utf-8',newline='') as data:
#     reader=csv.DictReader(data)
#     for row in reader:
#         print(row)

# country challenge using dict reader

# import csv
# country_file='country_info.txt'

# countries={}

# with open(country_file,encoding='utf-8',newline='') as data:
#     sample=data.read()
#     co_dialect=csv.Sniffer().sniff(sample)
#     data.seek(0)
#     reader=csv.DictReader(data,dialect=co_dialect)
#     for row in reader:
#         countries[row['Country'].casefold()]=row
		
# while True:    
#     Name=input("Enter the name of the country \n").casefold()

#     if Name in countries:
#         A1=countries[Name]['Capital']
#         print(f"The Capital of {Name} is {A1}")
#     else:
#         print("Invalid")
#         break

# import csv
# country_file='country_info.txt'

# dialect=csv.excel
# dialect.delimiter='|'

# countries={}

# with open(country_file,encoding='utf-8',newline='') as data:
#     heading=data.readline().strip('\n').split(dialect.delimiter)
#     for index,value in enumerate(heading):
#         heading[index]=value.casefold()
# #the purpose of this program is to have your own custom headers rather than creating a completely new dict
#     reader=csv.DictReader(data,dialect=dialect,fieldnames=heading)
#     for row in reader:
#         countries[row['country'].casefold()]=row


# reading and writing        IMP

# import csv

# ordering = ['Country', 'Gold', 'Silver', 'Bronze', 'Rank']
# # Note the lack of 'Total' in `ordering`

# with open('OlympicMedals_2020.csv', encoding='utf-8', newline='') as data, open('medals_dict.py', 'w', encoding='utf-8') as output_file:
#     # Write the first part of the code (excluding the actual data)
#     print('import csv', file=output_file)
#     print(file=output_file)
#     print('medals_table = [', file=output_file)

#     reader = csv.DictReader(data)
#     for row in reader:
#         print(row)

#     # Read each row from the CSV file, as a dictionary,
#     # and produce a new dictionary containing the key/value
#     # pairs we want, in the order we want.
#     for row_dict in reader:
#         new_dict = {}
#         # Only print the values for the keys we want
#         # (in the order we want them).
#         for key in ordering:
#             value = row_dict[key]
#             if value.isnumeric():
#                 value = int(value)
#             new_dict[key.casefold()] = value
			

#         # print the dictionary to the output file
#         # (indented by 4 spaces, with a trailing comma).
#         print(f'    {new_dict},', file=output_file)

#     # All the data rows have been written, print the terminating ]
#     print(']', file=output_file)
#     print(file=output_file)  # and finish with a blank line.


# dictwriter

# open medals_dict.py

# zip function

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
		  ("Bad Company", "Bad Company", 1974),
		  ("Nightflight", "Budgie", 1981),
		  ("More Mayhem", "Imelda May", 2011),
		  ("Ride the Lightning", "Metallica", 1984),
		  ]

keys=['album','artist','year']

# for row in albums:
#     zip_object=zip(keys,row)
#     print(zip_object)
#     for item in zip(keys,row):
#         print(f"\t {item} ")

# for row in albums:
#     zip_object=zip(keys,row)
#     albums_dict=dict(zip_object)
#     print(albums_dict)


# import csv

# output_album='album_dict.csv'

# with open(output_album,'w',encoding='utf-8',newline='') as data:
#     writer=csv.DictWriter(data,fieldnames=keys)
#     writer.writeheader()

#	  for row in albums:
#         zip_object=zip(keys,row)
#         albums_dict=dict(zip_object)
#         writer.writerow(albums_dict)





