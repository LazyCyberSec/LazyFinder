import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import requests

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.markdown('<img style="float: left; width: 15%;" src="https://i.ibb.co/6PQVYD9/logo.png" /><h1 style="float: left;">LazySec</h1>', unsafe_allow_html=True)
name, authentication_status, username = authenticator.login('Login', 'main')

def sql():
    st.write('test')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Admin Finder')
    url = st.text_input('put url')
    if st.button('RUN'):
        urls = url + ':80'
        adminfile = 'adminfile.txt'
        with open(adminfile, 'r') as file:
            adminfile = file.read().strip().split('\n')
            results = []
            for admin_url in adminfile:
                site = url + admin_url  # Concatenate url with admin_url
                response = requests.get(site)
                if response.status_code == 200:
                    results.append(f"Vuln: {site}")
                else:
                    results.append(f"Not Vuln: {site}")
            txt = st.text_area("", "\n".join(results))

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')



    


