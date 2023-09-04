vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# a=vehicles['er5']
# b=vehicles.get('jimny')
# print(a)
# print(b)

# for key in vehicles:
#     a=vehicles[key]
#     print(a)

# for key,value in vehicles.items():
#     print(key,value,sep=" : ")


# vehicles['soso']="ooga booga boo" 
# for key,value in vehicles.items():
#     print(key,value,sep=" : ")


for i in range(3):
    key=input("key \n")
    value=input("value \n")
    vehicles[key]=value

for key,value in vehicles.items():
    print(key,value,sep=" : ")