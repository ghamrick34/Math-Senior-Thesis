import numpy as np
import u_and_d_General as u_and_d
import fetch
from Hull_White_class import Node

u = u_and_d.u()
d = u_and_d.d()

day_0 = Node(0, 0, fetch.close_data()[-5], 1)
day_1_u = Node(1, 1, day_0.price * u, u)
day_1_d = Node(2, 1, day_0.price * d, d)
day_2_uu = Node(3, 2, day_1_u.price * u, u*u)
day_2_ud = Node(4, 2, day_1_u.price * d, u*d)
day_2_dd = Node(5, 2, day_1_d.price * d, d*d)
day_3_uuu = Node(6, 3, day_2_uu.price * u, u*u*u)
day_3_uud = Node(7, 3, day_2_uu.price * d, u*u*d)
day_3_udd = Node(8, 3, day_2_ud.price * d, u*d*d)
day_3_ddd = Node(9, 3, day_2_dd.price * d, d*d*d)
day_4_uuuu = Node(10, 4, day_3_uuu.price * u, u*u*u*u)
day_4_uuud = Node(11, 4, day_3_uuu.price * d, u*u*u*d)
day_4_uudd = Node(12, 4, day_3_uud.price * d, u*u*d*d)
day_4_uddd = Node(13, 4, day_3_udd.price * d, u*d*d*d)
day_4_dddd = Node(14, 4, day_3_ddd.price * d, d*d*d*d)
