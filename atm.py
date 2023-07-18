#!/usr/bin/python3
import getpass

# Creating lists of users, their PINs, and bank statements
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]

# While loop checks existence of the entered username
while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# Comparing PIN
count = 0
while count < 3:
    print('------------------')
    print('******************')
    pin = getpass.getpass('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    if pin.isdigit():
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
    else:
        print('--------------------------------')
        print('********************************')
        print('PIN MUST CONSIST OF 4 DIGITS')
        print('********************************')
        print('--------------------------------')
        count += 1

# In case of three unsuccessful PIN attempts, exit the program
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('*************************')
print()
print('--------------------------')
print('**************************')    
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main menu
while True:
    print('-------------------------------')
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
    print('*******************************')
    print('-------------------------------')

    if response == 's':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE', amounts[n], 'EURO ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')
        
    elif response == 'w':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 EURO NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] = amounts[n] - cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'EURO')
            print('***********************************')
            print('-----------------------------------')
            
    elif response == 'l':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 10 EURO NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] = amounts[n] + cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'EURO')
            print('****************************************')
            print('----------------------------------------')
    
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin = getpass.getpass('ENTER A NEW PIN: ')
        print('*****************************')
        print('-----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------')
            print('******************')
            new_ppin = getpass.getpass('CONFIRM NEW PIN: ')
            print('*******************')
            print('-------------------')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT FROM THE PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')

    elif response == 'q':
        exit()
    
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
