
import argparse, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def basic_clean(df):
    df = df.drop_duplicates().copy()
    if "price" in df.columns:
        df["price"] = coerce_price(df["price"])
    for c in df.columns:
        if df[c].dtype.kind in "biufc":
            if df[c].isna().mean() < 0.95:
                df[c] = df[c].fillna(df[c].median())
        else:
            df[c] = df[c].fillna("Unknown")
    return df

def main(listings_csv, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    df = pd.read_csv(listings_csv, low_memory=False)
    df = basic_clean(df)
    df.to_csv(os.path.join(out_dir, "cleaned_listings.csv"), index=False)

    # Summary stats
    desc = df.select_dtypes(include=[np.number]).describe()
    desc.to_csv(os.path.join(out_dir, "summary_stats.csv"))

    # Price distribution
    if "price" in df.columns:
        plt.figure()
        df["price"].dropna().plot(kind="hist", bins=50)
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "price_hist.png"), dpi=150)
        plt.close()

    # Listings per neighbourhood
    neigh_col = None
    for c in ["neighbourhood_cleansed", "neighbourhood", "neighborhood"]:
        if c in df.columns:
            neigh_col = c
            break
    if neigh_col:
        plt.figure()
        df[neigh_col].value_counts().head(20).plot(kind="bar")
        plt.ylabel("Listings")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "listings_by_neighbourhood.png"), dpi=150)
        plt.close()

    # Correlation heatmap
    num_df = df.select_dtypes(include=[np.number])
    if not num_df.empty:
        corr = num_df.corr(numeric_only=True)
        plt.figure()
        plt.imshow(corr, aspect="auto")
        plt.colorbar()
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, "correlation_heatmap.png"), dpi=150)
        plt.close()

    print("Analysis complete. Outputs saved to:", out_dir)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--listings_csv", required=True, help="Path to Inside Airbnb listings.csv")
    p.add_argument("--out_dir", default="outputs", help="Directory to save outputs")
    args = p.parse_args()
    main(args.listings_csv, args.out_dir)
