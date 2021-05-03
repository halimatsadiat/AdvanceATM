def account_number_validation(account_number):
   
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print('Invalid Account number, account number should be integer')
                return False
            except TypeError:
                print('Invalid account type')
                return False
        else:
            print('Account Number cannot be more than 10 digits')
            return False 
    else:
        print('Account Number is a required field')
        return False 

