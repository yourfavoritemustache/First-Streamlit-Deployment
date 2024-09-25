import streamlit as st
import streamlit_authenticator as stauth

def hash_passwords(passwords):
    ## Function to hash passwords
    return stauth.Hasher(passwords).generate()

def login():
    # User credentials
    names = ['Astengoli', 'Guest']
    usernames = st.secrets['usernames']
    passwords = st.secrets['passwords']
    
    # Hash passwords
    hashed_passwords = hash_passwords(passwords)

    # Create credentials dictionary
    credentials = {
        'usernames': {
            usernames[0]: {'name': names[0], 'password': hashed_passwords[0]},
            usernames[1]: {'name': names[1], 'password': hashed_passwords[1]}
        }
    }
    # Create authenticator object
    authenticator = stauth.Authenticate(
        credentials=credentials,
        cookie_name='expenses_dashboard',
        cookie_key = 'yourfavoritesignaturek3y',
        cookie_expiry_days=1
    )
    # Implement login widget
    name, authentication_status, username = authenticator.login('main', 'Login')
    
    return authenticator, name, authentication_status, username

def access_type(username):
    if username != 'guest':
        main()
    else:
        guest_page()

def main():
    st.title('Main Page')
    st.write(st.secrets['passwords'])
    type(st.secrets['passwords'])

def guest_page():
    st.title('Gues Page')
    st.write(st.secrets['passwords'])
    st.secrets['passwords']

if __name__ == '__main__':
    st.set_page_config(layout='wide',initial_sidebar_state='expanded')
    authenticator, name, authentication_status, username = login()
    access_level = username
    # Handle authentication status
    if authentication_status:
        access_type(username)
        authenticator.logout('Log out')
    elif authentication_status == False:
        st.error('Username or password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')