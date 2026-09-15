import pandas as pd
df=pd.read_csv('customer_shopping_behavior.csv')
print(df.head())

df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)

print("\nMissing values after filling Review Rating:")
print(df.isnull().sum())




df.columns = df.columns.str.lower()

df.columns = df.columns.str.replace(' ', '_')

df = df.rename(columns={
    'purchase_amount_(usd)': 'purchase_amount'
})

print("\nColumn names:")
print(df.columns)



labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']

df['age_group'] = pd.qcut(
    df['age'],
    q=4,
    labels=labels
)

print("\nAge and Age Group:")
print(df[['age', 'age_group']].head(10))





frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(
    frequency_mapping
)

print("\nPurchase Frequency:")
print(
    df[
        ['purchase_frequency_days', 'frequency_of_purchases']
    ].head(10)
)



print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nFinal Missing Values:")
print(df.isnull().sum())


print("\nDiscount Applied and Promo Code Used:")
print(df[['discount_applied', 'promo_code_used']].head(10))



same_values = (df['discount_applied'] == df['promo_code_used']).all()

print("\nAre discount_applied and promo_code_used identical?")
print(same_values)




df = df.drop('promo_code_used', axis=1)



print("\nFinal column names:")
print(df.columns)



# ==========================================
# CONNECT PYTHON TO MYSQL
# ==========================================
import os
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
     password=os.getenv("MYSQL_PASSWORD"),
    database="customer_shopping"
)

if connection.is_connected():
    print("MySQL connected successfully!")

connection.close()



from sqlalchemy import create_engine

# ==========================================
# LOAD CLEANED DATA INTO MYSQL
# ==========================================

from sqlalchemy.engine import URL

# Create MySQL connection safely
# Create MySQL connection safely
connection_url = URL.create(
    drivername="mysql+mysqlconnector",
    username="root",
    password=os.getenv("MYSQL_PASSWORD"),
    host="localhost",
    port=3306,
    database="customer_shopping"
)

engine = create_engine(connection_url)

# Load DataFrame into MySQL
df.to_sql(
    name="customer_shopping_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into MySQL!")

engine.dispose()