import pandas as pd
import sqlite3

# Load the dataset
file_path = '/content/WA_Fn-UseC_-Telco-Customer-Churn.csv'
df = pd.read_csv(file_path)

# Connect to SQLite (or create it)
conn = sqlite3.connect('telco_customer_churn.db')

# Write the data to a SQLite table
df.to_sql('telco_churn', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

# Reconnect to SQLite
conn = sqlite3.connect('telco_customer_churn.db')

# 1. Count total customers
total_customers_query = "SELECT COUNT(*) AS total_customers FROM telco_churn;"
total_customers = pd.read_sql(total_customers_query, conn)
print(total_customers)

# 2. Count churned vs non-churned customers
churn_count_query = """
SELECT Churn, COUNT(*) AS count
FROM telco_churn
GROUP BY Churn;
"""
churn_count = pd.read_sql(churn_count_query, conn)
print(churn_count)

# 3. Average tenure of churned vs non-churned customers
avg_tenure_query = """
SELECT Churn, AVG(tenure) AS average_tenure
FROM telco_churn
GROUP BY Churn;
"""
avg_tenure = pd.read_sql(avg_tenure_query, conn)
print(avg_tenure)

# 4. Percentage of customers with different payment methods
payment_method_query = """
SELECT PaymentMethod, COUNT(*) AS count
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY count DESC;
"""
payment_methods = pd.read_sql(payment_method_query, conn)
print(payment_methods)

# 5. Distribution of monthly charges
monthly_charge_query = """
SELECT ROUND(MonthlyCharges, 2) AS charge_range, COUNT(*) AS count
FROM telco_churn
GROUP BY charge_range
ORDER BY charge_range;
"""
monthly_charges_distribution = pd.read_sql(monthly_charge_query, conn)
print(monthly_charges_distribution)

# Close the connection
conn.close()
