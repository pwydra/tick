import portfolio

def entry(filename):
    investments = portfolio.load_portfolio_csv(filename)
    portfolio.print_portfolio(investments)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entry('test.csv')
