
# 📊 Customer Churn Prediction Using Machine Learning

A machine learning project that predicts customer churn using customer demographics, billing information, contract details, and payment methods. This project implements an end-to-end data science workflow, including data preprocessing, feature engineering, exploratory data analysis, model training, evaluation, and model persistence.

---

## 📌 Project Overview

Customer churn occurs when customers stop using a company's products or services. Predicting churn enables businesses to identify customers who may leave and develop customer retention strategies.

In this project, three machine learning classification algorithms are implemented:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The models are trained and evaluated using a customer churn dataset containing 500 records.

---

## 🎯 Project Objectives

- Analyze customer information and churn patterns.
- Clean and preprocess the dataset.
- Encode categorical features.
- Perform feature engineering.
- Analyze feature relationships using EDA.
- Train multiple classification models.
- Evaluate models using classification metrics.
- Visualize confusion matrices and ROC curves.
- Save trained models using Joblib.
- Create a reusable customer churn prediction function.

---

## 📂 Dataset Information

**Dataset Name:** `churn_data.csv`

| Property | Details |
|---|---|
| Total Records | 500 |
| Original Features | 8 input columns + target |
| Final Model Features | 20 |
| Missing Values | None |
| Problem Type | Binary Classification |
| Target Variable | `Churn` |

### Dataset Features

| Feature | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Tenure | Duration of the customer relationship |
| MonthlyCharges | Monthly customer charges |
| TotalCharges | Total customer charges |
| Contract | Customer contract type |
| PaymentMethod | Customer payment method |
| PaperlessBilling | Paperless billing status |
| SeniorCitizen | Senior citizen indicator |
| Churn | Target variable |

### Target Encoding

| Value | Meaning |
|---|---|
| 0 | Not Churned |
| 1 | Churned |

### Target Distribution

| Category | Count |
|---|---:|
| Not Churned | 447 |
| Churned | 53 |

**Dataset churn rate:** 10.6%

> Note: The dataset is imbalanced, so balanced class weights were used during model training.

---

## 🛠️ Technologies and Libraries

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computing
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Scikit-learn** – Machine learning and evaluation
- **Joblib** – Model saving and loading
- **Jupyter Notebook** – Development environment

---

## 🔄 Project Workflow

```text
Data Collection
      ↓
Data Loading
      ↓
Data Exploration
      ↓
Data Preprocessing
      ↓
Categorical Encoding
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving
      ↓
Reusable Prediction Function
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Checked data types and dataset structure.
3. Checked for missing values.
4. Encoded categorical variables using One-Hot Encoding.
5. Removed the `CustomerID` identifier from the modeling features.
6. Separated the input features and target variable.
7. Converted Boolean columns into integer values where required.
8. Aligned model features with the saved feature-column structure.

No missing values were found in the dataset.

---

## ⚙️ Feature Engineering

The following features were created to improve the analysis:

### 1. Average Monthly Spend

```python
AverageMonthlySpend = TotalCharges / Tenure
```

Estimates the average amount spent by a customer per month.

### 2. Estimated Annual Charges

```python
EstimatedAnnualCharges = MonthlyCharges * 12
```

Estimates the customer's annual charges.

This feature was excluded from the final model because it was perfectly correlated with `MonthlyCharges`.

### 3. Tenure Group

Customers were grouped into the following categories:

- New Customer
- Short Term
- Medium Term
- Long Term

### 4. Long-Term Contract Indicator

Indicates whether the customer has a one-year or two-year contract.

### 5. Electronic Check Indicator

Indicates whether the customer uses Electronic Check as their payment method.

### 6. Paperless Billing Indicator

Indicates whether paperless billing is enabled.

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Churn distribution analysis
- Numerical feature analysis
- Correlation analysis
- Tenure group analysis
- Feature importance analysis

### Key Observations

- The dataset contains 53 churned customers and 447 non-churned customers.
- Tenure showed an approximate negative correlation with churn.
- Average monthly spend showed an approximate positive correlation with churn.
- Long-term contract indicators showed an approximate negative relationship with churn.
- Tenure and tenure-group features were among the most important features in the Random Forest analysis.

> Important: These observations are specific to this dataset and should not automatically be generalized to other customer populations.

---

## 🤖 Machine Learning Models

Three classification algorithms were trained.

### 1. Logistic Regression

Logistic Regression was used as a baseline classification model.

```python
LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    solver="lbfgs",
    random_state=42
)
```

### 2. Decision Tree Classifier

A Decision Tree was trained with a maximum depth of 5.

```python
DecisionTreeClassifier(
    max_depth=5,
    class_weight="balanced",
    random_state=42
)
```

### 3. Random Forest Classifier

A Random Forest model with 200 estimators was trained.

```python
RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)
```

---

## 📈 Model Performance

The dataset was split into training and testing sets using an 80:20 ratio.

| Dataset | Records |
|---|---:|
| Training Set | 400 |
| Testing Set | 100 |

### Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Decision Tree | 94% | 72.7% | 72.7% | 72.7% | 0.856 |
| Random Forest | 97% | 78.6% | 100% | 88% | 0.997 |
| Logistic Regression | 97% | 78.6% | 100% | 88% | 0.998 |

> The reported metrics were obtained from a single stratified train-test split using `random_state=42`. Further validation is required to assess generalization.

### Evaluation Metrics

| Metric | Description |
|---|---|
| Accuracy | Percentage of correct predictions |
| Precision | Accuracy of positive churn predictions |
| Recall | Percentage of actual churn cases identified |
| F1-Score | Balance between precision and recall |
| ROC-AUC | Ability to distinguish between the two classes |

---

## 🔍 Confusion Matrix

The Logistic Regression confusion matrix on the test dataset was:

| | Predicted Not Churned | Predicted Churned |
|---|---:|---:|
| Actual Not Churned | 86 | 3 |
| Actual Churned | 0 | 11 |

### Results

- True Negatives: 86
- False Positives: 3
- False Negatives: 0
- True Positives: 11

The model identified all 11 actual churn cases in this test set and incorrectly classified 3 non-churned customers as churned.

---

## 📉 ROC Curve

ROC curves were generated for all three models to compare their classification performance across different probability thresholds.

### ROC-AUC Results

- Decision Tree: 0.856
- Random Forest: 0.997
- Logistic Regression: 0.998

The ROC-AUC results are based on the selected test split and should be validated using cross-validation and an independent dataset before practical deployment.

---

## 💾 Model Saving

The trained models and preprocessing objects were saved using Joblib.

### Saved Files

```text
saved_models/
├── decision_tree.pkl
├── feature_columns.pkl
├── logistic_regression.pkl
├── random_forest.pkl
└── scaler.pkl
```

### Example

```python
import joblib

joblib.dump(
    logistic_model,
    "saved_models/logistic_regression.pkl"
)

joblib.dump(
    random_forest,
    "saved_models/random_forest.pkl"
)

joblib.dump(
    decision_tree,
    "saved_models/decision_tree.pkl"
)

joblib.dump(
    scaler,
    "saved_models/scaler.pkl"
)

joblib.dump(
    X.columns.tolist(),
    "saved_models/feature_columns.pkl"
)
```

---

## 🔁 Reusable Prediction Function

A reusable function was created to predict customer churn using customer information.

### Input Parameters

- Tenure
- Monthly charges
- Total charges
- Contract type
- Payment method
- Paperless billing
- Senior citizen status

### Example Input

```python
predict_customer_churn(
    tenure=6,
    monthly_charges=85,
    total_charges=510,
    contract="Month-to-month",
    payment_method="Electronic Check",
    paperless_billing="Yes",
    senior_citizen=0
)
```

### Example Output

| Model | Prediction |
|---|---|
| Logistic Regression | Churn |
| Decision Tree | Churn |
| Random Forest | Churn |

The function performs feature engineering, encoding, feature alignment, scaling, and prediction using the saved models.

---

## 📁 Project Structure

```text
Week10-Customer-Churn-Prediction/
│
├── churn_data.csv
├── customer_churn_prediction.ipynb
├── saved_models/
│   ├── decision_tree.pkl
│   ├── feature_columns.pkl
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── scaler.pkl
│
└── README.md
```

> Replace `customer_churn_prediction.ipynb` with the exact filename of your notebook if it is different.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd Week10-Customer-Churn-Prediction
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

### Step 6: Launch Jupyter Notebook

```bash
jupyter notebook
```

### Step 7: Open the Notebook

Open the project notebook and run the cells in sequence.

---

## ⚠️ Project Limitations

- The dataset contains only 500 records.
- Model evaluation uses a single train-test split.
- The target variable is imbalanced.
- Some engineered features overlap with existing features.
- The churn distribution may be specific to this dataset.
- Test-set performance may not generalize to new datasets.
- Extensive hyperparameter tuning was not performed.

---

## 🚀 Future Improvements

- Use a larger and more representative dataset.
- Implement stratified cross-validation.
- Perform hyperparameter tuning.
- Remove redundant features.
- Test additional classification algorithms.
- Analyze precision-recall curves.
- Optimize prediction thresholds based on business needs.
- Develop an interactive Streamlit dashboard.
- Deploy the model as a web application.
- Monitor model performance after deployment.

---

## 🎓 Skills Demonstrated

- Python Programming
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Categorical Encoding
- Feature Scaling
- Binary Classification
- Logistic Regression
- Decision Tree
- Random Forest
- Model Evaluation
- Confusion Matrix Analysis
- ROC-AUC Analysis
- Joblib Model Persistence
- Reusable Prediction Functions
- Jupyter Notebook
- Machine Learning Workflow

---

## 🏁 Conclusion

This project demonstrates the development of a complete customer churn prediction workflow using machine learning.

The project includes data exploration, preprocessing, feature engineering, model training, performance evaluation, confusion matrix analysis, ROC curve visualization, and model persistence using Joblib.

Logistic Regression and Random Forest achieved 97% accuracy and 100% recall on the selected test split. A reusable prediction function was also created to generate predictions using customer details.

The project provides practical experience in building and evaluating classification models. Additional validation, feature selection, and deployment work would be required before using the model in a real-world business environment.

---

## 👨‍💻 Author

**Viren Wankhade**

Aspiring Data Analyst | Data Science Enthusiast
- GitHub: https://github.com/viren689
- Portfolio: https://viren-portfolio-gamma.vercel.app/
- Email: viren19271@gmail.com

