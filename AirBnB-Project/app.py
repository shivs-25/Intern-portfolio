
import os
import io
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans


NYC_LISTINGS_URL = "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-08-01/visualisations/listings.csv"

def ensure_default_listings(path="listings.csv"):
    if os.path.exists(path):
        return path
    # Try to download NYC latest snapshot referenced in README
    try:
        import requests
        r = requests.get(NYC_LISTINGS_URL, timeout=60)
        r.raise_for_status()
        with open(path, "wb") as fh:
            fh.write(r.content)
        return path
    except Exception:
        return None

st.set_page_config(page_title="Airbnb Data Analysis & Dashboard", layout="wide")

st.title("Airbnb Data Analysis & Interactive Dashboard")

st.markdown("""
**How to use this app**  
1) Use the filters in the sidebar to explore pricing, availability, and reviews.  
""")

# -----------------------------
# Helpers
# -----------------------------
@st.cache_data
def load_csv(uploaded_file_or_path):
    if uploaded_file_or_path is None:
        return None
    try:
        if hasattr(uploaded_file_or_path, "read"):
            df = pd.read_csv(uploaded_file_or_path, low_memory=False)
        else:
            df = pd.read_csv(uploaded_file_or_path, low_memory=False)
        return df
    except Exception as e:
        st.error(f"Failed to load CSV: {e}")
        return None

def coerce_price(series):
    try:
        return (
            series.astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(" ", "", regex=False)
            .str.extract(r'([0-9]*\.?[0-9]+)')[0]
            .astype(float)
        )
    except Exception:
        return pd.to_numeric(series, errors="coerce")

def try_parse_dates(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    return df

def basic_clean(df):
    df = df.copy()
    # Standardize column names
    df.columns = [c.strip() for c in df.columns]
    # Remove duplicates
    df = df.drop_duplicates()
    # Price
    if "price" in df.columns:
        df["price"] = coerce_price(df["price"])
    # Availability fields often numeric
    for c in ["availability_30", "availability_60", "availability_90", "availability_365",
              "minimum_nights", "maximum_nights", "calculated_host_listings_count",
              "number_of_reviews", "review_scores_rating"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    # Parse dates if present
    date_like = [c for c in df.columns if "date" in c.lower()]
    try_parse_dates(df, date_like)
    # Handle missing: fill essential categorical with "Unknown", numeric with median
    for c in df.columns:
        if df[c].dtype.kind in "biufc":
            if df[c].isna().mean() < 0.95:
                df[c] = df[c].fillna(df[c].median())
        else:
            df[c] = df[c].fillna("Unknown")
    return df

def safe_col(df, candidates, default=None):
    for c in candidates:
        if c in df.columns:
            return c
    return default

# -----------------------------
# Data inputs
# -----------------------------
default_path = ensure_default_listings("listings.csv")
if default_path and os.path.exists(default_path):
    st.info("Using listings.csv (auto-downloaded NYC dataset).")
    listings_df_raw = load_csv(default_path)
else:
    st.error("Could not load listings.csv. Please check your internet or download the file manually.")
    st.stop()

if listings_df_raw is None:
    st.warning("Could not load listings data. Please make sure the file is available.")
    st.stop()


# Clean
listings_df = basic_clean(listings_df_raw)

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")
neigh_col = safe_col(listings_df, ["neighbourhood_cleansed", "neighbourhood", "neighborhood"], None)
room_col  = safe_col(listings_df, ["room_type"], None)
price_col = safe_col(listings_df, ["price"], None)

if neigh_col:
    selected_neigh = st.sidebar.multiselect("Neighbourhood", options=sorted(listings_df[neigh_col].dropna().unique().tolist()))
else:
    selected_neigh = []

if room_col:
    selected_room = st.sidebar.multiselect("Room type", options=sorted(listings_df[room_col].dropna().unique().tolist()))
else:
    selected_room = []

if price_col:
    min_p, max_p = float(np.nanmin(listings_df[price_col])), float(np.nanmax(listings_df[price_col]))
    p_range = st.sidebar.slider("Price range", min_value=0.0, max_value=max(100.0, max_p), value=(min_p if np.isfinite(min_p) else 0.0, min(1000.0, max_p) if np.isfinite(max_p) else 1000.0))
else:
    p_range = (0.0, 1e9)

# Apply filters
df_f = listings_df.copy()
if neigh_col and selected_neigh:
    df_f = df_f[df_f[neigh_col].isin(selected_neigh)]
if room_col and selected_room:
    df_f = df_f[df_f[room_col].isin(selected_room)]
if price_col:
    df_f = df_f[(df_f[price_col] >= p_range[0]) & (df_f[price_col] <= p_range[1])]

st.subheader("Dataset Snapshot")
st.dataframe(df_f.head(50), use_container_width=True)

# -----------------------------
# KPIs
# -----------------------------
left, mid, right, more = st.columns(4)
with left:
    st.metric("Total Listings", len(df_f))
with mid:
    if price_col:
        st.metric("Average Price", f"{df_f[price_col].mean():.2f}")
    else:
        st.metric("Average Price", "N/A")
with right:
    rev_col = safe_col(df_f, ["number_of_reviews"], None)
    st.metric("Avg Reviews", f"{df_f[rev_col].mean():.2f}" if rev_col else "N/A")
with more:
    av_col = safe_col(df_f, ["availability_365"], None)
    st.metric("Avg Availability (days)", f"{df_f[av_col].mean():.1f}" if av_col else "N/A")

# -----------------------------
# Visualizations
# -----------------------------
st.header("Exploratory Analysis")

# Distribution of Price
if price_col:
    st.subheader("Price Distribution")
    fig, ax = plt.subplots()
    ax.hist(df_f[price_col].dropna(), bins=50)
    ax.set_xlabel("Price")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Listings by Neighbourhood
if neigh_col:
    st.subheader("Listings by Neighbourhood")
    topn = st.slider("Show top N neighbourhoods", 5, 30, 10)
    neigh_counts = df_f[neigh_col].value_counts().head(topn).reset_index()
    neigh_counts.columns = [neigh_col, "count"]
    fig_bar = px.bar(neigh_counts, x=neigh_col, y="count")
    st.plotly_chart(fig_bar, use_container_width=True)

# Room type impact on price
if room_col and price_col:
    st.subheader("Price by Room Type (Box Plot)")
    fig_box = px.box(df_f[[room_col, price_col]].dropna(), x=room_col, y=price_col)
    st.plotly_chart(fig_box, use_container_width=True)

# Price vs. Reviews
rev_col = safe_col(df_f, ["number_of_reviews"], None)
if price_col and rev_col:
    st.subheader("Price vs. Number of Reviews")
    fig_scatter = px.scatter(df_f, x=rev_col, y=price_col, opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Correlation heatmap (numeric)
st.subheader("Correlation Heatmap (Numerical)")
num_df = df_f.select_dtypes(include=[np.number]).copy()
if not num_df.empty:
    corr = num_df.corr(numeric_only=True)
    fig_heat = px.imshow(corr)
    st.plotly_chart(fig_heat, use_container_width=True)
else:
    st.info("No numeric columns available for correlation.")

# Optional: Simple price prediction
st.header("Price Prediction and Clustering")
with st.expander("Run Basic Linear Regression to predict price"):
    if price_col:
        feature_candidates = [c for c in ["minimum_nights", "maximum_nights",
                                          "availability_365", "number_of_reviews",
                                          "calculated_host_listings_count", "review_scores_rating"]
                              if c in df_f.columns]
        if feature_candidates:
            X = df_f[feature_candidates].fillna(0.0)
            y = df_f[price_col].fillna(df_f[price_col].median())
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            r2 = model.score(X_test, y_test)
            st.write(f"R² on hold-out set: {r2:.3f}")
            st.write("Coefficients:")
            coef_df = pd.DataFrame({"feature": feature_candidates, "coef": model.coef_})
            st.dataframe(coef_df)
        else:
            st.info("Not enough numeric features to train a model.")
    else:
        st.info("Price column is required.")

with st.expander("K-Means clustering on numeric features"):
    if not num_df.empty:
        k = st.slider("Number of clusters (k)", 2, 10, 3)
        km = KMeans(n_clusters=k, n_init="auto", random_state=42)
        fit_df = num_df.fillna(num_df.median(numeric_only=True))
        labels = km.fit_predict(fit_df)
        st.write("Cluster sizes:", pd.Series(labels).value_counts().to_dict())
        df_with_cluster = df_f.copy()
        df_with_cluster["cluster"] = labels
        st.dataframe(df_with_cluster[[neigh_col, room_col, price_col, "cluster"]].head(50) if neigh_col and room_col and price_col else df_with_cluster.head(50))
    else:
        st.info("No numeric columns available for clustering.")

# -----------------------------
# Downloads
# -----------------------------
st.header("Downloads")
clean_csv = df_f.copy()
csv_bytes = clean_csv.to_csv(index=False).encode("utf-8")
st.download_button("Download Filtered Data (CSV)", data=csv_bytes, file_name="filtered_listings.csv", mime="text/csv")

# Also allow downloading the cleaned full dataset (without filters)
clean_full = listings_df.copy().to_csv(index=False).encode("utf-8")
st.download_button("Download Cleaned Full Listings (CSV)", data=clean_full, file_name="cleaned_listings.csv", mime="text/csv")

st.success("Dashboard ready. Use the sidebar to filter and the headers to explore visuals.")
