def load_data():
    new_album=None
    new_artist=None
    artist_list=[]

    with open('albums.txt','r') as albums:
        for line in albums:
            artist_f,album_f,year_f,song_f=tuple(line.strip('\n').split('\t'))
            year_f=int(year_f)
            print(artist_f,album_f,year_f,song_f)

if __name__=="__main":
    load_data()