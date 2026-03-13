
import processor
import dashboard
import os

def main():
    # 1. Engine: Process Data if not already done
    if not os.path.exists('./data/processed_data.csv'):
        processor.process_ipl_data()
    else:
        print("Processed data found. Ready to launch.")

    # 2. Face: Launch Dashboard
    # Note: Streamlit usually runs via CLI, but for a controller:
    print("To view dashboard, run: streamlit run main.py")
    dashboard.run_dashboard()

if __name__ == "__main__":
    main()