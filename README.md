# 🌟 Credit Scoring with Random Forest  

This project is an **end-to-end machine learning application** that predicts an individual's **creditworthiness**.  
It uses a **Random Forest classifier** trained on the **German Credit Data** to classify applicants as a **"good"** or **"bad"** credit risk. 
It allows users to input personal and financial attributes, and then predicts whether the credit risk is **Good** or **Bad**. 

The project includes:  
- A model training script  
- A user-friendly web application built with **Streamlit**  
- A deployment pipeline  

---

## 🚀 Live Application  
👉 [Credit Scoring with Random Forest — Live App](https://credit-scoring-using-random-forest-y4swxuubrbctwhjx6jxwte.streamlit.app/)  

---

## 🎯 Project Overview  

The goal of this project is to demonstrate a **complete machine learning workflow**:  

1. **Data Analysis** – Understanding a dataset with a mix of numerical and categorical features  
2. **Model Building** – Creating a robust machine learning model using a **Pipeline** for consistent preprocessing  
3. **Deployment** – Packaging the model and serving it through an interactive web application on Streamlit Cloud  

💡 The application allows users to input **20 different attributes** about a potential borrower and receive a **real-time prediction** of their credit risk.  

---

## 💻 Technologies Used  

- **Python** – Core programming language  
- **Scikit-learn** – For building the machine learning model (RandomForestClassifier), preprocessing (OneHotEncoder, ColumnTransformer), and managing the workflow (Pipeline).  
- **Streamlit** – For the interactive web application  
- **Pandas** – Data manipulation and analysis  
- **Joblib** – Saving and loading the trained model  

---

## 📊 The Data: German Credit Data  

The project uses the **German Credit Data** dataset, a classic benchmark for credit risk prediction.  
- **Instances:** 1,000  
- **Attributes:** 20  

**Target Variable**: `class`
- `1` → Good credit risk  
- `2` → Bad credit risk  

The dataset includes **categorical** and **numerical features**

### Attributes Overview  
- Attribute1: Status of existing checking account  
- Attribute2: Duration of the credit in months  
- Attribute3: Credit history  
- Attribute4: Purpose of the credit  
- Attribute5: Credit amount  
- Attribute6: Savings account/bonds  
- Attribute7: Present employment since  
- Attribute8: Installment rate  
- Attribute9: Personal status and sex  
- Attribute10: Other debtors / guarantors  
- Attribute11: Present residence since  
- Attribute12: Property  
- Attribute13: Age in years  
- Attribute14: Other installment plans  
- Attribute15: Housing  
- Attribute16: Number of existing credits at this bank  
- Attribute17: Job  
- Attribute18: Number of people liable to provide maintenance for  
- Attribute19: Telephone  
- Attribute20: Foreign worker  

---

## ⚙️ Model Development

### 1. Preprocessing
- Handled **categorical** and **numerical** features separately using a `ColumnTransformer`.  
- Applied **OneHotEncoding** for categorical variables.  
- Numerical variables were passed as-is.  

### 2. Model Training
- Used **Random Forest Classifier** (`sklearn.ensemble.RandomForestClassifier`) with default parameters and `random_state=42`.  
- Created a **Pipeline** that combines preprocessing + model training.  
- Trained on the German Credit dataset.  

### 3. Model Saving
- Saved the trained pipeline using **joblib** → `random_forest_credit_model.joblib`.  

---

## 💻 Streamlit App (app.py)

The **Streamlit interface** allows users to:  
- Input features dynamically (based on dataset columns).  
- Select categorical values from dropdowns.  
- Enter numerical values via number inputs.  
- Click **Predict Credit Score** to classify as:  
  - ✅ **Good Credit Risk**  
  - ❌ **Bad Credit Risk**  

Error handling is included for safe predictions.

---

## ⚡ How to Run the Project Locally  

### Step 1: Clone the Repository  
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```
> Replace `your-username/your-repository-name` with your actual GitHub repository URL.  

### Step 2: Install Dependencies  
Create a `requirements.txt` file with the following content:  
```
streamlit==1.36.0
scikit-learn==1.5.0
pandas==2.2.2
joblib==1.4.2
```
Then install dependencies:  
```bash
pip install -r requirements.txt
```

### Step 3: Train and Save the Model  
```bash
python train_model.py
```
This will generate:  
```
random_forest_credit_model.joblib
```

### Step 4: Run the Streamlit Application  
```bash
streamlit run app.py
```

This will start a local server and open the application in your browser.  

---

## 📂 Project Structure  

```
├── app.py                           # Streamlit frontend for user application  
├── german_credit_data.csv           # Training dataset  
├── RF_credit_scoring.ipynb          # Exploratory analysis and model building  
├── random_forest_credit_model.joblib # Saved model pipeline  
├── requirements.txt                 # Project dependencies  
├── train_model.py                   # Script to train and save the model pipeline  
└── README.md                        # Project documentation  
```

---

## 📈 Results & Insights

- Random Forest achieved strong performance on the dataset.  
- The pipeline ensures **seamless integration of preprocessing + classification**.  
- The model is suitable for evaluating **credit risk** and can be extended for real-world applications.

---

## 📚 References

- German Credit Dataset  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  

---

## 📌 Future Improvements  
- Experiment with **hyperparameter tuning**  
- Compare with other ML models (XGBoost, Logistic Regression, etc.)  
- Enhance UI with **charts and feature importance visuals**  
- Feature importance visualization in the Streamlit app. 

---

👩‍💻 Developed by Tamanna Bhrigunath  
