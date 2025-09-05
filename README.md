# 🌟 Credit Scoring with Random Forest  

This project is an **end-to-end machine learning application** that predicts an individual's **creditworthiness**.  
It uses a **Random Forest classifier** trained on the **German Credit Data** to classify applicants as a **"good"** or **"bad"** credit risk.  

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
- **Scikit-learn** – RandomForestClassifier, OneHotEncoder, ColumnTransformer, and Pipelines  
- **Streamlit** – For the interactive web application  
- **Pandas** – Data manipulation and analysis  
- **Joblib** – Saving and loading the trained model  

---

## 📊 The Data: German Credit Data  

The project uses the **German Credit Data** dataset, a classic benchmark for credit risk prediction.  
- **Instances:** 1,000  
- **Attributes:** 20  

**Target Variable:**  
- `1` → Good credit risk  
- `2` → Bad credit risk  

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

## 📂 File Structure  

```
├── app.py                           # Streamlit web application  
├── german_credit_data.csv           # Training dataset  
├── RF_credit_scoring.ipynb          # Exploratory analysis and model building  
├── random_forest_credit_model.joblib # Saved model pipeline  
├── requirements.txt                 # Project dependencies  
├── train_model.py                   # Script to train and save the model pipeline  
└── README.md                        # Project documentation  
```

---

## 📌 Future Improvements  
- Experiment with **hyperparameter tuning**  
- Compare with other ML models (XGBoost, Logistic Regression, etc.)  
- Enhance UI with **charts and feature importance visuals**  

---

## 🤝 Contributing  
Contributions are welcome! Please fork the repo and submit a pull request.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---
