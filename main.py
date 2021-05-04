#register
#username, password
#generation user id

#login 
#username or email and password

#bank operation
#initializing the system

import random
import validation
import database



def init():

    print('Welcome to bankPHP')

    haveAccount = int(input('do you have an account with us: 1. (yes) 2 (no) \n'))
    
    if (haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()

def login():
    print('******* Login *******')
    account_number_from_user = input('What is your account number? \n')
    
    is_valid_account_number = validation.account_number_validation(account_number_from_user)
    
    if is_valid_account_number:

        password = input('What is your password \n')

        for account_number,userDetails in database.items():
            if (account_number == int(account_number_from_user)):
                if (userDetails[3] == password):
                    bankOperation(userDetails)

        print('Invalid account or password')
        login()
    else:
        init()  

def register():
    print('******Register******')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('create a password for yourself \n')
  
    account_number = generate_account_number()

    #database[account_number] = [ first_name, last_name, email, password, 0]
    is_user_created = database.create(account_number,[first_name, last_name, email, password, 0]) 

    if is_user_created:
        print('Your account has been created')
        print('== ==== ====== ===== ===')
        print('Your account number is %d' %account_number)
        print('== ==== ====== ===== ===')
        login()
    
    else:
        print('something went wrong')
        register()

def bankOperation(user):
    print('welcome %s %s ' % ( user[0], user[1]))
    
    selected_option = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) exit \n'))
    if ( selected_option == 1):
        deposit_operation()

    elif ( selected_option == 2):
        withdrawal_operation()

    elif (selected_option == 3):
        logout()

    elif ( selected_option == 4):
        exit()

    else:
        print('Invalid option selected')

def withdrawal_operation():
    withdraw_option = int(input('How much would you like to withdraw? \n'))
    print('Take your #' + withdraw_option + ' cash')
    print('Thank you for banking with us')

def deposit_operation():
    deposit_option = int(input('How much do you want to deposit? \n'))
    print('You have succesfully deposited #' + deposit_option)
    print('Thank you for banking with us')
    
def generate_account_number():
    return random.randrange(1111111111,9999999999)

def logout():
    login()
### ACTUAL BANKING SYSTEM

#print(generate_account_number())
init()