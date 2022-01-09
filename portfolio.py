import csv

valid_cols = ['symbol', 'quantity_owned', 'purchase_price', 'cost_basis', 'purchase_date', 'tax_treatment']
# csv file is expected to have the following fields:
#   symbol           stock, bond or mutual fund symbol
#   quantity_owned   number of units owned
#   purchase_price   price at which units were purchase. If not specified and quanity and cost-basis are specified,
#                    this is calculated by dividing quanity into cost-basis
#   cost_basis       total amount paid for position (possibly less commission). If not specified and quantity and
#                    purchase price are, then calculated by multiplying quanity and purchase price.
#   purchase_date    date position was purchased. If omitted, position is assumed to be long-term if taxable
#   tax_treatment    one of: taxable (brokerage), deferred (IRA, 401k, 403b), tax-free (Roth IRA)
#
# some columns to think about for the future:
#   quantity_purchased    to keep track of splits
#   sell_date             this and the following two fields could track gain/loss/tax
#   sell_price
#   sell_quantity
def load_portfolio_csv(file_name) -> []:
    investments = []
    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        first = True
        for row in csv_reader:
            investment = {}
            if first:
                first = False
            else:
                symbol = row['symbol']
                qty = to_float(row['quantity_owned'])
                price = to_float(row['purchase_price'])
                basis = to_float(row['cost_basis'])
                if not price and basis and qty:
                    price = basis / qty
                if not basis and price and qty:
                    basis = price * qty
                investment['symbol'] = symbol
                investment['quantity_owned'] = qty
                investment['purchase_price'] = price
                investment['cost_basis'] = basis
                investments.append(investment)
        return investments

def print_portfolio(p: []):
    print(f'\tsymbol\t : .qty... \tprice \tbasis')
    for row in p:
        symbol = row['symbol']
        qty = to_float(row['quantity_owned'])
        price = to_float(row['purchase_price'])
        basis = to_float(row['cost_basis'])

        if basis and price:
            print(f'\t{symbol}\t : {qty:7.2f} \t{price:7.2f} \t{basis:10.2f}')
        else:
            if not basis:
                basis = 0
            if not price:
                price = 99999
            print(f'\t{symbol}\t : {qty:7.2f} \t{price:7.2f} \t{basis:10.2f}')

def is_float(n: str) -> bool:
    if n is None:
        return False
    try:
        float(n)
        return True
    except ValueError:
        return False

def to_float(s:str) -> float:
    if is_float(s):
        return float(s)
    else:
        return None