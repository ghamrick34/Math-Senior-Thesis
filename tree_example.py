import matplotlib.pyplot as plt 
plt.xlim(0,1) 
plt.figtext(0.18,0.5,'S')
plt.figtext(0.6,0.5+0.2,'Su')
plt.figtext(0.6,0.5-0.2,'Sd')

plt.annotate('',xy=(0.6,0.5+0.25), xytext=(0.1,0.5), arrowprops=dict(facecolor='g',shrink=0.01))
plt.annotate('',xy=(0.6,0.5-0.25), xytext=(0.1,0.5), arrowprops=dict(facecolor='b',shrink=0.01))
plt.axis('off')
plt.show()