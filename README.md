# Churn-Prediction-for-Customers
This project aims to analyze customer churn data from a telecommunications company to uncover factors influencing customer churn and explore patterns using SQL queries, Python, and data visualization techniques.

Dataset Overview
The dataset contains information about telecommunications customers, their usage patterns, subscription details, and whether they have churned (left the service). Below are the key columns:

customerID: Unique customer ID
gender: Customer's gender
SeniorCitizen: Whether the customer is a senior citizen (1 or 0)
tenure: Number of months the customer has stayed with the company
Contract: Contract type (Month-to-month, One year, Two year)
PaymentMethod: Customer’s payment method
MonthlyCharges: Monthly bill
TotalCharges: Total amount charged to the customer
Churn: Whether the customer has churned (Yes or No)
Project Workflow
1. Data Preprocessing
Handling missing values
Converting categorical data into numerical representations for analysis
Removing irrelevant columns (e.g., customerID)
Feature scaling and encoding for machine learning
2. SQL Analysis
Data loaded into SQLite for advanced querying
Key insights are drawn by running SQL queries on the dataset
3. Visualizations
Multiple visualizations are generated to support the SQL-based analysis, such as:
Churn distribution
Monthly Charges distribution
Contract types vs. Churn
Key SQL Queries for Analysis
1. Count Total Customers
sql
Copy code
SELECT COUNT(*) AS total_customers FROM telco_churn;
2. Churn Count
sql
Copy code
SELECT Churn, COUNT(*) AS churn_count
FROM telco_churn
GROUP BY Churn;
3. Average Tenure by Churn
sql
Copy code
SELECT Churn, AVG(tenure) AS avg_tenure
FROM telco_churn
GROUP BY Churn;
4. Customers by Payment Method
sql
Copy code
SELECT PaymentMethod, COUNT(*) AS count
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY count DESC;
Setup Instructions
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
SQLite 3.x (comes pre-installed with Python)
Required Python libraries:
pandas
matplotlib
seaborn
sqlite3 (built-in with Python)
Steps to Run the Project Locally
1. Clone the repository:
bash
Copy code
git clone https://github.com/your-username/telco-customer-churn-analysis.git
cd telco-customer-churn-analysis
2. Install the required Python libraries:
bash
Copy code
pip install pandas matplotlib seaborn
3. Load the dataset into a SQLite database:
bash
Copy code
# Python script to load data into SQLite
import pandas as pd
import sqlite3

# Load the dataset
file_path = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

# Connect to SQLite
conn = sqlite3.connect('telco_customer_churn.db')

# Write the data to a SQL table
df.to_sql('telco_churn', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
4. Run SQL Queries:
You can run the SQL queries provided above within SQLite or using Python to fetch insights from the dataset.

Visualizations
This project also includes visualizations to provide better insights into churn behavior and customer attributes.

Churn Distribution Visualization (Python example):
python
Copy code
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Churn', data=df)
plt.title('Churn Distribution')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()
Insights
Churn Rate: The churn rate in the dataset is around X%.
Tenure Impact: Customers with shorter tenures are more likely to churn, particularly those on Month-to-month contracts.
Payment Method Correlation: Customers using Electronic check are more likely to churn compared to those using Bank transfer or Credit card.
Conclusion
This project successfully demonstrates how SQL and Python can be leveraged to analyze customer churn, identify key factors influencing churn, and visualize the results for better decision-making.


Average Tenure: Customers who churn have an average tenure of X months, compared to Y months for those who stay.
Payment Method: The most common payment method is Electronic check, followed by Mailed check and Bank transfer.
Monthly Charges: Monthly charges are skewed, with a significant number of customers falling in certain charge ranges.
Conclusion
This project provides insights into customer churn patterns by leveraging SQL queries and visualizations. It helps identify key factors contributing to customer churn, which can be useful for customer retention strategies.
