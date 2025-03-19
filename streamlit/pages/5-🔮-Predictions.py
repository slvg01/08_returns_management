import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
import requests
from pydantic import BaseModel
import os

#page_icon_image = Image.open('images/logo.png')
image_path = os.path.join(os.path.dirname(__file__), "..", "images", "logo.png")
page_icon_image = Image.open(image_path)

# Configure Streamlit page settings
st.set_page_config(
    layout="wide",
    page_title="RMAapp",
    page_icon=page_icon_image
)

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

# Define the Pydantic model
class Item(BaseModel):
    Shop: int
    Order_Date_FK: int
    ProductCode: int
    OriginalSaleAmountInclVAT: float
    CustomerID: int
    SaleDocumentNumber: int
    RevenueInclVAT: float
    CostPriceExclVAT: float
    BrandName: int
    ModelGroup: int
    ProductGroup: int

# Sidebar header
#st.sidebar.header("Select model")

# List of models
#models = ["High Positive Recall Model", "Balanced Model"]

# Check if the third model exists
#if os.path.exists("models/XGB_artifacts.joblib"):
#    models.append("Third Model")

# Model selection dropdown
#model_name = st.sidebar.selectbox("Model", models)

# Model selection mapping
#model_mapping = {
#    "High Positive Recall Model": "high_recall",
#    "Balanced Model": "balanced",
#    "Third Model": "third"
#}

# Add space to the UI
for _ in range(2):
    st.markdown("")

# Create columns for layout
col1, col2 = st.columns([2, 2])

# Display Page Title in the first column
col1.markdown("""
    <h1>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return Prediction tool</h1>
    <h2>Please Enter or load your sales data below</h2>
""", unsafe_allow_html=True)

# Input form for user to provide sales data
Shop = col1.number_input("Shop", value=1)
Order_Date_FK = col1.number_input("Date", value=20240125)
Product_code = col1.text_input("Product Code", value='1968361059464632550')
OriginalSaleAmountInclVAT = col1.number_input("Original Sale Amount Incl VAT", value=99.95)
CustomerID = col1.text_input("Customer ID", value='-2190786785520839526')
SaleDocumentNumber = col1.text_input("Sale Document Number", value='23995792')
RevenueInclVAT = col1.number_input("Revenue Incl VAT", value=74.96)
CostPriceExclVAT = col1.number_input("Cost Price Excl VAT", value=36.53)
BrandName = col1.text_input("Brand Name", value='3694837121284491212')
ModelGroup = col1.text_input("Model Group", value='3162564956579801398')
ProductGroup = col1.text_input("Product Group", value='-453682476182549203')

# Predict button
if st.button("Predict"):
    item = Item(
        Shop=Shop,
        Order_Date_FK=Order_Date_FK,
        ProductCode=Product_code,
        OriginalSaleAmountInclVAT=OriginalSaleAmountInclVAT,
        CustomerID=CustomerID,
        SaleDocumentNumber=SaleDocumentNumber,
        RevenueInclVAT=RevenueInclVAT,
        CostPriceExclVAT=CostPriceExclVAT,
        BrandName=BrandName,
        ModelGroup=ModelGroup,
        ProductGroup=ProductGroup
    )

    # Make a POST request to the FastAPI endpoint with selected model
    #response = requests.post(f"http://localhost:8000/predict/{model_mapping[model_name]}", json=item.dict())
    response = requests.post(f"http://localhost:8000/predict", json=item.dict())

    if response.status_code == 200:
            data = response.json()
            prediction = data["prediction"]
            risk_rate = data["risk_rate"]

            # Display the result
            st.write(f"Prediction: {prediction}")
            st.write(f"Risk rate: {risk_rate:.2%}")
    else:
            st.error("Failed to get prediction from the server.")
