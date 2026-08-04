import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VISUALIZATION_DIR = os.path.join(BASE_DIR, "visualizations")

os.makedirs(VISUALIZATION_DIR, exist_ok=True)

# ---------------------------------------
# Load Dataset
# ---------------------------------------
def load_data():
    """
    Load the sales dataset from the data folder.
    """

    # Get the folder where main.py is located
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # Create full path to CSV
    file_path = os.path.join(current_folder, "data", "sales_data.csv")

    print("Current Folder :", current_folder)
    print("CSV Path       :", file_path)

    try:
        dataframe = pd.read_csv(file_path)
        print("\n✅ Dataset loaded successfully.\n")
        return dataframe

    except FileNotFoundError:
        print("\n❌ CSV file not found.")
        print("Expected location:")
        print(file_path)
        return None

    except Exception as e:
        print("\n❌ Error:", e)
        return None


# ----------------------------------------
# Clean Dataset
# ----------------------------------------
def clean_data(data):
    """
    Clean and prepare the dataset.
    """

    data = data.drop_duplicates()
    data = data.dropna()

    data["Date"] = pd.to_datetime(data["Date"])

    data["Month"] = data["Date"].dt.strftime("%B")

    data["Quantity"] = pd.to_numeric(data["Quantity"])

    data["Price"] = pd.to_numeric(data["Price"])

    data["Total_Sales"] = pd.to_numeric(data["Total_Sales"])

    print("✅ Data cleaned successfully.")

    return data


# ----------------------------------------
# Analyze Dataset
# ----------------------------------------
def analyze_data(data):

    print("\n" + "=" * 60)
    print("          E-COMMERCE SALES ANALYSIS")
    print("=" * 60)

    total_orders = len(data)

    total_revenue = data["Total_Sales"].sum()

    average_sale = data["Total_Sales"].mean()

    top_product = (
        data.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    regional_sales = (
        data.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    monthly_sales = (
        data.groupby("Month")["Total_Sales"]
        .sum()
        .reindex(month_order)
        .dropna()
    )

    print(f"\nTotal Orders : {total_orders}")
    print(f"Total Revenue : ₹{total_revenue:,.2f}")
    print(f"Average Sale : ₹{average_sale:,.2f}")

    print("\nTop Selling Products")
    print(top_product)

    print("\nRegional Sales")
    print(regional_sales)

    return top_product, regional_sales, monthly_sales


# ----------------------------------------
# Bar Chart
# ----------------------------------------
def plot_product_sales(top_product):

    plt.figure(figsize=(10,6))

    top_product.plot(kind="bar")

    plt.title("Product-wise Quantity Sold")

    plt.xlabel("Product")

    plt.ylabel("Quantity Sold")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(VISUALIZATION_DIR, "product_sales_bar.png"))

    plt.close()

    print("✅ Bar chart saved.")


# ----------------------------------------
# Line Chart
# ----------------------------------------
def plot_monthly_sales(monthly_sales):

    plt.figure(figsize=(10,6))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o",
        linewidth=2
    )

    plt.title("Monthly Sales Trend")

    plt.xlabel("Month")

    plt.ylabel("Total Sales (₹)")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(os.path.join(VISUALIZATION_DIR, "monthly_sales_line.png"))
    plt.close()

    print("✅ Line chart saved.")


# ----------------------------------------
# Pie Chart
# ----------------------------------------
def plot_region_sales(regional_sales):

    plt.figure(figsize=(8,8))

    regional_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.ylabel("")

    plt.title("Sales Distribution by Region")

    plt.tight_layout()

    plt.savefig(os.path.join(VISUALIZATION_DIR, "region_sales_pie.png"))

    plt.close()

    print("✅ Pie chart saved.")


# ----------------------------------------
# Generate Insights
# ----------------------------------------
def generate_insights(data):

    print("\n" + "=" * 60)
    print("INSIGHTS")
    print("=" * 60)

    highest_region = (
        data.groupby("Region")["Total_Sales"]
        .sum()
        .idxmax()
    )

    best_product = (
        data.groupby("Product")["Quantity"]
        .sum()
        .idxmax()
    )

    highest_sale = data["Total_Sales"].max()

    print(f"Highest Revenue Region : {highest_region}")

    print(f"Best Selling Product : {best_product}")

    print(f"Highest Single Sale : ₹{highest_sale:,.2f}")

    print("\nBusiness Insights")

    print("- The highest revenue comes from the best-performing region.")

    print("- The best-selling product has the highest quantity sold.")

    print("- Monthly sales trends help identify seasonal demand.")

    print("- Data visualization makes sales analysis easier.")


# ----------------------------------------
# Main Function
# ----------------------------------------

def main():


    # Load dataset
    data = load_data()

    if data is None:
        return

    # Clean dataset
    data = clean_data(data)

    # Analyze dataset
    top_product, regional_sales, monthly_sales = analyze_data(data)

    # Generate charts
    plot_product_sales(top_product)
    plot_monthly_sales(monthly_sales)
    plot_region_sales(regional_sales)

    # Generate insights
    generate_insights(data)

    print("\n" + "=" * 60)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("Charts saved inside the 'visualizations' folder.")
    print("=" * 60)


# ----------------------------------------
# Program Starts Here
# ----------------------------------------
if __name__ == "__main__":
    main()