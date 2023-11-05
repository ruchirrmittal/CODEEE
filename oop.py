# A function inside a class is called a method.

# creating a class:

# class Item:
#     def calc(self,x,y):
#         return x*y
    


# item1=Item()
# item1.name="phone"
# item1.price=100
# item1.quantity=5
# print(item1.calc(item1.price,item1.quantity))

# constructor __init__

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
    
    @classmethod
    def change_payrate(cls,amount):
        cls.pay_rate=amount

    @classmethod
    def from_str(cls,emp_str):
        name,price,quantity=emp_str.split("-")
        return cls(name,price,quantity)


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

# print(Item.all)
# for instances in Item.all:
#     print(instances.name)

# print(item1.calc())

# print(f"Item:{item1.name} and price:{item1.price} \nItem:{item2.name} and price:{item2.price}")
# print("\n")
# print("Item:{0.name} and price:{0.price} \nItem:{1.name} and price:{1.price}".format(item1,item2))
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)

# _______________________________________________________
# _______________________________________________________
# _______________________________________________________
# _______________________________________________________

'''
import datetime
import pytz


class Account:
    """
    simple class to store name and balance
    """
    @staticmethod
    def _current_time():
        utctime=datetime.datetime.utcnow()
        return pytz.utc.localize(utctime)
    
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transaction_list=[(Account._current_time(),balance)]
        print(f"Account created for {self.name}")
        self.display()

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.display()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount))
            self.transaction_list.append((Account._current_time(),amount))
    
    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            self.transaction_list.append((Account._current_time(),-amount))
            self.display()
        else:
            print("not enough balance")

    def display(self):
        print(f"Balance in the account is {self.balance}")
        
    def trans(self):
        for date,amount in self.transaction_list:
            if amount>0:
                tran_type="Deposited"
            else:
                tran_type="Withdrawn"
                amount*=-1
            print("{0:6} {1} on {2} (local time was {3})".format(amount,tran_type, date , date.astimezone()))

if __name__=="__main__":
    ruchir=Account("Ruchir",1000)
    ruchir.deposit(1000)
    ruchir.withdraw(200)
    ruchir.trans()
    ruchir.deposit(1)
    ruchir.withdraw(2000)
    ruchir.trans() 

'''
# _____________________________________________________________
# _____________________________________________________________
# _____________________________________________________________

class songs:
    