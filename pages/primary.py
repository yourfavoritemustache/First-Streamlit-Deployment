import streamlit as st


if st.session_state.authentication_status==False:
    st.switch_page("app.py")
else:
    st.title('Main Page')
    st.write('Private page bitch')
    
