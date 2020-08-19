import matplotlib.pyplot as plt
import numpy as np
import u_and_d
import fetch
from Hull_White_class import Node

u = u_and_d.u()
d = u_and_d.d()

day_0 = Node(0, 0, fetch.close_data()[-2], 1)
day_1_u = Node(1, 1, day_0.price * u, 0.5)
day_1_d = Node(2, 1, day_0.price * d, 0.5)
day_2_uu = Node(3, 2, day_1_u.price * u, 0.25)
day_2_ud = Node(4, 2, day_1_u.price * d, 0.5)
day_2_dd = Node(5, 2, day_1_d.price * d, 0.25)

tree = [day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd]

day = [(int(i.day)) for i in tree]
price = [(float(i.price)) for i in tree]


# plot the chart
plt.scatter(day,price)

# zip joins x and y coordinates in pairs
for x,y in zip(day,price):

    label = "{:.2f}".format(y)

    # this method is called for each point
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,3,1))

plt.show()