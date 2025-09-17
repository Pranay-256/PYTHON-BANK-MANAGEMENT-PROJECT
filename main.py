
import json   #for performing json operations
import random  #for generating ramdom pin combinations
import string  #for performing string operations 
from pathlib import Path   #for locating the json file data.json
class Bank:
    database = 'data.json'      
    data = []  #dummy data
    try:
      if Path(database).exists():  
        with open(database) as fs:
           data = json.loads(fs.read())  #json.loads takes a JSON string and converts it into a Python object.
      else:
         print("no such files exists")     
    except Exception as err:
        print(f"an exception has occured as {err}")        

    @staticmethod   #normal function which belongs to the class Bank
    def __update():  #private
       with open(Bank.database,'w') as fs:
          fs.write(json.dumps(Bank.data))  #json.dumps takes a Python object and converts it into a JSON string
           
    @classmethod   #class level function
    def __generateaccno(cls):  #private
       while (True): #running until finds a unique account number
          alphabets = random.choices(string.ascii_letters,k=3)   #gives 3 random alphabets as lsit
          nums = random.choices(string.digits,k=3)   #gives 3 random strings as list
          spchar = random.choices("!@#$%^&*",k=1)  # gives random special character as list
          id = alphabets + nums + spchar
          random.shuffle(id)  #shuffles the id list
          accno =  "".join(id)   #joining the elements of id to a single string 
          if all(accno!= i ['accountno'] for i in cls.data): #check for unique account numbers
             return accno 
         
    def createaccount(self):
        info = {
           "name" : input("enter your name : "),
           "age" : int(input("enter your age : ")),
           "email" : input("enter your email id :"),
           "pin_no" : int(input("tell your pin : ")),
           "accountno" : Bank.__generateaccno(),
           "balance" : 0  
        }
        if info['age']< 18 or len(str(info['pin_no'])) != 4:
           print("sorry you cannot create your account")
        else:
           print("account has been created succesfully")
           for i in info:
              print(f"{i} : {info[i]}")
           print("remember your account number and pin number")   

           Bank.data.append(info)
           Bank.__update()

    def depositmoney(self):
       accno = input("please enter your account number : ")
       pin = int(input("please enter your pin number : ")) 
       userdata = [i for i in Bank.data if i['accountno'] == accno and i['pin_no'] == pin]

       if userdata == False: #empty list is considered as falsey and the condtiton checks if the list is empty or not 
          print("sorry no data found")
       else:
          print(f"you have {userdata[0]['balance']} rupees in your account")
          amount = int(input("how much you want to deposit ? : "))
          if amount > 100000:
             print("depositing amount should be less than 100000")
          elif amount <=0:
             print("depositing amount cannot be less than or equal to  0 ")  
          else:
             userdata[0]['balance'] +=amount ##
             Bank.__update()
             print("your amount has been deposited succesfully ")
             print(f"balance = {userdata[0]['balance']} rupees")

    def withdrawmoney(self):
       accno = input("please enter your account number : ")
       pin = int(input("please enter your pin number  : ")) 
       userdata = [i for i in Bank.data if i['accountno'] == accno and i['pin_no'] == pin]

       if userdata == False: #empty list
          print("sorry no data found")
       else:
          print(f"you have {userdata[0]['balance']} rupees in your account")
          amount = int(input("how much you want to withdraw ? : "))
          if amount > userdata[0]['balance']:
             print(f"withdrawing amount should be less than {userdata[0]['balance']}")
          elif amount <=0:
             print("withdrawing amount cannot be less than or equal to 0 ")  
          else:
             userdata[0]['balance'] -=amount #accessing zeroeth indexed element of the list i.e the dictionary inside the list and updating balance of that dictionary
             Bank.__update()
             print("your amount has been withdrewn succesfully ")
             print(f"balance = {userdata[0]['balance']} rupees")

    def checkdetails(self):
       accno = input("please enter your account number : ")
       pin = int(input("please enter your pin number  : "))
       userdata = [i for i in Bank.data if i['accountno'] == accno and i['pin_no'] == pin] 
       print("your information are : \n")     
       for i in userdata[0]: # accessing zeroeth indexed element of the list i.e the dictionary inside the list
          if i =='balance':
             continue
          else:
             print(f"{i} : {userdata[0][i]}") # accessing first element of the dictionary which iterates automatically using for loop
       print(f"balance : {userdata[0]['balance']} rupees")       

    def updatedetails(self):
       accno = input("please enter your account number : ")
       pin = int(input("please enter your pin number  : "))
       userdata = [i for i in Bank.data if i['accountno'] == accno and i['pin_no'] == pin]

       if userdata == False:
          print("no such user data found")
       else:
          print("the list of the data which you can change are shown below : \n")
          print(" name")
          print(" email id")
          print(" pin number\n")   
          print("fill the details of the fields which you want to change or press enter if you don't want to change\n")
          newdata= {                                                                 #another dummy data
             "name" : input("please tell your new name or press enter to skip : "),
             "email" : input("please tell your new email or press enter to skip : "),
             "pin_no" : input("enter your new pin or press enter to skip :") # pin_no is string because we could need to press enter which is not possible if the data type is int without giving any integer
              }                                                              # later on we have typecasted it to int
          if newdata['name'] == "":
             newdata['name'] = userdata[0]['name']
          if newdata['email'] =="":
             newdata['email'] = userdata[0]['email']
          if newdata['pin_no'] =="":
             newdata['pin_no'] = userdata[0]['pin_no']    

          newdata['age'] = userdata[0]['age']
          newdata['accountno'] = userdata[0]['accountno']
          newdata['balance'] = userdata[0]['balance']   

          if type(newdata['pin_no']) == str: # typecating pin_no to int
             newdata['pin_no'] = int(newdata['pin_no'])

          for i in newdata :
             if newdata[i] == userdata[0][i]:
                continue
             else:
                userdata[0][i] = newdata[i] 

          Bank.__update() 
          print("details have been updated succesfully")

    def deleteaccount(self):
       accno = input("please enter your account number : ")
       pin = int(input("please enter your pin number : "))
       userdata = [i for i in Bank.data if i['accountno']==accno and i['pin_no']==pin]

       if userdata == False:
          print("sorry no such data exists")  
       else:
          check = input("press y if you want to delete your account or n if you don't want to delete your account : ")
          if check =='n' or check =='N':
             print("account deletion process has been terminated")
          elif check =='y' or check =='Y':
             index = Bank.data.index(userdata[0])   
             Bank.data.pop(index)
             print("account has been succesfully delelted")
             Bank.__update()
          else:
             print("invalid input received operation has been terminated")         

user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for viewing your details")
print("press 5 for updating your detais")
print("press 6 for deleting your account")

check = int(input("tell your response : "))
if check == 1:
   user.createaccount()
if check == 2:
   user.depositmoney() 
if check == 3:
   user.withdrawmoney() 
if check == 4:
   user.checkdetails()
if check == 5:
   user.updatedetails()
if check == 6:
   user.deleteaccount()   


