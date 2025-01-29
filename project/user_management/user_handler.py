def add_user(users, username, age):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    
    for user in users:
        if user['username'] == username:
            raise ValueError("Username already exists.")
    
    users.append({'username': username, 'age': age})


def remove_user(users, username):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    
    for i, user in enumerate(users):
        #enumerate() function in Python adds a counter to an iterable and returns it as an enumerate object.
        if user['username'] == username:
            users.pop(i)
            return
    raise ValueError("User does not exist.")


def get_user_info(users, username):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    
    for user in users:
        if user['username'] == username:
            return user
    raise ValueError("User does not exist.")


def update_user_age(users, username, new_age):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    if not isinstance(new_age, int):
        raise ValueError("New age must be an integer.")
    if new_age < 0:
        raise ValueError("Age cannot be negative.")
    
    for user in users:
        if user['username'] == username:
            user['age'] = new_age
            return
    raise ValueError("User does not exist.")
