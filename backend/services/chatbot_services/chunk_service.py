from services.chatbot_services.csv_loader import get_inventory_data


def row_to_chunk(row):

    chunk = f"""
Product ID: {row['Product ID']}
Product Name: {row['Product Name']}

Current Inventory: {row['Inventory Level']}
Predicted Sales: {row['Predicted Sales']}
Daily Sales: {row['Daily Sales']}

Days Left: {row['Days Left']}

Inventory Risk: {row['Risk']}

Recommended Order Quantity: {row['Recommended Order Quantity']}

Supplier: {row['Supplier Name']}
Supplier Lead Time: {row['Supplier Lead Time']} Days

Recommended Inventory Action: {row['Action']}
"""

    return chunk.strip()


def create_chunks(df):

    chunks = []

    for _, row in df.iterrows():
        chunks.append(row_to_chunk(row))

    return chunks


def get_inventory_chunks():

    df = get_inventory_data()

    return create_chunks(df)
