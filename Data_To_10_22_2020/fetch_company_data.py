import fetch
import pandas as pd

renewable = ["run","fslr","cwen","nee","vslr","tsla","plug"]
fossil = ["xom","bp","cvx","rydaf","cop"]

for stock in renewable:
    fetch.close_data(stock).to_csv(stock+'.csv')