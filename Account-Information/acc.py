class Account:
    def __init__(self, filepath):
        self.filepath = filepath # Making the filepath as an instance variable hence it could be used 
        with open(filepath, 'r') as file: #as self.filepath in all the functions inside the class 
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount 

    def deposit(self,amount):
        self.balance = self.balance + amount 
    
    def commit(self, filepath ):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))
    

        
account = Account("balance.txt")
#print(account.balance)

#account.withdraw(100)
#print(account.balance)
# After withdrawal the changes are needed to be written in the file hence we utilise the commit button 

account.commit("balance.txt")

class Checking(Account):
    """ This class generates checking objects""" # Docstring
    type = "checking" # Class variables are created outside the class and can be accessed by all the members of the class
    def __init__(self,filepath,fee): # we can have instance variable in the inheritance class also
        #implementing inheritance 
        self.fee = fee
        Account.__init__(self, filepath)
    def transfer(self,amount):
        self.balance = self.balance - amount -self.fee


ajay_checking = Checking("ajay.txt", 1)
ajay_checking.transfer(100)
print(ajay_checking.balance)
ajay_checking.commit("ajay.txt")

deepu_checking = Checking("deepu.txt", 1)
deepu_checking.transfer(100)
print(deepu_checking.balance)
deepu_checking.commit("deepu.txt")

print(deepu_checking.__doc__)




# After creating the inheritance object one needs to commit the changes 
