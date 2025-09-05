Credit Scoring with Random ForestThis project is an end-to-end machine learning application that predicts an individual's creditworthiness. It uses a Random Forest classifier trained on the German Credit Data to classify applicants as a "good" or "bad" credit risk. The project includes a model training script, a user-friendly web application built with Streamlit, and a deployment pipeline.🚀 Live ApplicationYou can test the deployed application here:Credit Scoring with Random Forest - Live App🎯 Project OverviewThe goal of this project is to demonstrate a complete machine learning workflow:Data Analysis: Understanding a dataset with a mix of numerical and categorical features.Model Building: Creating a robust machine learning model using a Pipeline for consistent preprocessing.Deployment: Packaging the model and serving it through an interactive web application on Streamlit Cloud.The application allows a user to input 20 different attributes about a potential borrower and receive a real-time prediction on their credit risk.💻 Technologies UsedPython: The core programming language for the entire project.Scikit-learn: For building the machine learning model (RandomForestClassifier), preprocessing (OneHotEncoder, ColumnTransformer), and managing the workflow (Pipeline).Streamlit: For creating the interactive web application.Pandas: For data manipulation and analysis.Joblib: For saving and loading the trained machine learning model.📊 The Data: German Credit DataThe project uses the well-known German Credit Data dataset, a classic benchmark for credit risk prediction. The dataset contains 1,000 instances and 20 attributes.The model's goal is to predict the class variable, where 1 indicates a good credit risk and 2 indicates a bad credit risk.Here's what each attribute represents:Attribute1: Status of existing checking accountAttribute2: Duration of the credit in monthsAttribute3: Credit historyAttribute4: Purpose of the creditAttribute5: Credit amountAttribute6: Savings account/bondsAttribute7: Present employment sinceAttribute8: Installment rateAttribute9: Personal status and sexAttribute10: Other debtors / guarantorsAttribute11: Present residence sinceAttribute12: PropertyAttribute13: Age in yearsAttribute14: Other installment plansAttribute15: HousingAttribute16: Number of existing credits at this bankAttribute17: JobAttribute18: Number of people liable to provide maintenance forAttribute19: TelephoneAttribute20: Foreign worker🚀 How to Run the Project LocallyFollow these steps to set up and run the application on your local machine:Step 1: Clone the Repositorygit clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

Note: Remember to replace your-username/your-repository-name.git with your actual GitHub repository URL.Step 2: Install DependenciesCreate a requirements.txt file in your project folder with the following content. These are the pinned versions to ensure the app runs correctly.streamlit==1.36.0
scikit-learn==1.5.0
pandas==2.2.2
joblib==1.4.2

Then, install the dependencies:pip install -r requirements.txt

Step 3: Train and Save the ModelFirst, you need to train the model and save the pipeline to a file. This is a crucial step before running the app.python train_model.py

This will create a file named random_forest_credit_model.joblib.Step 4: Run the Streamlit ApplicationWith the model saved, you can now launch the web application.streamlit run app.py

This command will start a local web server and open the application in your browser.📁 File Structure.
├── app.py                       # The Streamlit web application.
├── german_credit_data.csv       # The dataset used for training.
├── RF_credit_scoring.ipynb      # Jupyter Notebook for exploratory analysis and model building.
├── random_forest_credit_model.joblib # The saved, trained model pipeline.
├── requirements.txt             # List of project dependencies for deployment.
├── train_model.py               # Script to train and save the model pipeline.
└── README.md                    # This file.

