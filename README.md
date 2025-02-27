# Stock Price Tracker Web Application

## 📌 Overview
The **Stock Price Tracker** is a web application designed to visualize stock market data using historical stock prices stored in a **CSV file**. It allows users to select a stock index and view detailed market information through interactive tables and charts.

This project does **not** fetch real-time data from any stock exchange. Instead, it processes and displays historical data from a pre-loaded CSV file.

## ⚙️ How It Works

### **1. Backend (Flask API)**
- The backend is built using **Flask** and serves stock data from a CSV file.
- When a user selects a stock index, the backend filters the relevant data and returns it as a JSON response.
- Data preprocessing ensures missing values are handled properly.

### **2. Frontend (HTML, Bootstrap, Chart.js)**
- Users can select a stock index from a dropdown menu.
- Stock details are displayed in a **dynamic table**.
- A **Chart.js line graph** visualizes stock trends.
- Data is fetched asynchronously using **AJAX (jQuery)** to update the table and chart without reloading the page.

## 🔧 Features
✅ **Stock Selection** – Choose different stock indices to view details.  
✅ **Interactive Table** – Displays market data like opening price, closing price, volume, and performance metrics.  
✅ **Chart Visualization** – Line chart shows stock price trends.  
✅ **CSV-Based Data** – Uses historical data instead of real-time stock prices.  
✅ **Responsive UI** – Designed with **Bootstrap** for a clean and mobile-friendly experience.  

## 🚀 Installation & Setup
### **Prerequisites**
- Python 3.x
- Flask
- Pandas
- jQuery, Bootstrap, Chart.js (for frontend)

### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/stock-price-tracker.git
cd stock-price-tracker
```

### **2. Install Dependencies**
```sh
cd server
pip install flask pandas
```

### **3. Run the Application**
```sh
python app.py
```

### **4. Access the Web App**  
Go to:  
👉 **Open `index.html` in your browser**

## 🛠 Future Improvements
- ✅ Add **search functionality** for stock indices.
- ✅ Improve **data preprocessing** to handle missing values better.
- ✅ Implement **sorting/filtering** in the stock data table.
- ✅ Optimize **chart updates** for better performance.
- ⏳ Add real-time stock data integration (Future Scope).

## 🏆 Contributing
If you have ideas for improving this project, feel free to submit a pull request! Contributions are always welcome. 😊

## 📜 License
This project is licensed under the **MIT License**.

---


