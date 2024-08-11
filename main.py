import streamlit as st
import toml
from streamlit_option_menu import option_menu
from utils.gsheets_connect import init_google_auth
from components import sizes, brands, categories, products
from utils.config_loader import config  # Import config loader

# Load and print theme configurations from config.toml
primary_color = config['theme']['primaryColor']
font = config['theme']['font']

print(f"Primary Color: {primary_color}")
print(f"Font: {font}")

# Load secrets and initialize Google Sheets connection
secrets = toml.load('.streamlit/secrets.toml')
init_google_auth(secrets['google_sheets'])

# Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("styles/main.css")

def main():
    # Sidebar menu with custom styles
    with st.sidebar:
        choice = option_menu("F1RSTventory", ["Dashboard", "Orders", "Products", "Brands", "Categories", "Sizes", "Report", "Issues"], 
                             icons=['grid-3x3-gap', 'cart', 'box', 'tags', 'layers', 'rulers', 'check-circle', 'gear'], 
                             menu_icon="empty", default_index=0,
                             styles={
                                 "container": {"padding": "0!important", "background-color": "#18181B"},
                                 "icon": {"color": "white", "font-size": "16px"}, 
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", 
                                              "--hover-color": "#E41717", "font-family": "SFProDisplay, sans-serif"},
                                 "nav-link-selected": {"background-color": "#333333", "color": "white", "font-family": "SFProDisplay, sans-serif"},
                             })
    
    # Show the selected page
    if choice == "Sizes":
        sizes.show()
    elif choice == "Brands":
        brands.show()
    elif choice == "Categories":
        categories.show()
    elif choice == "Products":
        products.show()
    elif choice == "Dashboard":
        st.write("Dashboard content goes here")
    elif choice == "Orders":
        st.write("Orders content goes here")
    elif choice == "Report":
        st.write("Report content goes here")
    elif choice == "Issues":
        st.write("Issues content goes here")

if __name__ == "__main__":
    main()
