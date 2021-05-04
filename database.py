#create record
#update record
#read record
#delete record
#find user

#CRUD
import os

user_db_path = 'data/user_record/'

def create(account_number, userDetails):

    completion_state = False

    try:
        f = open('data/user_record/' + str(account_number) + '.txt', 'x')
    
    except FileExistsError:
        print('User already exist')
        #delete(account_number)
    else:
        f.write(str(userDetails))
        completion_state = True
    
    finally:    
        f.close()

        return completion_state
    #create a file
    #name of the file would be account_number.txt
    # add the user details to the file
    # return True

def read(user_account_number):
    print('read user record')
    # find user with account number
    # fetch contact of the file

def update(user_account_number):
    print('Update user record')
    #find user with account number
    # fetch the contact of the file
    #update the contact of the file
    #save the file
    # return true

def delete(user_account_number):
    
    is_delete_successful = False

    if (os.path.exists(user_db_path + str(user_account_number) + '.txt')):
        
        try:

            os.remove(user_db_path + str(user_account_number) + '.txt')
            is_delete_successful = True

        except FileNotFoundError:
            print('User not found')

        finally:

            return is_delete_successful

    #find user with account number

    #delete the user record [file]
    #return true

def find(user_account_number):
    print('find user')
    #find user record n the data folder

#print(delete(3786136944))
