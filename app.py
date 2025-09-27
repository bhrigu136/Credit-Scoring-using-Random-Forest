import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained pipeline
pipeline = joblib.load("random_forest_credit_model.joblib")

# --- Page Setup ---
st.set_page_config(
    page_title="Credit Scoring using Random Forest",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Sidebar Application Summary ---
st.sidebar.title("📌 Application Summary")
st.sidebar.markdown("""
This app predicts **credit risk (Good / Bad)** using a **Random Forest model**  
trained on the **German Credit Data** dataset.  

- **Dataset size:** 1,000 instances  
- **Attributes:** 20 (mix of numerical + categorical)  
- **Target:** Creditworthiness (`1 = Good`, `2 = Bad`)  

👉 Enter customer attributes on the main page to get predictions.
""")

# --- Sidebar: About the App ---
st.sidebar.title("ℹ️ About the Dataset")
st.sidebar.markdown("""
The **German Credit Data** dataset is a benchmark for credit risk prediction.  
It includes **20 attributes** related to personal and financial information.  

### Attributes Overview  
1. **Status of existing checking account**  
2. **Duration of credit (months)**  
3. **Credit history**  
4. **Purpose of credit**  
5. **Credit amount**  
6. **Savings account/bonds**  
7. **Present employment since**  
8. **Installment rate in % of disposable income**  
9. **Personal status and sex**  
10. **Other debtors/guarantors**  
11. **Present residence since**  
12. **Property**  
13. **Age in years**  
14. **Other installment plans**  
15. **Housing**  
16. **Number of existing credits at this bank**  
17. **Job**  
18. **Number of people liable to provide maintenance**  
19. **Telephone**  
20. **Foreign worker**  
""")

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 Developed by **Tamanna Bhrigunath**")

# --- Header Section ---
st.title(" Credit Scoring with Random Forest")
st.markdown(
    """
    This interactive web application predicts an applicant's **creditworthiness**  
    using a machine learning model trained on the **German Credit Data**.  
    """
)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# --- Load Dataset for Inputs ---
original_data = pd.read_csv("german_credit_data.csv")
categorical_features = original_data.select_dtypes(include=['object']).columns.tolist()
numerical_features = original_data.select_dtypes(exclude=['object']).columns.tolist()

# --- Input Section ---
st.subheader("📝 Enter Applicant Details")
st.markdown("Provide the following information to assess credit risk:")

with st.expander("🔽 Fill Applicant Information", expanded=True):
    input_data = {}
    for col in original_data.columns:
        if col == "class":
            continue
        if col in categorical_features:
            options = original_data[col].unique().tolist()
            input_data[col] = st.selectbox(f"{col}", options)
        elif col in numerical_features:
            input_data[col] = st.number_input(
                f"{col}", value=float(original_data[col].mean())
            )

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# --- Prediction ---
if st.button("🚀 Predict Credit Score"):
    try:
        prediction = pipeline.predict(input_df)
        probability = pipeline.predict_proba(input_df)

        applicant_summary = {
            "Age": input_data.get("Age in years", "N/A"),
            "Credit Amount": input_data.get("Credit amount", "N/A"),
            "Duration": input_data.get("Duration in months", "N/A"),
        }

        st.markdown("### 📊 Applicant Summary")
        st.write(pd.DataFrame([applicant_summary]))

        if prediction[0] == 1:
            st.markdown(
                f"<div class='prediction-good'>✅ Good Credit Risk <br> Confidence: {probability[0][0]*100:.2f}%</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='prediction-bad'>❌ Bad Credit Risk <br> Confidence: {probability[0][1]*100:.2f}%</div>",
                unsafe_allow_html=True,
            )

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

