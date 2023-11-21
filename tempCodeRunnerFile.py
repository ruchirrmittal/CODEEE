class player:

    def __init__(self,name):
        self.name=name
        self._lives=3
        self.level=1
        self.score=0

    def get_lives(self):
        return self._lives
    
    def set_lives(self,value):
        self._lives=value

    lives=property(get_lives,set_lives)

# watch vid 352
p1=player("tim")
print(p1.name)
print(p1.score)
print(p1.lives)
p1.lives +=1
print(p1.lives)
