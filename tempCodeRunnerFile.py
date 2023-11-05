class Item:
    pay_rate=0.8 #class attribute
    all=[]

    def __init__(self,name : str,price : float,quantity = 0):
        
        print(f'instance is created {name}')
        
        # assert
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero"

        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)
 
    def calc(self):
        return self.price*self.quantity
    
    def discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"
    
    # @classmethod
    def change_payrate(self,amount):
        self.pay_rate=amount


item1=Item("Phone",100,5)
item2=Item("laptop",1000,3)
item3=Item("cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("KEyboard",75,5)

print(item1.price)
print(item1.pay_rate)
Item.change_payrate(1)
item1.discount()
print(item1.price)