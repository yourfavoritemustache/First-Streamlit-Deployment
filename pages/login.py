import streamlit as st
import streamlit_authenticator as stauth

def pag_layout(username):
    primary = st.Page(
        "pages/primary.py",
        title="Primary",
        icon=":material/person_add:",
        # default=(username != "Guest"),
    )
    secondary = st.Page(
        "pages/secondary.py",
        title="Secondary",
        icon=":material/person_add:",
    )
    third = st.Page(
        "pages/third.py",
        title="Third",
        icon=":material/person_add:",
    )
    public = st.Page(
        "pages/public.py",
        title="public",
        icon=":material/person_add:",
    )
    public = st.Page(
        "pages/public.py",
        title="public",
        icon=":material/person_add:",
    )

    private_pages = [primary,secondary,public]
    guest_pages = [third,public]
    public = [public]

    page_dict = {}
    if username == None:
        page_dict["Public"] = public
    elif username == 'guest':
        page_dict["Guest"] = guest_pages
    else:
        page_dict['Admin'] = private_pages
        
    pg = st.navigation(page_dict)
    pg.run()

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

def main():
    st.title('Login page')
    st.write('For Guest access use "guest" for username and password')

if __name__ == '__main__':
    st.set_page_config(layout='wide')
    authenticator, name, authentication_status, username = login()
    # Handle authentication status
    if authentication_status:
        pag_layout(username)
        authenticator.logout('Log out')
    elif authentication_status == False:
        st.error('Username or password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

