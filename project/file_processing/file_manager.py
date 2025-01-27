import json
# get user from input
def get_users_from_input():
    users = []
    while True:
        username = input("Enter username (type 'exit' to finish): ")
        if username.lower() == 'exit':
            break
        try:
            age = int(input(f"Enter age for {username}: "))
            users.append({"username": username, "age": age})
            
        except ValueError:
            print("Invalid age input, please enter a valid number.")
        
    return users

# Function to save users to a file
def save_users_to_file(filename, users):
    try:
        with open(filename, 'w') as file:
            json.dump(users, file)
        print(f"Users have been successfully saved to {filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to load users from a file
def load_users_from_file(filename):
    try:
        with open(filename, 'r') as file:
            users = json.load(file)
        return users
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []  # Return an empty list if there's an error

# Function to write text analysis results to a file
def write_summary(filename, text_analysis):
    try:
        
        with open(filename, 'w') as file:
            for i in text_analysis:
                file.write(f"{i}\n")
        print(f"Results have been successfully saved to {filename}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    