import streamlit as st
import streamlit_authenticator as stauth

def pag_layout(username):
    login = st.Page(
        "pages/login.py",
        title="Login",
        icon=":material/person_add:",
    )
    page_dict = {}
    page_dict['Admin'] = login
        
    pg = st.navigation(login)
    pg.run()
   
if __name__ == '__main__':
    st.set_page_config(layout='wide')
    st.title('Public page')
    st.write('explanation explanation explanation explanation explanation explanation explanation explanation explanation explanation explanation explanation')
    login = st.Page(
        "pages/login.py",
        title="Login",
        icon=":material/person_add:",
    )
    pg = st.navigation(login)
    pg.run()
