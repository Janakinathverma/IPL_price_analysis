# 🏏 IPL Auction & Performance Analytics

**IPL Auction & Performance Analytics** is a data-driven project that explores the relationship between team spending in IPL auctions and actual player performance on the field. It helps in identifying whether high-budget squads guarantee tournament wins or if "Smart Scouting" (Efficiency) is the true key to success.



## 🚀 Features

- **Automated Data Processing:** Clean and merge disparate auction and performance datasets.
- **Value vs. Price Analysis:** Identify "Steal Deals" (High impact, low cost) vs "Overpaid Traps" (Low impact, high cost).
- **Interactive Dashboard:** Built with Streamlit for intuitive exploration.
- **Role-Based Impact:** Analyze match-winning consistency across different player roles (Batsmen, Bowlers, All-rounders).
- **Spending Discipline Insights:** Visualizing franchise spending patterns.

## 🛠 Tech Stack

Dillinger uses a number of open-source projects to work properly:

- [Python 3] - The core language.
- [Pandas] - For powerful data manipulation and cleaning.
- [Streamlit] - For building the interactive dashboard.
- [Matplotlib] & [Seaborn] - For data visualization.
- [Kaggle Datasets] - Source of raw IPL data.

## 📂 Project Structure

```text
├── data/
│   ├── IPLPlayerAuctionData.csv  # Auction metadata
│   ├── IPL.csv                  # Ball-by-ball performance data
│   └── processed_data.csv       # Merged & cleaned analysis file
├── dashboard.py                 # Streamlit UI
├── processor.py                 # Data cleaning & feature engineering
├── main.py                      # Project orchestrator
└── .gitignore                   # Ignores heavy data/ and venv files
🛠 Installation
Dillinger requires Python 3 to run.

Install the necessary dependencies:

Bash
pip install pandas streamlit matplotlib seaborn
🚀 Usage
To get the dashboard running, follow these two steps:

1. Process the raw data:

Bash
python3 processor.py
2. Launch the dashboard:

Bash
streamlit run dashboard.py
💡 Key Findings
Higher spending does not guarantee tournament wins.

Smart Scouting (finding players with high "Runs-per-Crore" efficiency) is often the differentiator between top-tier and bottom-tier teams.

Role Impact: Multi-skilled players (All-rounders) often show higher consistency in delivering match-winning impacts compared to specialized players.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

License
MIT

Free Software, Hell Yeah!