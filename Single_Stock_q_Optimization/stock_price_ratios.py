import fetch

def stock_price_ratios(entry):
    ratios = []
    close_data = fetch.close_data(entry)
    for index in range(len(close_data)-1):
        ratios.append(close_data[index+1]/close_data[index])
    return ratios
