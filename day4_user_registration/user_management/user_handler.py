import os

# create directory for storing data
def create_directories():
    roles=['Employee','Admin','Manager']
    for role in roles:
        directory=f'./day4_user_registration/{role}_data'
        if not os.path.exists(directory):
            os.makedirs(directory)

# Save user data into appropriate file
def save_user_data(role,username,password,email,phone):
    file_path=f'./day4_user_registration/{role}_data/{role}.txt'
    with open(file_path,'a') as file:
        file.write(f'{username},{password},{email},{phone}\n')


# check username exist or not
def username_exists(role,username,password,email,phone):
    file_path=f'./day4_user_registration/{role}_data/{role}.txt'
    if os.path.exists(file_path):
        with open(file_path,'r')as file:
            users=file.readlines()
            for user in users:
                stored_username=user.split(',')[0]
                stored_password=user.split(',')[1]
                stored_email=user.split(',')[2]
                stored_phone=user.split(',')[3]
                if stored_username==username or stored_password ==password or stored_email==email or stored_phone==phone:
                    return True
    return False

# To validate the user
def validate_user(role,username,password):
    file_path=f'./day4_user_registration/{role}_data/{role}.txt'
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            users=file.readlines()
            for user in users:
                store_username=user.strip().split(',')[0]
                store_password=user.strip().split(',')[1]
                if store_username==username and store_password==password:
                    return True
    return False

# validate_user('Admin','rushi','rushi@123')

# To change Password
def change_password(role,username,new_password):
    file_path=f'./day4_user_registration/{role}_data/{role}.txt'
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            users=file.readlines()
        
        with open(file_path,'w') as file:
            for user in users:
                store_username,store_password,store_email,store_phone=user.strip().split(',')
                if store_username==username:
                    file.write(f'{username},{new_password},{store_email},{store_phone}\n')
                    return True
                else:
                    file.write(user)
    return False
    


