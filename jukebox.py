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



SONGS_LIST_INDEX=3
SONG_TITLE=1

while True:

    print("Please choose a album.(Invalid choice is exit)")
    for index, (title,artist,year,songs) in enumerate(albums):
        print("{0} : {1}".format(index+1,title))

    choice=int(input())

    if 1<=choice<=len(albums):
        songs_list=albums[choice-1][SONGS_LIST_INDEX]
        # print(songs_list)
    else:    
        break    

    print("Please choose a song:")
    for index,(trackno,song) in enumerate(songs_list):
        print("{}:{} ".format(index+1,song))

    song_choice=int(input()) 
    
    if 1<= song_choice<= len(songs_list):
        title=songs_list[song_choice-1][SONG_TITLE]  
    else:
        print("Please choose a album.(Invalid choice is exit)")
        for index, (title,artist,year,songs) in enumerate(albums):
            print("{0} : {1}".format(index+1,title))
        


    print("Currently playing: {}.".format(title))
    print("="*50)    
       