import streamlit as st
import subprocess
import pandas as pd
import numpy as np
import os
import base64
from PIL import Image 


#page_icon_image = Image.open('images/logo.png')
image_path = os.path.join(os.path.dirname(__file__), "..", "images", "logo.png")
page_icon_image = Image.open(image_path)

#define the page configuration
st.set_page_config(
    layout="wide",
    page_title="Exploratory Data Analysis",
    page_icon=page_icon_image  # Path to your local image file
)

st.title("Exploratory Data Analysis")

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



st.markdown("""
<style>
.title {
    font-size:30px !important;
    color: #000000; 
    font-weight: bold; 
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.text-box {
    background-color: rgba(255, 255, 255, 0.9); 
    border-radius: 10px;  
    padding: 10px;  
    margin: 10px 0;  
    font-size:16px !important;
    color: #000000; 
}
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio('Analysis Stream', ['data key figures', 'Shop', 'Product', 'Brand', 'Price','Clients'])
if page == 'data key figures':

    st.markdown('<div class="title">&nbsp&nbsp DATA KEY FIGURES </div>', unsafe_allow_html=True)
    st.text('') # blank line
    st.markdown("""
    
    <div class="text-box">
        <ul>
            <li>Data are comprised of 12 numerical data (but 9 of them are in fact categorical which was taken into account for the preprocessing)</li>
            <li>1.75M lines covering a 2 month period</li>
            <li>No null values</li>
            <li>Out of that, duplicates represent a bit less than 50% of the total lines</li>
            <li>Further duplicate analysis shows that it is difficult to exclude them without knowing more about the company logging process. There is a possibility that those duplicates (same shoes, same day, same shop bought several times) are real sales (especially online):
                <ul>
                    <li>Numerous customers</li>
                    <li>Double size buying</li>
                </ul>
            </li>
        </ul>
    </div>
                
""", unsafe_allow_html=True)

    st.text('')
    
    #Print the first 5 rows of the dataframe
    st.text('base data:')
    df = pd.read_csv('../EDA/df.csv')
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].astype(str)

    st.dataframe(df.head(5))
    
    st.text('')

    # Create two columns
    col1, col2 = st.columns(2)

    # Run the first script and capture the output
    result1 = subprocess.run(['python', '../EDA/0_Base1.py'], stdout=subprocess.PIPE)
    output1 = result1.stdout.decode('utf-8')

    # Display the output in the first column
    col1.text(output1)

    # Run the second script and capture the output
    result2 = subprocess.run(['python', '../EDA/0_Base2.py'], stdout=subprocess.PIPE)
    output2 = result2.stdout.decode('utf-8')

    # Display the output in the second column
    for _ in range(7):
        col2.text("")
    col2.text(output2)
    
    




if page == 'Shop':

    st.markdown('<div class="title">SHOP </div>', unsafe_allow_html=True)
    st.text('')  # blank line
    st.text('')  # blank line
    st.text('')  # blank line
    st.markdown("""
<div class="text-box">
    <p><b>The 2 online businesses:</b></p>
    <ul>
        <li>Represent 10% of total sales but 40% of the return.</li>
        <li>Indeed, the return rate is around 19% vs 4% average.</li>
        <li>Moreover, their discount rate is higher by 7 points and thus their profitability.</li>
    </ul>
    <p>This needs a deeper analysis to set up a strategy that may correct those imbalanced elements both for return rate and profitability.</p>
</div>
""", unsafe_allow_html=True)
    st.text('')