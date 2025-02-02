import streamlit as st
from day4_user_registration.user_management.user_handler import (
    create_directories,
    save_user_data,
    username_exists,
    validate_user,
    change_password
)
 
def main():
    # Create necessary directories for storing user data
    create_directories()
 
    # Set up the Streamlit app UI
    st.title('User Management System')
 
   
 
    # Display all options on one page
    st.header('Choose an Action')
 
    # Use radio buttons to select the action
    action = st.radio('What would you like to do?',
                      ('New Registration', 'Log in', 'Change Password'))
    
    # Function to select a role (Employee, Manager, Admin)
    def select_role():
        role = st.selectbox('Select your Role', ['Employee', 'Manager', 'Admin'])
        return role
 
    # Handle the selected action
    if action == 'New Registration':
        st.subheader('Register New Account')
        try:
            role = select_role()
            username = st.text_input('Enter username:')
            password = st.text_input('Enter password:', type='password')
            email = st.text_input('Enter your email:')
            mobile = st.text_input('Enter your mobile number:')
 
            if st.button('Register'):
                # Check if all fields are filled
                if not username or not password or not email or not mobile:
                    st.error('Please fill in all the fields')
                # Check if the username already exists
                elif username_exists(role, username, password, email, mobile):
                    st.error('Username already exists')
                else:
                    # Save the user data and show success message
                    save_user_data(role, username, password, email, mobile)
                    st.success('Registration Successful')
        except Exception as e:
            st.error(f'Error: {e}')
 
    elif action == 'Log in':
        st.subheader('Login to Account')
        try:
            role = select_role()
            username = st.text_input('Enter username:')
            password = st.text_input('Enter password:', type='password')
 
            if st.button('Login'):
                # Check if both username and password are entered
                if not username or not password:
                    st.error('Please enter both username and password')
                # Validate the user credentials
                elif validate_user(role, username, password):
                    st.success(f'Welcome, {username}!')
                else:
                    st.error('Invalid Username or Password')
        except Exception as e:
            st.error(f'Error: {e}')
 
    elif action == 'Change Password':
        st.subheader('Change Your Password')
        try:
            role = select_role()
            username = st.text_input('Enter username:')
            old_password = st.text_input('Enter old password:', type='password')
            new_password = st.text_input('Enter new password:', type='password')
 
            if st.button('Change Password'):
                # Check if all fields are filled
                if not username or not old_password or not new_password:
                    st.error('Please fill in all the fields')
                # Validate the old password
                elif validate_user(role, username, old_password):
                    # Change the password and show success message
                    change_password(role, username, new_password)
                    st.success('Password changed successfully')
                else:
                    st.error('Invalid username or password')
        except Exception as e:
            st.error(f'Error: {e}')
 
# Run the main function when the script is executed
if __name__ == '__main__':
    main()