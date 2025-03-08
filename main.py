import pdfplumber
import re
import pandas as pd
import sys

def main():
    print("\n### Brokerage Statements Extractor ###\n")
    
    if len(sys.argv) < 2:
        print("Please provide the path to the PDF file as an argument.")
        sys.exit(1)
    
    filename = sys.argv[1]

    operations = []
    operation_total_value = None
    liquidation_value = None
    exchange_fees_value = None
    
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                # Getting operations
                operations = extract_operations(text)
                operation_total_value = extract_operation_total_value(text)
                liquidation_value = extract_liquidation_value(text)
                exchange_fees_value = extract_exchange_fees_value(text)
                costs = liquidation_value + exchange_fees_value
                split_operation_costs(operations, costs, operation_total_value)
                
    to_csv(operations)

    print("######### Report #########")
    print("Liquidation Value:", liquidation_value)
    print("Exchange Fees Value:", exchange_fees_value)
    print("Operation Total Value:", operation_total_value)
    print("###########################")

    print("\nExtraction completed. Check the 'outputs' folder for the CSV file.\n")

def extract_numeric_value(text, pattern, group = 1):
    match = re.compile(pattern).search(text)
    if match:
        return float(match.group(group).replace(".", "").replace(",", "."))
    return None

def extract_liquidation_value(text):
    return extract_numeric_value(text, r"Taxa de liquidação\s+([\d,.]+)")

def extract_exchange_fees_value(text):
    return extract_numeric_value(text, r"Emolumentos\s+([\d,.]+)")

def extract_operation_total_value(text):
    return extract_numeric_value(text, r"Valor das operações\s+([\d,.]+)")

def extract_operations(text):
    operations = []
    
    date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    order_pattern = re.compile(
        r"B3 RV LISTADO\s+(C|V)\s+VISTA\s+([A-Z0-9\s]+)\s+([A-Z0-9]+)\s+CI\s+#?\s*(\d+)\s+([\d,.]+)\s+([\d,.]+) D"
    )

    match_operation_date = date_pattern.search(text.replace("\n", " "))
    if match_operation_date:
        operation_date = match_operation_date.group(0)

    for match in order_pattern.finditer(text):
        operation_type = match.group(1)
        symbol = match.group(3).strip()
        quantity = int(match.group(4)) 
        unit_price = float(match.group(5).replace(".", "").replace(",", "."))
        value = float(match.group(6).replace(".", "").replace(",", "."))
        operations.append({
            "operation_date": operation_date,
            "operation_type": operation_type,
            "symbol": symbol,
            "quantity": quantity,
            "unity_price": unit_price,
            "total_value": value,
            "costs": 0
        })

    return operations

def split_operation_costs(operations, costs, operation_total_value):
    for o in operations:
        o["costs"] = round(costs * o["total_value"] / operation_total_value, 2)
    return operations

def to_csv(operations):
    records = []
    for operation in operations:
        records.append([
            operation["operation_date"],
            operation["operation_type"],
            operation["symbol"],
            operation["quantity"],
            operation["unity_price"],
            operation["costs"],
            operation["total_value"]
        ])

    print("Extracted Operations:\n", records, "\n") 
    
    df_operations = pd.DataFrame(records, columns=["Date", "Operation type", "Symbol", "Quantity", "Unity Price", "Costs", "Total Value"])
    df_operations.to_csv("./outputs/operations.csv", index=False)

main()