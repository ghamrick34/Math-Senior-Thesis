import matplotlib
import matplotlib.pyplot as plt
import fetch

close_data = fetch.close_data()
stock = fetch.stock()

# Plot the close price of the stock
fig,ax = plt.subplots()
ax.plot(close_data, color = 'indigo')


ax.set(xlabel = 'Year', ylabel = 'Price ($)', title =  stock + " Close Price Over Time")
ax.grid()


plt.show()