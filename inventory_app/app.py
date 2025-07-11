import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Ensure data directory exists
DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

# Load data with fallback to empty DataFrame
def load_data(name, columns):
    path = os.path.join(DATA_PATH, f"{name}.csv")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return pd.DataFrame(columns=columns)
    return pd.read_csv(path)

# Save data to CSV
def save_data(name, df):
    path = os.path.join(DATA_PATH, f"{name}.csv")
    df.to_csv(path, index=False)

# UI settings
st.set_page_config(page_title="Inventory App", layout="wide")
st.title("📦 Inventory & Sales Management App")

# Sidebar menu
menu = st.sidebar.selectbox("Choose Module", ["Customer", "Products", "Sales", "Expenses", "Profit Report"])

# --- Customer Registration ---
if menu == "Customer":
    st.header("🧑 Customer Registration")
    customers = load_data("customers", ["CustId", "CustName", "Address", "ContactNo", "EmailId", "OpeningBalance", "RegistrationDate", "Category"])

    with st.form("cust_form"):
        cid = st.number_input("Customer ID", min_value=1)
        name = st.text_input("Name")
        addr = st.text_input("Address")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        bal = st.number_input("Opening Balance", min_value=0.0)
        cat = st.selectbox("Category", ["Regular", "Premium"])
        reg_date = st.date_input("Registration Date")

        if st.form_submit_button("Submit"):
            new_row = pd.DataFrame([{
                "CustId": cid,
                "CustName": name,
                "Address": addr,
                "ContactNo": phone,
                "EmailId": email,
                "OpeningBalance": bal,
                "RegistrationDate": reg_date,
                "Category": cat
            }])
            customers = pd.concat([customers, new_row], ignore_index=True)
            save_data("customers", customers)
            st.success("✅ Customer Added!")

# --- Product Management ---
elif menu == "Products":
    st.header("🧾 Product Management")
    products = load_data("products", ["ProdId", "ProdName", "Description", "Rate", "CreationDate"])

    with st.form("prod_form"):
        pid = st.number_input("Product ID", min_value=1)
        pname = st.text_input("Product Name")
        desc = st.text_input("Description")
        rate = st.number_input("Rate", min_value=0.0)
        cdate = st.date_input("Creation Date")

        if st.form_submit_button("Add Product"):
            new_row = pd.DataFrame([{
                "ProdId": pid,
                "ProdName": pname,
                "Description": desc,
                "Rate": rate,
                "CreationDate": cdate
            }])
            products = pd.concat([products, new_row], ignore_index=True)
            save_data("products", products)
            st.success("✅ Product Added!")

# --- Sales Entry ---
elif menu == "Sales":
    st.header("💰 Sales Entry")
    sales = load_data("sales", ["SalesInvoiceNo", "CustId", "CustName", "ProdId", "ProdName", "Description", "Rate", "GSTPercentage", "GSTAmount", "FinalAmount", "DateOfInvoice"])
    customers = load_data("customers", ["CustId", "CustName"])
    products = load_data("products", ["ProdId", "ProdName", "Description", "Rate"])

    with st.form("sales_form"):
        inv = st.number_input("Invoice No", min_value=1)
        cid = st.selectbox("Customer ID", customers["CustId"]) if not customers.empty else 0
        cname = customers[customers["CustId"] == cid]["CustName"].values[0] if cid in customers["CustId"].values else ""
        pid = st.selectbox("Product ID", products["ProdId"]) if not products.empty else 0
        prod = products[products["ProdId"] == pid].iloc[0] if pid in products["ProdId"].values else None
        inv_date = st.date_input("Invoice Date")

        if st.form_submit_button("Submit Sale") and prod is not None:
            gst = 18
            gst_amt = prod["Rate"] * gst / 100
            total = prod["Rate"] + gst_amt

            new_row = pd.DataFrame([{
                "SalesInvoiceNo": inv,
                "CustId": cid,
                "CustName": cname,
                "ProdId": pid,
                "ProdName": prod["ProdName"],
                "Description": prod["Description"],
                "Rate": prod["Rate"],
                "GSTPercentage": gst,
                "GSTAmount": gst_amt,
                "FinalAmount": total,
                "DateOfInvoice": inv_date
            }])
            sales = pd.concat([sales, new_row], ignore_index=True)
            save_data("sales", sales)
            st.success("✅ Sale Recorded!")

# --- Expense Entry ---
elif menu == "Expenses":
    st.header("📉 Expense Entry")
    expenses = load_data("expenses", ["ExpenseNo", "ExpenseType", "ExpenseAmount", "DateOfExpense", "ExpenseFor"])

    with st.form("exp_form"):
        eno = st.number_input("Expense No", min_value=1)
        etype = st.text_input("Type")
        amount = st.number_input("Amount", min_value=0.0)
        date = st.date_input("Date")
        purpose = st.text_input("Expense For")

        if st.form_submit_button("Add Expense"):
            new_row = pd.DataFrame([{
                "ExpenseNo": eno,
                "ExpenseType": etype,
                "ExpenseAmount": amount,
                "DateOfExpense": date,
                "ExpenseFor": purpose
            }])
            expenses = pd.concat([expenses, new_row], ignore_index=True)
            save_data("expenses", expenses)
            st.success("✅ Expense Added!")

# --- Profit & Loss Report ---
elif menu == "Profit Report":
    st.header("📈 Profit & Loss Report")
    sales = load_data("sales", ["FinalAmount"])
    expenses = load_data("expenses", ["ExpenseAmount"])

    total_sales = sales["FinalAmount"].sum()
    total_exp = expenses["ExpenseAmount"].sum()
    profit = total_sales - total_exp

    st.metric("Total Sales", f"₹ {total_sales}")
    st.metric("Total Expenses", f"₹ {total_exp}")
    st.metric("Profit", f"₹ {profit}")
