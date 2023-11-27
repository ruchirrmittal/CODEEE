import random

class Enemy:

    def __init__(self,name="Enemy",hit_points=0,lives=1):
        self.name=name
        self.hit_points=hit_points
        self.lives=lives
        self.alive=True

    def take_damage(self,damage):
        saver=self.hit_points
        remaining_points=self.hit_points-damage
        if remaining_points >= 0:
            self.hit_points=remaining_points
            print(f"I took {damage} and have remaining {self.hit_points}")
        else:
            self.lives-=1
            self.hit_points=saver
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.alive=False
            

    def __str__(self) -> str:
        return f"Name:{self.name},Lives{self.lives},Hit Points{self.hit_points}"
    

class Troll(Enemy):
    
    def __init__(self, name):
        # super(Troll,self).__init__(name=name, hit_points=23, lives=1)
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print("Me {0.name}!!!!! {0.name} stomps you thomp thomp".format(self))


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3)

    def dodges(self):
        if random.randint(1,3)==3:
            print(f"{self.name} dodges the attack")
            return True
        else:
            return False
        
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self.hit_points=140

    def take_damage(self, damage):
        super().take_damage(damage//4)
