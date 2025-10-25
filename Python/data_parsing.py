import pdfplumber
import re
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# === CONFIGURATION ===
PDF_FOLDER = "Grocery Invoice pdfs"
DB_CONFIG = {
    "dbname": "Grocery Data DB",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# REGEX PATTERNS 
item_pattern = re.compile(
    r"^(?P<item_name>.+?)\s*Item\s(?P<item_id>\d+)\s*\$(?P<unit_price>\d+\.\d{2})\s*"
    r"(?P<qty_ordered>\d+)\s*(?P<qty_shipped>\d+)\s*(?P<status>\w+)\s*\$(?P<order_total>\d+\.\d{2})\s*\$(?P<invoice_total>\d+\.\d{2})",
    re.MULTILINE
)

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        return text

def parse_invoice_text(text):
    items = []
    for match in item_pattern.finditer(text):
        items.append(match.groupdict())
    return items

def categorize_item(item_name):
    item_name = item_name.lower()

    categories = {
    "Dairy & Refrigerated": [
        "Kirkland Signature Organic Greek Nonfat Yogurt, Plain, 3 lbs",
        "Chobani Blended Greek Yogurt, Vanilla, 40 oz",
        "Kirkland Signature Whole Milk, 1 Gallon",
        "Kirkland Signature Non Fat Milk, 1 Gallon",
        "Kirkland Signature 2% Reduced Fat Milk, 1 Gallon",
        "PHILADELPHIA Cream Cheese Spread, Original, 48 oz",
        "Cheswick Mild Cheddar & Monterey Jack Cheese, Shredded, 5 lbs",
        "Cascade Dairy Mexican Four Cheese Blend, Shredded, 5 lbs"
    ],

    "Meat & Protein": [
        "Kirkland Signature Lightly Breaded Chicken Breast Chunks, Boneless Skinless, 4 lbs",
        "Tyson Boneless Chicken Bites, Buffalo Style, 3.5 lbs",
        "Kirkland Signature Organic Ground Beef, 85% Lean 15% Fat, 4 lbs",
        "Kirkland Signature Fully-Cooked Bacon, Hickory Wood Smoked, 1 lb",
        "Case Sale Jumbo Halal Chicken Breast, Boneless, Skinless, 40 lbs"
    ],

    "Bakery & Grains": [
        "Thomas' Bagels, Everything, 12 ct",
        "Village Hearth Cottage White Bread, 24 oz, 2 ct",
        "La Banderita 10\" Flour Tortillas, 20 ct",
        "Quaker Instant Oatmeal, Variety Pack, 1.51 oz, 52 ct",
        "Kirkland Signature Ancient Grains Probiotic Granola, 35.3 oz"
    ],

    "Produce & Frozen Fruit": [
        "Kirkland Signature Three Berry Blend, 4 lbs",
        "Premium Strawberries, 2 lbs",
        "Premium Blueberries, 18 oz",
        "Raspberries, 12 oz",
        "Bananas, 3 lbs",
        "Avocados, 6 ct",
        "Baking Potatoes, 10 lbs"
    ],

    "Condiments, Sauces & Seasonings": [
        "Lawry's Coarse Ground Garlic Salt with Parsley, 33 oz",
        "Lawry's Seasoned Salt, 40 oz",
        "McCormick Cajun Seasoning, 18 oz",
        "McCormick Italian Seasoning, 6.25 oz",
        "McCormick Premium Taco Seasoning, 24 oz",
        "Kinder's Organic Seasoning, Garlic Butter, 12.2 oz",
        "Kinder's Organic Seasoning, Bourbon Steak, 12.4 oz",
        "Cholula Hot Sauce, Original, 12 fl oz, 2 ct",
        "Frank's RedHot Cayenne Pepper Sauce, Original, 1 Gallon",
        "Rao's Homemade Marinara Sauce, 28 oz, 2 ct",
        "Hidden Valley Ranch Homestyle Dressing and Topping, 40 fl oz, 2 ct",
        "Hellmann's Real Mayonnaise, 1 Gallon",
        "Sweet Baby Ray's Barbecue Sauce, 160 oz",
        "Sue Bee Pure Honey, Midwest Raw Unfiltered Honey, 80 oz"
    ],

    "Beverages": [
        "Bolthouse Farms 100% Orange Juice, 52 fl oz, 2 ct"
    ],

    "Snacks & Packaged Food": [
        "Famous Amos Cookies, Chocolate Chip, 2 oz, 42 ct",
        "Dot’s Homestyle Pretzels, Original Seasoned Pretzel Twists, 1 oz, 36 ct",
        "Skippy Creamy Peanut Butter, 48 oz, 2 ct"
    ],

    "Paper & Disposable Products": [
        "Dixie Ultra Paper Plate, 8-1/2\", 240 ct",
        "Dixie Ultra Paper Bowl, 20 oz, 135 ct",
        "Solo Plastic Knife, Heavyweight, White, 500 ct",
        "Solo Plastic Fork, Heavyweight, White, 500 ct",
        "Kirkland Signature Plastic Cold Cup, Red, 18 oz, 240 ct",
        "Kirkland Signature 2-Ply Paper Towels, White, 160 Create-A-Size Sheets, 12 ct",
        "Kirkland Signature Bath Tissue, 2-Ply, 4.5\" x 4\", 380 Sheets, 30 ct"
    ],

    "Cleaning & Household Supplies": [
        "Dial Antibacterial & Moisturizing Foaming Hand Wash + Aloe, Spring Water Scent, 7.5 fl oz, 4 ct",
        "Dawn Platinum Advanced Power Liquid Dish Detergent, Fresh Scent, 90 fl oz",
        "Scotch-Brite Stainless Steel Scrubber, 16 ct",
        "Kirkland Signature Outdoor Trash Bags, 20% PCR, Black, 50 Gallon, 70 ct"
    ]
    }

    for category, keywords in categories.items():
        for kw in keywords:
            if kw.lower() in item_name:
                return category
    return "Other"

#  Adds derived columns and converts types.
def clean_and_prepare(df, week_number):
    df["week"] = week_number
    df["unit_price"] = df["unit_price"].astype(float)
    df["qty_ordered"] = df["qty_ordered"].astype(int)
    df["qty_shipped"] = df["qty_shipped"].astype(int)
    df["order_total"] = df["order_total"].astype(float)
    df["invoice_total"] = df["invoice_total"].astype(float)
    df["category"] = df["item_name"].apply(categorize_item)
    return df

# Loads the data frame into a PostgreSQL table
def load_to_postgres(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    records = df.to_dict('records')
    columns = list(records[0].keys())
    values = [[r[c] for c in columns] for r in records]

    insert_query = f"INSERT INTO costco_orders ({', '.join(columns)}) VALUES %s"
    execute_values(cur, insert_query, values)
    conn.commit()

    cur.close()
    conn.close()

def main():
    all_data = []

    # Loop through all PDFs in folder
    for i, filename in enumerate(sorted(os.listdir(PDF_FOLDER)), start=1):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, filename)
            print(f"Processing {filename} as Week {i}...")
            text = extract_text_from_pdf(pdf_path)
            items = parse_invoice_text(text)

            if not items:
                print(f"No matches found in {filename}. Check formatting or regex.")
                continue

            df = pd.DataFrame(items)
            df = clean_and_prepare(df, i)
            all_data.append(df)

    if all_data:
        full_df = pd.concat(all_data, ignore_index=True)
        print(full_df.head(10))
        load_to_postgres(full_df)
        print("Data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    main()
