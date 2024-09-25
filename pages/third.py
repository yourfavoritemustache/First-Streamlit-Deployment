import streamlit as st

if (st.session_state.authentication_status == None) or (st.session_state.authentication_status == False):
    st.switch_page("app.py")
else:
    st.title('Third Page')
    st.write('For Guest!!!!!')
