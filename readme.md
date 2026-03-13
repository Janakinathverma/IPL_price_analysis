
# 🏏 IPL Auction & Performance Analytics
---

**IPL Auction & Performance Analytics** is a data-driven project that explores the relationship between **team spending in IPL auctions** and **actual player performance on the field**.

The goal is to analyze whether **high-budget squads guarantee tournament success** or if **smart scouting and efficient spending** are the real differentiators.

---

# 🚀 Features

* **Automated Data Processing**
  Clean and merge auction data with player performance datasets.

* **Value vs Price Analysis**
  Identify:

  * 💎 **Steal Deals** – High impact players with low cost
  * ⚠️ **Overpaid Traps** – Expensive players with low impact

* **Interactive Dashboard**
  Built using **Streamlit** for intuitive data exploration.

* **Role-Based Performance Analysis**
  Compare impact across:

  * Batsmen
  * Bowlers
  * All-rounders

* **Spending Discipline Insights**
  Visualize franchise spending patterns and efficiency.

---

# 🛠 Tech Stack

| Tool            | Purpose                        |
| --------------- | ------------------------------ |
| Python          | Core programming language      |
| Pandas          | Data cleaning and manipulation |
| Streamlit       | Interactive dashboard          |
| Matplotlib      | Data visualization             |
| Seaborn         | Statistical visualizations     |
| Kaggle Datasets | IPL raw datasets               |

---

# 📂 Project Structure

```text
IPL-Auction-Analytics
│
├── data/
│   ├── IPLPlayerAuctionData.csv     # Auction metadata
│   ├── IPL.csv                     # Ball-by-ball match data
│   └── processed_data.csv          # Cleaned merged dataset
│
├── dashboard.py                    # Streamlit dashboard
├── processor.py                    # Data cleaning & feature engineering
├── main.py                         # Project orchestrator
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ipl-auction-analytics.git
cd ipl-auction-analytics
```

Install dependencies:

```bash
pip install pandas streamlit matplotlib seaborn
```

---

# 🚀 Usage

### 1️⃣ Process Raw Data

```bash
python3 processor.py
```

This will generate the cleaned dataset.

---

### 2️⃣ Launch Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

---

# 📊 Key Insights

📌 **Higher spending does NOT guarantee tournament success.**

📌 Teams that focus on **player efficiency metrics (Runs-per-Crore, Wickets-per-Crore)** often perform better.

📌 **All-rounders** frequently deliver **higher match impact consistency** compared to specialized roles.

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Submit a pull request

For major changes, please open an issue first.

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider **starring the repository**.

---
