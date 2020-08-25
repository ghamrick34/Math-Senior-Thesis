import matplotlib.pyplot as plt
import numpy as np
import u_and_d
import fetch
from Hull_White_class import Node
from datetime import date

u = u_and_d.u()
d = u_and_d.d()

day_0 = Node(0, 0, fetch.close_data()[-5], 1)
day_1_u = Node(1, 1, day_0.price * u, 0.5)
day_1_d = Node(2, 1, day_0.price * d, -0.5)
day_2_uu = Node(3, 2, day_1_u.price * u, 0.25)
day_2_ud = Node(4, 2, day_1_u.price * d, 0.5)
day_2_dd = Node(5, 2, day_1_d.price * d, -0.25)
day_3_uuu = Node(6, 3, day_2_uu.price * u, 0.125)
day_3_uud = Node(7, 3, day_2_uu.price * d, 0.375)
day_3_udd = Node(8, 3, day_2_ud.price * d, -0.375)
day_3_ddd = Node(9, 3, day_2_dd.price * d, -0.125)
day_4_uuuu = Node(10, 4, day_3_uuu.price * u, 0.0625)
day_4_uuud = Node(11, 4, day_3_uuu.price * d, 0.25)
day_4_uudd = Node(12, 4, day_3_uud.price * d, 0.375)
day_4_uddd = Node(13, 4, day_3_udd.price * d, -0.25)
day_4_dddd = Node(14, 4, day_3_ddd.price * d, -0.0625)

tree = [day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd, day_3_uuu, day_3_uud, day_3_udd, day_3_ddd, day_4_uuuu, day_4_uuud, day_4_uudd, day_4_uddd, day_4_dddd]

fig,ax = plt.subplots()

day = [i.day for i in tree]
price = [i.price for i in tree]
scale = [1000*abs(i.probability) for i in tree]
colors = [abs(i.probability) for i in tree]
marker = 'D'

print(colors)

# plot the chart
ax.scatter(day,price, s=scale, c=colors, marker=marker)

# zip joins x and y coordinates in pairs
for x,y in zip(day,price):

    label = "{:.2f}".format(y)

    # this method is called for each point
    ax.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Real-life data
real_life_data_day = [0,1,2,3,4]
real_life_data_price = [(fetch.close_data()[i-5]) for i in range(5)]

ax.plot(real_life_data_day,real_life_data_price)


plt.xticks(np.arange(0,5,1))

stock = fetch.stock()
today = date.today()
d1 = today.strftime("%B %d, %Y")
ax.set(xlabel = 'Days since ' + d1, ylabel = 'Price ($)', title =  stock + ' Predicted Close Price Over Time')

fig.tight_layout()

plt.show()