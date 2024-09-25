import streamlit as st


if 'authentication_status' not in st.session_state:
    st.switch_page("app.py")
else:
    st.title('Main Page')
    st.write('Private page bitch')
    
