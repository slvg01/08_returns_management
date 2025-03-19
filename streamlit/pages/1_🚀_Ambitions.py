import streamlit as st
import os
import base64
from PIL import Image 




#page_icon_image = Image.open('images/logo.png')
image_path = os.path.join(os.path.dirname(__file__), "images", "logo.png")
page_icon_image = Image.open(image_path)

#define the page configuration
st.set_page_config(
    layout="wide",
    page_title="Ambitions",
    page_icon=page_icon_image  # Path to your local image file
)

st.title("Ambitions")



# # Open an image file
# image = Image.open('images/logo.png')
# st.image(image, caption='attempt', use_column_width=True)



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




st.markdown(
    """
   
    **1. Characteristics of a Good Model:**
    A good predictive model for returns optimization should possess the following characteristics:

    - **Accuracy:** Ability to accurately predict the likelihood of returns based on historical data and relevant features.

    - **Interpretability:** Clear interpretation of model outputs, allowing stakeholders to understand the factors driving return behavior.

    - **Scalability:** Capability to scale with increasing data volumes and complexity, ensuring robust performance in dynamic business environments.

    - **Generalization:** Ability to generalize well to unseen data, ensuring reliable predictions in real-world scenarios.

    - **Actionability:** Provision of actionable insights that enable stakeholders to implement targeted strategies for returns mitigation and optimization.


    **2. Risks and Challenges:**   

    - **Biased Data:** Biases in historical data can lead to biased model predictions, resulting in inaccurate or unfair outcomes.

    - **Overfitting:** Overfit models may perform well on training data but generalize poorly to new data, leading to suboptimal decisions.

    - **Model Interpretability:** Complex models may lack interpretability, making it challenging to understand the underlying factors driving predictions.


    **3. Performance Monitoring:**
    Performance monitoring of predictive models involves:

    - **Metrics Tracking:** Monitor key performance metrics, such as accuracy, precision, recall, and F1-score, to assess model performance over time.

    - **Feedback Loop:** Incorporate feedback from stakeholders and end-users to identify model drift, concept drift, or shifts in business requirements.

    - **Model Refresh:** Regularly retrain and update models using new data to ensure continued relevance and accuracy.


    """
)
