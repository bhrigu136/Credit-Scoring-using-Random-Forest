import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Load the raw data
data = pd.read_csv("german_credit_data.csv")

# Separate features (X) and target (y)
# The notebook shows that 'class' is the target variable
X = data.drop("class", axis=1)
y = data["class"]

# Identify categorical and numerical columns from the original data
categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=np.number).columns

# Create the preprocessor using ColumnTransformer
# It will apply OneHotEncoder to categorical columns and leave numerical columns as is.
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

# Create the full pipeline
# This pipeline includes both the data preprocessing and the classifier
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Fit the pipeline on the full dataset
pipeline.fit(X, y)

# Save the entire trained pipeline to a file
joblib.dump(pipeline, 'random_forest_credit_model.joblib')

print("Model pipeline trained and saved successfully!")