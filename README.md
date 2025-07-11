
# 📦 Inventory & Sales Management App (Streamlit)

This is a full-featured web application built with **Streamlit** to manage customers, products, GST-based sales, expenses, and generate profit reports — all in one lightweight, interactive interface.

Whether you're running a small business, handling freelance sales, or learning how data apps work, this project is a great example of how to integrate Python, Streamlit, and Pandas into a complete solution.

---

## 🚀 Features

### 🧑 Customer Management
- Register new customers
- Store contact details and categories (Regular / Premium)
- Track opening balance and registration date

### 🧾 Product Management
- Add new products with descriptions and pricing
- Automatically track creation date

### 💰 Sales Module
- Select customer and product for each sale
- Auto-fill product info
- Automatically calculate **18% GST** and final amount
- Save each sale with invoice number and date

### 📉 Expenses Module
- Record daily/weekly/monthly business expenses
- Add purpose and date for each entry

### 📈 Profit Report
- Total Sales, Total Expenses, and Profit shown live
- Clean and real-time financial summary

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – for UI
- **Pandas** – for data handling and CSV storage
- **CSV files** – used as backend database (simple and portable)

---

## 📂 Project Structure

```
inventory_app/
├── app.py
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── sales.csv
│   └── expenses.csv
└── requirements.txt
```

---

## ▶️ How to Run

1. **Clone the repo**:
```bash
git clone https://github.com/rajwardhan-patil/inventory-app-streamlit.git
cd inventory-app-streamlit
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the app**:
```bash
streamlit run app.py
```

---

## 📹 Demo

> *(https://www.linkedin.com/posts/rajwardhan-patil08_python-streamlit-webapp-activity-7349418222581870594-oFjU?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFRojOEBxwsZgAgjLAnYIb1xlIPdRJqffkQ)*

---

## 💡 Future Ideas

- Add login/authentication system
- Convert to SQLite or PostgreSQL backend
- Downloadable invoice PDFs
- Dashboard charts with Plotly or Altair
- Streamlit Cloud Deployment

---

## 🤝 Contribution

Feel free to fork the repo and submit a PR. Suggestions and improvements are always welcome!

---

## 📬 Contact

Made with ❤️ by Rajwardhan Patil

Connect on LinkedIn www.linkedin.com/in/rajwardhan-patil08
