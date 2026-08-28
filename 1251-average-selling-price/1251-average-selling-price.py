import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    # Join Prices with UnitsSold
    df = prices.merge(units_sold, on="product_id", how="left")
    
    # Keep only purchases within the price period
    df = df[
        (df["purchase_date"] >= df["start_date"]) &
        (df["purchase_date"] <= df["end_date"])
    ]
    
    # Calculate revenue
    df["revenue"] = df["price"] * df["units"]
    
    # Calculate average price for products having sales
    result = df.groupby("product_id").agg(
        total_revenue=("revenue", "sum"),
        total_units=("units", "sum")
    ).reset_index()
    
    result["average_price"] = (
        result["total_revenue"] / result["total_units"]
    ).round(2)
    
    # Add products that have no matching sales
    result = prices[["product_id"]].drop_duplicates().merge(
        result[["product_id", "average_price"]],
        on="product_id",
        how="left"
    )
    
    result["average_price"] = result["average_price"].fillna(0.00)
    
    return result