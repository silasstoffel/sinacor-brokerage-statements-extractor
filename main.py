import pdfplumber
import re
import pandas as pd
import sys

from symbol import search_symbol
from datetime import datetime
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

    filename = to_csv(operations)

    print("############# Extraction Report #############")
    print("(-) Liquidation Value: R$", liquidation_value)
    print("(-) Exchange Fees Value: R$", exchange_fees_value)
    print("(-) Total Costs: R$", costs)
    print("(!) Operation Total Value: R$", operation_total_value)
    print("#############################################")

    print("\nExtraction completed. Filename:", filename, "\n")

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

def extract_operation_type(text):
    b3 = "B3 RV LISTADO"
    bovespa = "1-BOVESPA"

    operation_type = (text.replace(b3, "").replace(bovespa, "")).strip()[:1]

    if operation_type == "C":
        return "C"
    elif operation_type == "V":
        return "V"
    
    return "UNKNOWN"

def extract_operations(text):
    operations = []
    txt = re.sub(r"\s+", " ", text)
    date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    pattern = re.compile(r"(B3 RV LISTADO|1-BOVESPA) (.*?) (\d+\s+[\d,.]+\s+[\d,.]+ [DC])")

    match_operation_date = date_pattern.search(text.replace("\n", " "))
    if match_operation_date:
        operation_date = match_operation_date.group(0)

    matches = pattern.findall(txt)

    for match in matches:
        text_chunk = f"{match[0]} {match[1]}".strip()
        numbers_chunk = match[2].strip()
        raw_data = f"{text_chunk} {numbers_chunk}"
        values = numbers_chunk.split(" ")
        quantity = int(values[0])
        unit_price = float(values[1].replace(".", "").replace(",", "."))
        total_value = float(values[2].replace(".", "").replace(",", "."))
        #print("Raw Data:", raw_data)

        operations.append({
            "raw_data": raw_data, 
            "operation_date": operation_date,
            "operation_type": extract_operation_type(text_chunk),
            "symbol": search_symbol(text_chunk, 'CLEAR'),
            "quantity": quantity,
            "unity_price": unit_price,
            "total_value": total_value,
            "costs": 0
        })

    return operations

def split_operation_costs(operations, costs, operation_total_value):
    for o in operations:
        if costs > 0:
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
            operation["total_value"],
            operation["raw_data"]
        ])

    #print("Extracted Operations:\n", records, "\n") 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"./outputs/operation_{timestamp}.csv"
    df_operations = pd.DataFrame(records, columns=["Date", "Operation type", "Symbol", "Quantity", "Unity Price", "Costs", "Total Value", "Raw Data"])
    df_operations.to_csv(filename, index=False)

    return filename

main()