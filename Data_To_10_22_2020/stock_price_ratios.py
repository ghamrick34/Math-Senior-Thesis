import pandas

def stock_price_ratios(entry):
    ratios = []
    close_data = pandas.read_csv(entry + ".csv")['Close']
    for index in range(len(close_data)-1):
        ratios.append(close_data[index+1]/close_data[index])
    return ratios
