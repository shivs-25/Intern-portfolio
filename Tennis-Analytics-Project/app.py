import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# 1. Page Configuration
# --------------------------
st.set_page_config(
    page_title="Tennis Insights Dashboard",
    layout="wide"
)

st.title("Tennis Insights Dashboard")
st.markdown("Interactive analytics powered by SportRadar tennis data.")

DB_PATH = "tennis_analysis.db"

# --------------------------
# 2. Load Data from Database
# --------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    competitions = pd.read_sql("SELECT * FROM competitions", conn)
    categories = pd.read_sql("SELECT * FROM categories", conn)
    seasons = pd.read_sql("SELECT * FROM seasons", conn)
    rankings = pd.read_sql("SELECT * FROM competitor_rankings", conn)
    conn.close()
    return competitions, categories, seasons, rankings

competitions, categories, seasons, rankings = load_data()

# --------------------------
# 3. Filters (Sidebar)
# --------------------------
st.sidebar.header("Filter Data")

years = sorted(seasons["year"].dropna().unique())
selected_year = st.sidebar.selectbox("Select Year", options=["All"] + [str(y) for y in years])

countries = sorted(rankings["country"].dropna().unique())
selected_country = st.sidebar.selectbox("Select Country", options=["All"] + countries)

# Filter Rankings
filtered_rankings = rankings.copy()
if selected_country != "All":
    filtered_rankings = filtered_rankings[filtered_rankings["country"] == selected_country]

# Filter Seasons
filtered_seasons = seasons.copy()
if selected_year != "All":
    filtered_seasons = filtered_seasons[filtered_seasons["year"] == int(selected_year)]

# --------------------------
# 4. KPIs
# --------------------------
st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Players", len(rankings))
col2.metric("Total Competitions", len(competitions))
col3.metric("Total Seasons", len(seasons))
col4.metric("Countries Represented", rankings["country"].nunique())

# --------------------------
# 5. Leaderboard - Top 10 Players
# --------------------------
st.subheader("Top 10 Players by Points")

top_players = (
    filtered_rankings.sort_values(by="points", ascending=False)
    .head(10)[["competitor_name", "points", "rank", "country"]]
)
st.dataframe(top_players)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_players, x="points", y="competitor_name", palette="Blues_d", ax=ax)
ax.set_title("Top 10 Players by Points")
st.pyplot(fig)

# --------------------------
# 6. Average Points by Country
# --------------------------
st.subheader("Average Points by Country")

country_points = (
    filtered_rankings.groupby("country")["points"].mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=country_points, x="points", y="country", palette="Greens_d", ax=ax)
ax.set_title("Top 10 Countries by Average Points")
st.pyplot(fig)

# --------------------------
# 7. Seasonal Growth Trend
# --------------------------
st.subheader("Seasonal Growth Trend")

season_growth = (
    filtered_seasons.groupby("year")["season_id"].count()
    .reset_index()
    .rename(columns={"season_id": "total_seasons"})
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=season_growth, x="year", y="total_seasons", marker="o", ax=ax)
ax.set_title("Number of Seasons Over Time")
st.pyplot(fig)

# --------------------------
# 8. Player Consistency Metric
# --------------------------
st.subheader("Player Consistency (Avg Points vs Range)")

consistency = (
    filtered_rankings.groupby("competitor_name")
    .agg(avg_points=("points", "mean"), point_range=("points", lambda x: x.max() - x.min()))
    .reset_index()
    .sort_values(by="avg_points", ascending=False)
    .head(20)
)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=consistency, x="avg_points", y="point_range", s=100, ax=ax)
ax.set_title("Player Consistency")
st.pyplot(fig)

# --------------------------
# 9. Download Section
# --------------------------
st.subheader("Download Query Results")
st.download_button(
    label="Download Top 10 Players CSV",
    data=top_players.to_csv(index=False),
    file_name="top_players.csv",
    mime="text/csv"
)

st.download_button(
    label="Download Country Points CSV",
    data=country_points.to_csv(index=False),
    file_name="country_points.csv",
    mime="text/csv"
)

st.success("Dashboard ready. Adjust filters on the left to explore insights interactively.")
