import streamlit as st

st.set_page_config(
    layout='wide',
    initial_sidebar_state = 'collapsed',
    page_title='Personal Finance Dashboard',
    page_icon='money_bag',
)

# Define all pages
p1 = st.Page(
    'Pages/primary.py',
    title = 'Primary',
    icon=':material/currency_exchange'
)
p2 = st.Page(
    'Pages/secondary.py',
    title = 'secondary',
    icon=':material/account_balance',
)
p3 = st.Page(
    'Pages/third.py',
    title = 'third',
)

# Install multipages
pg = st.navigation(pages=[p1,p2,p3])
pg.run()

st.title('Default page')