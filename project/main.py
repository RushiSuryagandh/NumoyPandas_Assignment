from utils.string_tools import * 
from user_management.user_handler import *
from file_processing.file_manager import *
'''while True:
    try:
        str1=input('Enyte string to perform operations:')
        if not str1.isalpha() and str1.isdigit():
            raise ValueError('Enter string values')
    except ValueError as e:
        print(f'Error :{e}')
    else:
        break

print(word_count_in_string(str1))
print(find_most_common_word(str1))
print(reverse_word(str1))
print(check_pallindrome(str1))'''


def string_tools_main():
    while True:
            print("\nChoose an action:")
            print("1. find the word count of string")
            print("2. find the most common word from string")
            print("3. reverse the string")
            print("4. check pallindrome of string")
            print("5. Exit")
            choice=input('Enter the number of action:')

            match choice:
                case '1':
                    str1=input('Enter String:')
                    try:
                        if not str1.isalpha() and str1.isdigit():
                            raise ValueError('Enter string values')
                    except ValueError as e:
                        print(f'Error :{e}')
                    print(word_count_in(str1))
                case '2':
                    str1=input('Enter String:')
                    try:
                        if not str1.isalpha() and str1.isdigit():
                            raise ValueError('Enter string values')
                    except ValueError as e:
                        print(f'Error :{e}')
                    print(find_most_common_word(str1))
                case '3':
                    str1=input('Enter String:')
                    try:
                        if not str1.isalpha() and str1.isdigit():
                            raise ValueError('Enter string values')
                    except ValueError as e:
                        print(f'Error :{e}')
                    print(reverse_word(str1))
                case '4':
                    str1=input('Enter String:')
                    try:
                        if not str1.isalpha() and str1.isdigit():
                            raise ValueError('Enter string values')
                    except ValueError as e:
                        print(f'Error :{e}')
                    print(check_pallindrome(str1))
                case '5':
                    print('Existing string tool operations')
                    break
                case _:
                    print('Enter Valid input')

def handle_user_main():
    users = []  # This will store the user data
    while True:
            # Get input from the user
            print("\nChoose an action:")
            print("1. Add User")
            print("2. Remove User")
            print("3. Get User Info")
            print("4. Update User Age")
            print('5. See all data')
            print("6. Exit")
            
            choice = input("Enter the number for the action: ")
            
            match choice:
                case '1':
                    username = input("Enter username: ")
                    age = int(input("Enter age: "))
                    try:
                        add_user(users, username, age)
                        print(f"User {username} added successfully.")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                case '2':
                    username = input("Enter username to remove: ")
                    try:
                        remove_user(users, username)
                        print(f"User {username} removed successfully.")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                case '3':
                    username = input("Enter username to get info: ")
                    try:
                        user_info = get_user_info(users, username)
                        print(f"User Info: {user_info}")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                case '4':
                    username = input("Enter username to update age: ")
                    new_age = int(input("Enter new age: "))
                    try:
                        update_user_age(users, username, new_age)
                        print(f"User {username}'s age updated to {new_age}.")
                    except ValueError as e:
                        print(f"Error: {e}")
                
                case '5':
                    print(users)
                    
                case '6':
                    print("Exiting program.")
                    break
                case _:
                    print("Invalid choice, please select a valid action.")

def Manage_file_main():
            
    while True:
        # Menu for user input
        print("\nChoose an action:")
        print("1. Enter Users")
        print("2. Save Users to File")
        print("3. Load Users from File")
        print("4. Write Text Analysis to File")
        print("5. Exit")

        # Get user input
        choice = input("Enter the number for the action: ")

        # Match-case to handle different user choices
        match choice:
            case '1':
                # Collect users from input
                users = get_users_from_input()
                print(f"Users entered: {users}")

            case '2':
                if users:
                    filename = input("Enter the filename to save users: ")
                    save_users_to_file(filename, users)
                else:
                    print("No users to save. Please enter users first.")

            case '3':
                filename = input("Enter the filename to load users from: ")
                loaded_users = load_users_from_file(filename)
                if loaded_users:
                    print("Loaded users:", loaded_users)

            case '4':
                filename=input('Enter the file name to save text analysis:')
                lode_file_data=input('Enter the file name to load the data for text analysis:')
                result_temp=load_users_from_file(lode_file_data)
                usernames = " ".join([user["username"] for user in result_temp])
                # print(type(usernames))
                result=word_count_in(usernames)
                print(result)
                # write_summary(filename,)

            case '5':
                print("Exiting the program.")
                break

            case _:
                print("Enter Valid Choice")

def main():
    while True:
        print("\nChoose an action:")
        print("1. To perform string tools function")
        print("2. To handle user")
        print("3. To manage file")
        print("4. Exit")
        choice=input('Enter the number of action:')
        
        match choice:
            case '1':
                print('======== String Toos Operations =======')
                string_tools_main()
            case '2':
                print('======== User Handler Operations =======')
                handle_user_main()
               
            case '3':
                print('======== Manage File Operations =======')
                Manage_file_main
                
            case '4':
                print('Existing Main Program')
                break
main()

