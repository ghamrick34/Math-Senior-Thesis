import numpy as np
import u_and_d_General as u_and_d
import fetch
from Hull_White_class import Node
from tree_class import tree

def gen_tree(q, entry):
    u = u_and_d.u(q, entry)
    d = u_and_d.d(q, entry)
    day_0 = Node(0, 0, fetch.close_data(entry)[-5], 1)
    day_1_u = Node(1, 1, day_0.price * u, q)
    day_1_d = Node(2, 1, day_0.price * d, (1-q))
    day_2_uu = Node(3, 2, day_1_u.price * u, q*q)
    day_2_ud = Node(4, 2, day_1_u.price * d, q*(1-q))
    day_2_dd = Node(5, 2, day_1_d.price * d, (1-q)*(1-q))
    day_3_uuu = Node(6, 3, day_2_uu.price * u, q*q*q)
    day_3_uud = Node(7, 3, day_2_uu.price * d, q*q*(1-q))
    day_3_udd = Node(8, 3, day_2_ud.price * d, q*(1-q)*(1-q))
    day_3_ddd = Node(9, 3, day_2_dd.price * d, (1-q)*(1-q)*(1-q))
    day_4_uuuu = Node(10, 4, day_3_uuu.price * u, q*q*q*q)
    day_4_uuud = Node(11, 4, day_3_uuu.price * d, q*q*q*(1-q))
    day_4_uudd = Node(12, 4, day_3_uud.price * d, q*q*(1-q)*(1-q))
    day_4_uddd = Node(13, 4, day_3_udd.price * d, q*(1-q)*(1-q)*(1-q))
    day_4_dddd = Node(14, 4, day_3_ddd.price * d, (1-q)*(1-q)*(1-q)*(1-q))
    
    nodes = tree(day_0, day_1_u, day_1_d, day_2_uu, day_2_ud, day_2_dd, day_3_uuu, day_3_uud, day_3_udd, day_3_ddd, day_4_uuuu, day_4_uuud, day_4_uudd, day_4_uddd, day_4_dddd)

    return nodes



