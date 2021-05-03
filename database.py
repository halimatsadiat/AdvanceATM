#create record
#update record
#read record
#delete record
#find user

#CRUD

def create(account_number, userDetails):
    print('create a new record')

    f = open('data/' + str(account_number) + '.txt', 'x')
    f.write(str(userDetails))
    f.close()
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
    print('delete user record')
    #find user with account number
    #delete the user record [file]
    #return true

def find(user_account_number):
    print('find user')
    #find user record n the data folder
create(1234567890,['sadiat', 'ogidan', 'sadiat@gmail.com', 'sad', 233])
