import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_dashboard():
    st.set_page_config(page_title="IPL Strategy Dashboard", layout="wide")
    st.title("🏏 IPL Auction & Performance Insights")
    st.markdown("---")

    df = pd.read_csv('./data/processed_data.csv')

    # --- KPI CARDS ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Spending", f"₹{df['Price'].sum():,.0f}")
    col2.metric("Avg Price", f"₹{df['Price'].mean():,.2f}")
    col3.metric("Max Bid", f"₹{df['Price'].max():,.0f}")
    col4.metric("Total Players Analyzed", len(df))

    # --- CHARTS ---
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Value vs Price Quadrant")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=df, x='Price', y='runs_batter', hue='Team', ax=ax)
        plt.axhline(df['runs_batter'].mean(), color='red', linestyle='--')
        plt.axvline(df['Price'].mean(), color='red', linestyle='--')
        st.pyplot(fig)
        with st.expander("💡 Insight: Does Money Buy Wins?"):
            st.write("""
            **Analysis:** We compare how much a player cost versus how many runs they actually scored.
            - **The 'Steal' Zone (Top-Left):** Players who were cheap but performed like stars. Smart teams target these.
            - **The 'Trap' Zone (Bottom-Right):** Expensive players who underperformed. This proves that **blindly spending money does not guarantee performance.**
            """)

    with c2:
        st.subheader("Team Spending Discipline")
        fig, ax = plt.subplots(figsize=(8, 5))
        team_spend = df.groupby('Team')['Price'].sum().sort_values(ascending=False)
        sns.barplot(x=team_spend.values, y=team_spend.index, palette='viridis', ax=ax)
        st.pyplot(fig)
        with st.expander("💡 Insight: Who spends the most?"):
            st.write("""
            **Analysis:** This highlights the fiscal discipline of franchises. High spending is only justified if the team is consistently in the top-right quadrant of our previous chart. If not, management needs to reconsider their auction strategy.
            """)

    # --- ROLE ANALYSIS ---
    st.subheader("Match-Winning Impact by Player Role")
    fig, ax = plt.subplots(figsize=(10, 4))
    role_impact = df.groupby('Role')['runs_batter'].mean().sort_values(ascending=False)
    sns.barplot(x=role_impact.index, y=role_impact.values, palette='magma', ax=ax)
    st.pyplot(fig)
    with st.expander("💡 Insight: Which role is the real MVP?"):
        st.write("""
        **Analysis:** This chart calculates the average 'Runs per Player' based on their designated role. 
        - If 'All-Rounders' or 'Keepers' show higher consistency than specialized 'Batsmen', it suggests that teams should prioritize multi-skilled players to win matches. This data-backed view helps in building a more balanced squad.
        """)

if __name__ == "__main__":
    run_dashboard()