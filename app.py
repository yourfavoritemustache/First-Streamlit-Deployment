import streamlit as st
import streamlit_authenticator as stauth

def pag_layout(username,authentication_status):
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

    private_pages = [primary,secondary,public]
    guest_pages = [third,public]
    public_pages = [public]

    page_dict = {}
    if authentication_status:
        if username == None:
            page_dict["Public"] = public_pages
        elif username == 'guest':
            page_dict["Guest"] = guest_pages
        else:
            page_dict['Private'] = private_pages
    else:
        page_dict["Public"] = public_pages
        
    pg = st.navigation(page_dict)
    pg.run()
    
def login_page_layout():
    public = st.Page(
        "pages/public.py",
        title="public",
        icon=":material/person_add:",
    )
    page_dict = {'Public':public}
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
    name, authentication_status, username = authenticator.login('sidebar',fields={'Form name':'Log in: use "guest" for guest access'})
    
    return authenticator, name, authentication_status, username

if __name__ == '__main__':
    st.set_page_config(layout='wide')
    authenticator, name, authentication_status, username = login()
    # Handle authentication status
    if authentication_status == None:
        pag_layout(username,authentication_status)
    elif authentication_status == False:
        pag_layout(username,authentication_status)
        st.error('Username or password is incorrect')
    else:
        pag_layout(username,authentication_status)
        authenticator.logout('Log out','sidebar')
