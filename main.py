import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from category_encoders import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.responses import HTMLResponse
from sklearn.model_selection import train_test_split



# Create the FastAPI app
app = FastAPI()

# Load model and artifacts once during startup
artifacts = joblib.load("models/XGB_artifacts.joblib")
onehot_columns = artifacts["features"]["onehot_features"]
target_columns = artifacts["features"]["target_features"]
encoder_target = artifacts["encoder_target"]
encoder_onehot = artifacts["encoder_onehot"]
scaler = artifacts["scaler"]
model = artifacts["model"]



# welcome and check page 
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; background-color: darkblue; color: white; flex-direction: column;">
            <h2>Welcome to Returns Predictions API</h2>
            <button onclick="location.href='http://127.0.0.1:8000/docs#/default/predict_predict_post'" type="button" style="margin: 10px; padding: 10px;">Enter the Rabbit Hole</button>        
        </body>
    </html>
    """

# Define a model for request body
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


# Preprocessing of the data
def preprocess_data(df):

    # # delete the return column
    # df = df.drop('Returned', axis=1)

    # create a discount rate and a profit columns
    df['discount_rate_%'] = 100*(df['OriginalSaleAmountInclVAT']-df['RevenueInclVAT']) / df['OriginalSaleAmountInclVAT']
    df['profit_%'] = 100*(df['RevenueInclVAT']-df['CostPriceExclVAT']) / df['OriginalSaleAmountInclVAT']

    # create a day of the week column
    df['Order_Date_FK'] = pd.to_datetime(df['Order_Date_FK'], format='%Y%m%d')
    df['day_of_week'] = df['Order_Date_FK'].dt.day_name()

    # add the number of item in the transaction and the identical number of item  of tx
    df['nb_item_tx'] = df.groupby('SaleDocumentNumber')['ProductCode'].transform('count')
    df['nb_similar_item_tx'] = df.groupby(['SaleDocumentNumber', 'ProductCode'])['ProductCode'].transform('count')

    # onehot and target encode + ensuring no nan value are present in case some category data were not present in train data + scaling
    df = encoder_onehot.transform(df)
    df = encoder_target.transform(df) 
    target_mean = 0.037
    df.fillna(target_mean, inplace=True)
    df = scaler.transform(df)
    return df




# predict function
@app.post("/predict")
def predict(item: Item):
    try:
        # # Convert input data to data frame
        # data = pd.DataFrame([dict(item)])

        # Define a dictionary with default values for all features
        default_values = {
            'Shop': 0,
            'Order_Date_FK': 0,
            'ProductCode': 0,
            'OriginalSaleAmountInclVAT': 0.0,
            'CustomerID': 0,
            'SaleDocumentNumber': 0,
            'RevenueInclVAT': 0.0,
            'CostPriceExclVAT': 0.0,
            'BrandName': 0,
            'ModelGroup': 0,
            'ProductGroup': 0
        }

        # Update the default values with the values from the input item
        input_values = {**default_values, **dict(item)}

        # Convert the updated values to a DataFrame
        data = pd.DataFrame([input_values])
        
        

        # Preprocess the data
        pre_processed_data = preprocess_data(data)

        # Make prediction
        prediction = model.predict(pre_processed_data)

        # Return prediction
        if prediction[0] == 0 :
           return {"prediction": "Risk of return are limited, sleep well boss" }
        else :
           return {"prediction": "Risk of return are high, action may be needed" }
    
    except Exception as e:
        return {"error": str(e)}
