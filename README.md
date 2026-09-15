# Customer Shopping Behavior Analysis

An end-to-end data analytics project analyzing customer shopping behavior using **Python, SQL, MySQL, and Power BI**. The project focuses on understanding customer spending patterns, product preferences, discount behavior, subscription status, and demographic trends.

---

## 📌 Project Overview

This project analyzes transactional customer shopping data containing **3,900 purchase records and 18 columns**.

The objective is to transform raw customer data into meaningful business insights that can help organizations understand:

- Customer spending behavior
- Revenue contribution across customer segments
- Product and category performance
- Subscription behavior
- Discount usage
- Customer demographics
- Product ratings
- Shipping preferences

The project follows an end-to-end analytics workflow:

**Data → Python Cleaning → MySQL → SQL Analysis → Power BI Dashboard → Business Insights**

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** | Data cleaning, preprocessing, and feature engineering |
| **Pandas** | Data manipulation and analysis |
| **MySQL** | Data storage and database management |
| **SQL** | Business analysis and querying |
| **Power BI** | Interactive dashboard and visualization |
| **GitHub** | Project documentation and version control |


## 📊 Power BI Dashboard

![Customer Shopping Behavior Dashboard](Screenshot%202026-09-15%20162301.png)

---

## 📂 Dataset

The dataset contains **3,900 customer purchase records** with **18 columns** covering customer demographics, purchase details, and shopping behavior.

### Key Data Categories

**Customer Demographics**
- Age
- Gender
- Location
- Subscription Status

**Purchase Details**
- Item Purchased
- Category
- Purchase Amount
- Season
- Size
- Color

**Shopping Behavior**
- Discount Applied
- Promo Code Used
- Previous Purchases
- Frequency of Purchases
- Review Rating
- Shipping Type

### Data Quality

- **Total Records:** 3,900
- **Total Columns:** 18
- **Missing Values:** 37 values in the Review Rating column

---

## 🐍 Data Cleaning & Preparation

Python and Pandas were used to clean and prepare the dataset for analysis.

### Data Preparation Steps

- Loaded the dataset using Pandas
- Inspected the dataset structure using `df.info()`
- Generated descriptive statistics using `df.describe()`
- Checked for missing values
- Handled missing `Review Rating` values using category-level median imputation
- Standardized column names to `snake_case`
- Removed unnecessary/redundant fields
- Prepared the cleaned dataset for database analysis

### Feature Engineering

Additional analytical features were created, including:

- `age_group`
- `purchase_frequency_days`

These features were used to support customer segmentation and behavioral analysis.

---

## 🗄️ SQL & MySQL Analysis

The cleaned dataset was loaded into MySQL for structured business analysis.

SQL queries were used to investigate questions such as:

- Revenue contribution by gender
- High-spending customers who used discounts
- Top 5 products by average review rating
- Purchase amount across different age groups
- Revenue by product category
- Subscriber vs. non-subscriber spending
- Customer purchasing patterns
- Product and category performance

---

## 📊 Power BI Dashboard

Power BI was used to create an interactive dashboard for analyzing customer shopping behavior.

### Dashboard Includes

- Customer demographics
- Revenue by category
- Revenue by age group
- Subscription status
- Gender analysis
- Shipping type
- Product performance
- Customer purchasing behavior

The complete interactive dashboard is available in:

**`customer.pbix`**

Open the file using **Microsoft Power BI Desktop** to explore the dashboard and interact with the visualizations.

---

## 📁 Project Structure

```text
Customer-Shopping-Behavior-Analysis/
│
├── README.md
├── customer.pbix
├── customer.sql
├── customer_shopping_behavior.csv
└── data_modelling.py
