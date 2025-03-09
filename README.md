# Sinacor Brokerage Statements Extractor

Sinacor data extractor pattern (brokerage statements)

### Setup

```shell
pip install -r requirements.txt
```

### How use it

**Input and Output CLI Mode**
```shell
# input
python3 main.py brokerage-statements.pdf

#output:

### Brokerage Statements Extractor ###

############# Extraction Report #############
(-) Liquidation Value: R$ 1.4
(-) Exchange Fees Value: R$ 0.28
(-) Total Costs: R$ 1.68
(!) Operation Total Value: R$ 5631.94
#############################################

Extraction completed. Filename: ./outputs/operation_20250309_172348.csv
```
**CSV Output**

```csv
Date,Operation type,Symbol,Quantity,Unity Price,Costs,Total Value,Raw Data
20/02/2025,C,ITRI11,17,68.8,0.35,1169.6,"B3 RV LISTADO C VISTA FII ITRI ITRI11 CI 17 68,80 1.169,60 D"
20/02/2025,C,ITRI11,1,68.79,0.02,68.79,"B3 RV LISTADO C VISTA FII ITRI ITRI11 CI # 1 68,79 68,79 D"
20/02/2025,C,ITRI11,2,68.78,0.04,137.56,"B3 RV LISTADO C VISTA FII ITRI ITRI11 CI # 2 68,78 137,56 D"
20/02/2025,C,PORD11,131,7.69,0.3,1007.39,"B3 RV LISTADO C VISTA FII POLO CRI PORD11 CI # 131 7,69 1.007,39 D"
20/02/2025,C,PORD11,4,7.69,0.01,30.76,"B3 RV LISTADO C VISTA FII POLO CRI PORD11 CI # 4 7,69 30,76 D"
20/02/2025,C,MOVI3,400,3.9,0.46,1560.0,"B3 RV LISTADO C VISTA MOVIDA ON NM 400 3,90 1.560,00 D"
```

### Supported Exchanges

- CLEAR CORRETORA - GRUPO XP (beta)