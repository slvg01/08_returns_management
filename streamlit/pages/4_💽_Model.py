import streamlit as st
import os
import base64
from PIL import Image 


#page_icon_image = Image.open('images/logo.png')
image_path = os.path.join(os.path.dirname(__file__), "..", "images", "logo.png")
page_icon_image = Image.open(image_path)

#define the page configuration
st.set_page_config(
    layout="wide",
    page_title="Predictive Models Characteristics",
    page_icon=page_icon_image  # Path to your local image file
)


st.title("Predictive Models Characteristics")

# Function to get the image in base64 for background
def add_bg_from_url(url):
    st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("{url}");
             background-size: cover;
         }}
         </style>
         """, unsafe_allow_html=True)

# Image URL for background
image_url = 'https://static.vecteezy.com/system/resources/previews/041/385/052/non_2x/ai-generated-a-cardboard-box-placed-on-a-white-background-free-photo.jpg'
add_bg_from_url(image_url)