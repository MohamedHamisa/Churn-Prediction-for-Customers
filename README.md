# Churn-Prediction-for-Customers
This project analyzes customer churn data from a fictional telecommunications company. The goal is to understand patterns of customer churn, including what factors might influence it and how different customer segments are impacted.

Dataset
The dataset used in this project is the Telco Customer Churn dataset. It contains the following columns:

customerID: Unique ID for each customer
gender: Gender of the customer
SeniorCitizen: Indicates if the customer is a senior citizen (1 or 0)
Partner: Indicates if the customer has a partner (Yes or No)
Dependents: Indicates if the customer has dependents (Yes or No)
tenure: Number of months the customer has stayed with the company
PhoneService: Indicates if the customer has phone service (Yes or No)
MultipleLines: Indicates if the customer has multiple lines (Yes, No, No phone service)
InternetService: Type of internet service (DSL, Fiber optic, No)
OnlineSecurity: Indicates if the customer has online security (Yes, No, No internet service)
OnlineBackup: Indicates if the customer has online backup (Yes, No, No internet service)
DeviceProtection: Indicates if the customer has device protection (Yes, No, No internet service)
TechSupport: Indicates if the customer has tech support (Yes, No, No internet service)
StreamingTV: Indicates if the customer has streaming TV service (Yes, No, No internet service)
StreamingMovies: Indicates if the customer has streaming movie service (Yes, No, No internet service)
Contract: Contract type (Month-to-month, One year, Two year)
PaperlessBilling: Indicates if the customer uses paperless billing (Yes or No)
PaymentMethod: Payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
MonthlyCharges: The amount charged to the customer monthly
TotalCharges: The total amount charged to the customer
Churn: Indicates if the customer has churned (Yes or No)
Project Workflow
Loading Data: The dataset is first loaded into a Pandas DataFrame and preprocessed, including handling missing values, encoding categorical variables, and correcting data types.

SQL Integration: After data preprocessing, the dataset is uploaded into a SQLite database to perform SQL-based data analysis.

SQL Queries: Key insights are extracted from the dataset using SQL queries, and these results are analyzed to draw meaningful conclusions.

SQL Analysis
1. Count Total Customers
sql
Copy code
SELECT COUNT(*) AS total_customers FROM telco_churn;
This query returns the total number of customers in the dataset.

2. Churn Count
sql
Copy code
SELECT Churn, COUNT(*) AS count
FROM telco_churn
GROUP BY Churn;
This query counts how many customers have churned (Yes) vs. those who have not (No).

3. Average Tenure by Churn
sql
Copy code
SELECT Churn, AVG(tenure) AS average_tenure
FROM telco_churn
GROUP BY Churn;
This query calculates the average tenure of customers who churned and those who didn’t.

4. Distribution by Payment Method
sql
Copy code
SELECT PaymentMethod, COUNT(*) AS count
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY count DESC;
This query returns the distribution of customers across different payment methods.

5. Monthly Charges Distribution
sql
Copy code
SELECT ROUND(MonthlyCharges, 2) AS charge_range, COUNT(*) AS count
FROM telco_churn
GROUP BY charge_range
ORDER BY charge_range;
This query groups monthly charges into ranges to understand customer distribution by charge amounts.

Setup Instructions
To run this project on your local machine, follow these steps:

Prerequisites
Python 3.x
SQLite 3.x (included with Python)
Required Python libraries:
pandas
matplotlib
seaborn
sqlite3 (Python's standard library)
Steps to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/telco-customer-churn-analysis.git
cd telco-customer-churn-analysis
Install the required libraries:

bash
Copy code
pip install pandas matplotlib seaborn
Load the dataset into SQLite using the script:

python
Copy code
import pandas as pd
import sqlite3

# Load the dataset
file_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

# Connect to SQLite (or create it)
conn = sqlite3.connect('telco_customer_churn.db')

# Write the data to a SQLite table
df.to_sql('telco_churn', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
Run the SQL queries provided in the SQL Analysis section to explore the data and extract insights.

(Optional) Visualize the results using matplotlib and seaborn:

python
Copy code
import seaborn as sns
import matplotlib.pyplot as plt

# Example: Visualize churn count
sns.barplot(x='Churn', y='count', data=churn_count)
plt.title('Churn Count')
plt.xlabel('Churn Status (1=Yes, 0=No)')
plt.ylabel('Count')
plt.show()
Insights
Churn Distribution: Understanding the ratio of churned vs. non-churned customers.
Average Tenure: Customers who churn have an average tenure of X months, compared to Y months for those who stay.
Payment Method: The most common payment method is Electronic check, followed by Mailed check and Bank transfer.
Monthly Charges: Monthly charges are skewed, with a significant number of customers falling in certain charge ranges.
Conclusion
This project provides insights into customer churn patterns by leveraging SQL queries and visualizations. It helps identify key factors contributing to customer churn, which can be useful for customer retention strategies.
