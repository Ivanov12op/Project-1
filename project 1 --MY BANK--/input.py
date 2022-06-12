
x=None
user_choice=()
choice_user_data=list(user_choice)
new_balance= 0
deposit_new= 0
def choice_user_data( ):
    while True:
     element=int(input('Select your number from the above menu : '))
     user_choice.append(element)
     print( f'Choice number is : { x } ')
     
     for num in choice_user_data:
        if x==1:
          name=input('Please Input Fullname (ex. Ada Jochn) : ')
          user_name.append(name)
        if x==2:
            withdraw=input( 'Please input a value to withdraw: ')
            new_balance.append(withdraw)
        if x==3:
            deposit = input ( 'Please input a value to deposit on account :')
            deposit_new.append(deposit)  
        if x==4:
            pass
        if x==5:
            print( 'Thank you for your visit ,have a nice day !')
            break
    # print("choice_user_data")

""" Select your number from the above menu : 1=<x<=5 \n
Choisnumber is 1 is selekted by the customer: \n
Number of Customers : 1  \n
Input Fullname: Ada Jochn \n
if x==1:
    print( user name )
if x==2: 
print( 'Pease input a value to Withdraw: ')
Please input a pin of choice : x \n
if x==3:
print( 'Pease input a value to deposit to start on account : ') 
if a==Exit and Quit"""


