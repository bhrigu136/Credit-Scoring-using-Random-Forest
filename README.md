# 🌟 Credit Scoring with Random Forest  

This project is an **end-to-end machine learning application** that predicts an individual's **creditworthiness** using a **Random Forest classifier** trained on the **German Credit Data** dataset. It classifies applicants as a **"good"** or **"bad"** credit risk.

The project features:
- A model training script  
- A user-friendly Streamlit web application  
- A complete deployment pipeline  

---

## 🚀 Live Application  
👉 [Credit Scoring with Random Forest — Live App](https://credit-scoring-using-random-forest-y4swxuubrbctwhjx6jxwte.streamlit.app/)

---

## 🎯 Project Overview  
This project demonstrates a **complete end-to-end machine learning workflow**, including:

1. **Data Analysis** – Exploring a dataset with both numerical and categorical attributes  
2. **Model Building** – Using a **Pipeline** for preprocessing and training a robust Random Forest model  
3. **Deployment** – Serving the model in real time through a **Streamlit-based web application**

The app allows users to provide **20 key borrower attributes** and receive a **real-time risk prediction**.

---

## 💻 Technologies Used  
- **Python** – Core language for scripting and modeling  
- **Scikit-learn** – Model building (`RandomForestClassifier`), preprocessing, and `Pipeline`  
- **Streamlit** – Front-end for building the interactive web application  
- **Pandas** – Data handling and exploration  
- **Joblib** – Managing model persistence (save/load)

---

## 📊 Dataset: German Credit Data  
The model is built on the **German Credit Data** (1,000 instances, 20 features).

**Target variable:**  
- `1` → Good credit risk  
- `2` → Bad credit risk

### Features  
1. Status of existing checking account  
2. Duration of credit (months)  
3. Credit history  
4. Purpose of credit  
5. Credit amount  
6. Savings account/bonds  
7. Present employment since  
8. Installment rate  
9. Personal status and sex  
10. Other debtors/guarantors  
11. Present residence since  
12. Property  
13. Age (years)  
14. Other installment plans  
15. Housing  
16. Number of existing credits at this bank  
17. Job  
18. Number of people liable for maintenance  
19. Telephone  
20. Foreign worker

---

## ⚡ How to Run the Project Locally  

### Step 1: Clone the repository  
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### Step 2: Install Dependencies  
Create a `requirements.txt` with the following:
```
streamlit==1.36.0
scikit-learn==1.5.0
pandas==2.2.2
joblib==1.4.2
```
Install them:
```bash
pip install -r requirements.txt
```

### Step 3: Train and Save the Model  
```bash
python train_model.py
```
This creates `random_forest_credit_model.joblib`.

### Step 4: Launch the Streamlit App  
```bash
streamlit run app.py
```
A local server will spin up, and the app should open automatically in your browser.

---

## 📂 File Structure  
```
├── app.py                                   # Streamlit web application  
├── german_credit_data.csv                   # Dataset file  
├── RF_credit_scoring.ipynb                  # Notebook for EDA & modeling  
├── random_forest_credit_model.joblib        # Serialized model/pipeline  
├── requirements.txt                         # Project dependencies  
├── train_model.py                           # Model training script  
└── README.md                                # Project documentation  
```

---

## 📌 Future Enhancements  
- Integrate **hyperparameter tuning** (GridSearchCV, RandomizedSearchCV)  
- Benchmark against other models (XGBoost, Logistic Regression)  
- Enrich UI with visualizations such as feature importances and interactive charts  

---

## 🤝 Contributions  
Contributions welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License  
Licensed under the **MIT License**

---
