import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from category_encoders import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib



# Load the data
df = pd.read_parquet('data/data_clean6.parquet')

# Define the features and target
X = df.drop('Returned', axis=1)
y = df['Returned']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
print(X_train.shape)

# onehot encode
categorical_feature_onehot = ['day_of_week']
encoder_onehot = OneHotEncoder(cols=categorical_feature_onehot, handle_unknown='return_nan', handle_missing='return_nan')
X_train_encoded_hot = encoder_onehot.fit_transform(X_train, y_train)
X_test_encoded_hot = encoder_onehot.transform(X_test)
print(X_train_encoded_hot.shape)
# Target encode
categorical_feature_target = ['Shop','CustomerID','ProductCode',  'BrandName',  'ModelGroup', 'ProductGroup', 'SaleDocumentNumber', 'Order_Date_FK']
encoder_target = TargetEncoder(cols=categorical_feature_target, handle_unknown='mean', handle_missing='mean')
X_train_encoded = encoder_target.fit_transform(X_train_encoded_hot, y_train)
X_test_encoded = encoder_target.transform(X_test_encoded_hot)
print(X_train_encoded.shape)

# Ensuring that no nan value are present in case some catagory data were not present in train data
target_mean = y_train.mean()
X_test_encoded = X_test_encoded.fillna(target_mean)  


# Normalize the data
sc = StandardScaler()
X_train_normalized = sc.fit_transform(X_train_encoded)  # fit on train and transform train 
X_test_normalized = sc.transform(X_test_encoded) # transform test with the same scaler based on train 
print(X_train_normalized.shape)

# Instantiate the model
xgb = XGBClassifier()

# Fit the model
param = {'gamma': 2, 'learning_rate': 0.01, 'max_depth': 12, 'n_estimators': 500, 'subsample': 0.85, 'scale_pos_weight':18} 
xgb = XGBClassifier(**param)
xgb.fit(X_train_normalized, y_train)



# Save the model
artifacts = {
        "features": {
            "onehot_features": categorical_feature_onehot,
            "target_features": categorical_feature_target,
        },
        "encoder_onehot": encoder_onehot,
        "encoder_target": encoder_target,
        "scaler": sc,
        "model": xgb,
    }
joblib.dump(artifacts, "models/XGB_artifacts.joblib")




