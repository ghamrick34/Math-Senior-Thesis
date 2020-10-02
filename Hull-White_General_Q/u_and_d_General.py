import stock_price_ratios
import statistics as stat
import math

stock_price_ratios = stock_price_ratios.stock_price_ratios()

sample_mean = stat.mean(stock_price_ratios)

sample_standard_deviation = stat.stdev(stock_price_ratios)


#q = 0.5
q = float(input('Enter value for q: '))

def u():
    return sample_mean + math.sqrt((1-q)/q) * sample_standard_deviation
# print("U = " + str(u()))

def d():
    return sample_mean - math.sqrt(q/(1-q)) * sample_standard_deviation
# print("D = " + str(d()))
