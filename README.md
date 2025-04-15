# 🏦 Loan Approval Prediction Model
This project is a **machine learning web application** that predicts whether a loan application should be approved based on user inputs such as income, credit history, loan amount and other financial parameters. 
The model uses **Logistic Regression** for classification and has been deployed to a live web domain.

## 🚀 Live Demo

👉 👉 [Check out the live app here](https://loan-approval-prediction-xu7o.onrender.com/predict)  (Will take time to load)

---

## 📊 Features

- Predicts loan approval status based on applicant details
- Built using Logistic Regression (Scikit-learn)
- Hyperparameter Tuning using GridSearchCV
- Clean and simple user interface
- Deployed and accessible on the web

---

## 🔧 Tech Stack

- **Python**
- **Scikit-learn** (Logistic Regression)
- **Pandas**, **NumPy**
- **Flask** 
- **HTML/CSS**
- **Deployed on**: Render

---

## 🧠 Machine Learning Model

The model is trained on a dataset of loan applicants with the following key features:

- Age
- Gender
- Applicant Annual Income
- Loan amount requested
- Length of credit history (in years)
- Credit Score
- Previous loan defaults

The target variable is the **Loan Status** (Approved / Not Approved).

Model Used:
- **Logistic Regression**
- Accuracy: ~`88.5%`
- Evaluation Metrics: Accuracy, Confusion Matrix, Classification_Report 

---

## 📁 Project Structure

```bash
├── models/             
│   └── grid.pkl           # Trained Logistic Regression model with best parameters
│   └── scaler.pkl         # StandardScaler used for input normalization
├── notebooks/
│   └── loan_approval.ipynb   # Jupyter notebook for data analysis & model training
│   └── loan_data.csv         # Dataset used for model training
├── templates/
│   └── index.html         # Home page
│   └── form.html          # Input form page
├── appliaction.py         # Flask backend for the web app 
├── requirements.txt       # Python dependencies
└── README.md              # Project overview
