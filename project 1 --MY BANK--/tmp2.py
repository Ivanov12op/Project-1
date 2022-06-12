
from msilib.schema import Property


class Account:
    count = 0
    
    def __init__(self,name,balance):
        Account.count +=1
        self.name=name
        self.balance=balance       

        print( f'Registered customers: {Account.count}')
    
    @Property
    def info_account (self): 
        print(f"Hello {self.name} you have {self.balance} lv. ")

    @balance.setter
    def set_balnce ( self, new_balance ) :
        self.balance = new_balance
        return
    def get_balance  (self):
        return self.balance

    @Property
    def info_account (self): 
        
        print(f"Hello {self.name} you have {self.balance} lv. ")
    
    

client1=Account('Ivan Ivanov',100 )
client2=Account('Alexa' ,200 )
client3=Account('Kiko Kirov',400 )

print(client2.balance)
