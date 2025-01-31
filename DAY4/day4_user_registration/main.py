from user_management.user_handler import create_directories,save_user_data,username_exists,validate_user,change_password
''' Write python code that allows users to register new accounts, log in to existing 
accounts, and reset their passwords. 
1. For new registration, store unique username and password in text file 
2. For log in check login is valid or not 
3. For password change, check for username and change the password 
4. Use proper error handling 
5. Data should be stored: username1,password_hash1,email_or_phone1 
6. Store data in separate folder for employee login, admin login, manager 
login, etc. 
7. Use os module to create proper directory structure. Check if directories 
and files if they are exists.   
8. Create a user interface using Streamlit '''

def main():
    create_directories()
    def select_role():
        role=input('Enter Your Role from (Employee,Manager,Admin):')
        while role not in ['Employee','Manager','Admin']:
            print('Enter valid Role')
            role=input('ENter Youe Role from (Employee,Manager,Admin)')
        return role
    
    while True:
        print("1:New Reistration \n 2:Log in \n 3:Changing the password \n 4:exit ")
        choice=input('Enter Valid Choice :')
        match choice:
            case '1':
                print('Register New Account')
                print('========================')
                try:
                    role=select_role()
                    username=input('Enter user name:')
                    password=input('Enter valid password:')
                    gmail=input('Enter your gmail:')
                    mobile=input('Enter Your Mobile Number:')

                    if not username or not password or not gmail or not mobile:
                        raise ValueError('Please Enter Valid Number')
                    elif username_exists(role,username,password,gmail,mobile):
                        raise ValueError('Username already exists')
                    else:
                        save_user_data(role,username,password,gmail,mobile)
                    print('Registration Successful')
                except ValueError as e:
                    print(f'Error:{e}')

                    
            case '2':
                print('Login to Account')
                print('====================')
                try:
                    role=select_role()
                    username=input('Enter user name:')
                    password=input('Enter password:')
                    if not username or not password :
                        raise ValueError('Please Enter all the fields')
                    elif validate_user(role,username,password):
                        print(f'Welcome:{username}')
                        break
                    else:
                        print('Invalid Username and Password')
                        
                except ValueError as e:
                    print(f'Error:{e}')
                


            case '3':
                print('Change Your Password')
                print('=======================')
                try:
                    role=select_role()
                    username=input('Enter User name:')
                    old_password=input('Enter old Password:')
                    new_password=input('Enter New Password:')
                    if not username or not old_password or not new_password:
                        raise ValueError('Please enter all the fields')
                    elif validate_user(role,username,old_password):
                        change_password(role,username,new_password)
                        print('Password changes successfully')
                        break
                    else:
                        print('Enter valid details')
                except ValueError as e:
                    print(f'Error:{e}')


            case '4':
                print('Existing Program')
                break
            case _:
                print('Enter Valid Choice')

main()