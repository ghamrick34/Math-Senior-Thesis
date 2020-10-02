import matplotlib.pyplot as plt
import numpy as np
import u_and_d_General as u_and_d
import fetch
from Hull_White_class import Node
import matplotlib.patches as mpatches
import nodes as n

# Predicted nodes
tree = [n.day_0, n.day_1_u, n.day_1_d, n.day_2_uu, n.day_2_ud, n.day_2_dd, n.day_3_uuu, n.day_3_uud, n.day_3_udd, n.day_3_ddd, n.day_4_uuuu, n.day_4_uuud, n.day_4_uudd, n.day_4_uddd, n.day_4_dddd]

# Real-life data
real_life_data_day = [0,1,2,3,4]
real_life_data_price = [(fetch.close_data()[i-5]) for i in range(5)]

# Day 1 error
day_1 = tree[1:3]
error_day_1 = min([abs(real_life_data_price[1]-day_1[i].price) for i in range(2)])/real_life_data_price[1]
#print(error_day_1)

# Day 2 error
day_2 = tree[3:6]
error_day_2 = min([abs(real_life_data_price[2]-day_2[i].price) for i in range(3)])/real_life_data_price[2]
#print(error_day_2)

# Day 3 error
day_3 = tree[6:10]
error_day_3 = min([abs(real_life_data_price[3]-day_3[i].price) for i in range(4)])/real_life_data_price[3]
#print(error_day_3)

# Day 4 error
day_4 = tree[10:15]
error_day_4 = min([abs(real_life_data_price[4]-day_4[i].price) for i in range(5)])/real_life_data_price[4]
#print(error_day_4)

# Error set

errors = [error_day_1, error_day_2, error_day_3, error_day_4]
total_error = sum(errors)
print(total_error)