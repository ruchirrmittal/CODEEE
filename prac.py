# data=[32,33,45,45,39,92,4,5,7,7,93,24,35,46,45,455,34,2,35,654,22]

# min=10
# max=100
# data.sort()

# stop=0

# for index,value in enumerate(data):
#     if value>=10:
#         stop=index
#         break

# print(data)
# print(stop)
# del data[0:stop]
# print(data)

# tup=("are","you","ready","to")
# a,b,c,d=tup
# print(a)
# print(d)

# albums=[("aa","bb","cc","dd"),
#         ("aa1","bb1","cc1","dd1"),
#         ("aa2","bb2","cc2","dd2"),
#         ("aa3","bb3","cc3","dd3")           
#         ]      



# for name,artist,year,singer in albums:
#     print("Album: {0}, Artist: {1}, Year:{2}, Singer: {3}".format(name,artist,year,singer))



albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),

    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),

    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
]
 
# album=albums[2]
# # print(album)
 
# songs=album[3]


# song=songs[1]


# ren=song[1]


# rennn=albums[2][3][1][1]
# print(rennn)
# for name,artist,year,songs in albums:
#     print(" Album : {} , Artist : {} , year {},Songs: {} ".format(name,artist,year,songs))
#     for index,song in enumerate(songs):
#         print("{}: {} ".format(index+1,song))

# for album in albums:
  # print()