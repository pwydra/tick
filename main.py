from json import JSONEncoder

import portfolio
import quote
def entry(filename):
    investments = portfolio.load_portfolio_csv(filename)
    portfolio.print_portfolio(investments)
    quote.get_history(investments)
    info_dict = quote.get_info(investments)
    print(JSONEncoder().encode(info_dict))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entry('all.csv')
