import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

# Load the image for the page icon
page_icon_image = Image.open('images/logo.png')

# Configure Streamlit page settings
st.set_page_config(
    layout="wide",
    page_title="RMAapp",
    page_icon=page_icon_image
)

# # Hide default Streamlit format for cleaner UI
# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)


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

# image URL
image_url = 'https://static.vecteezy.com/system/resources/previews/041/385/052/non_2x/ai-generated-a-cardboard-box-placed-on-a-white-background-free-photo.jpg'
add_bg_from_url(image_url)

for _ in range (2):
    st.markdown("")

# Create two columns
col1, col2 = st.columns([15, 2])

# Display the output in the first column
col1.markdown("""

<h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp Welcome to RmApp</h1>
              
# 💥Blasting Your Return Rate!💥
""", unsafe_allow_html=True)

for _ in range(4):
    col1.markdown("""
    """)

col1.markdown("""
<div class="text-box">
    <b>This app will allow you to navigate across key features of our return management system:</b>
    <ul>
        <li>Ambitions</li>
        <li>EDA on your data</li>
        <li>Data Preprocessing</li>
        <li>Selected Model and optimization tracking through MLFlow</li>
        <li>Predicting your return rate</li>
        <li>Adjusting the model according to your preference</li>
        <li>Strategic recommendations to optimize your return rate</li>
    </ul>
</div>
""", unsafe_allow_html=True)




# Define options for navigation
#navigation_options = ['Welcome', 'Use case', 'EDA', 'Balanced Model', 'Positive Recall Model', 'Energy', 'Predict!']

# Button to initiate contributing
start_contributing_button = st.button("Get started!")
if start_contributing_button:
    switch_page("Ambitions")