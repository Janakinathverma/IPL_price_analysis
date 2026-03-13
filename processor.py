import pandas as pd

def process_ipl_data():
    print("Data processing starts...")
    
    auction_df = pd.read_csv('./data/IPLPlayerAuctionData.csv', low_memory=False)
    ipl_df = pd.read_csv('./data/IPL.csv', low_memory=False)

    # 1. Performance Aggregate
    player_perf = ipl_df.groupby(['batter', 'year'])['runs_batter'].sum().reset_index()
    player_perf.rename(columns={'batter': 'Player', 'year': 'Year'}, inplace=True)

    # 2. Merge
    merged_df = pd.merge(auction_df, player_perf, on=['Player', 'Year'], how='inner')

    # 3. Clean & Rename 'Amount' to 'Price' (Ye zaroori hai!)
    if 'Amount' in merged_df.columns:
        # Amount clean karo
        merged_df['Amount'] = merged_df['Amount'].replace(r'[\$,]', '', regex=True)
        # Convert to numeric
        merged_df['Amount'] = pd.to_numeric(merged_df['Amount'])
        # Rename to 'Price'
        merged_df.rename(columns={'Amount': 'Price'}, inplace=True)
        
        # 4. Calculate Efficiency
        merged_df['Efficiency'] = merged_df['runs_batter'] / merged_df['Price']
    else:
        print("Error: 'Amount' column nahi mila!")

    merged_df.to_csv('./data/processed_data.csv', index=False)
    print("Success! Processed data saved with 'Price' column.")

if __name__ == "__main__":
    process_ipl_data()