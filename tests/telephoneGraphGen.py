import matplotlib.pyplot as plt
import numpy as np

discounts = [35, 35, 35, 30, 21, 20, 3, 16, 14, 14, 14, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12, 12, 11, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
prices_desc = [i / 100 for i in [10299900, 9429900, 9399900, 9300000, 9450000, 9648500, 8788000, 8559900, 8550000, 8250000, 8149900, 8139900, 7898900, 7799900, 7779900, 7722601, 7649900, 7600000, 7599900, 7579900, 7183099, 7175631, 7100000, 6999900, 6999900, 6949900, 6929900, 6900000, 6899900, 6649900, 6514200, 6509900, 6499900, 6399900, 6399900, 6398900]]
prices_asc = [i / 100 for i in [17500, 50000, 50000, 50000, 51400, 53400, 54900, 54900, 54900, 55000, 55900, 59700, 61900, 98000, 65000, 65000, 67900, 68900, 70900, 73300, 73300, 74900, 74900, 76000, 79700, 79900, 79900, 79900, 79900, 85000, 
85000, 89900, 89900, 94900, 94900, 95000]]
ratings = [4.7, 4.6, 4.7, 4.9, 4.6, 4.8, 4.6, 4.6, 4.5, 4.5, 4.7, 4.8, 4.9, 4.9, 5.0, 4.8, 5.0, 4.7, 4.6, 5.0, 4.8, 4.9, 4.8, 5.0, 5.0, 4.6, 4.9, 4.8, 4.9, 4.8, 4.9, 4.8, 4.7, 4.7, 4.5, 4.5]
reviews = [28763, 24392, 17499, 13221, 9658, 9536, 9245, 8818, 8812, 8341, 7943, 6836, 6823, 6715, 6553, 6480, 6446, 6256, 5589, 5546, 5419, 5292, 5151, 5119, 5024, 4936, 4478, 4475, 4451, 4386, 4158, 4080, 4074, 4029, 3960, 3955]

# Plotting discounts
plt.plot(discounts)
plt.xlabel('Index')
plt.ylabel('tDiscount')
plt.title('Telephone Discounts')
plt.show()

# Plotting prices in descending order
plt.plot(prices_desc)
plt.xlabel('Index')
plt.ylabel('Price')
plt.title('Telephone Prices (Descending Order)')
plt.show()

# Plotting prices in ascending order
plt.plot(prices_asc)
plt.xlabel('Index')
plt.ylabel('Price')
plt.title('Telephone Prices (Ascending Order)')
plt.show()

# Plotting ratings
plt.plot(ratings)
plt.xlabel('Index')
plt.ylabel('Rating')
plt.title('Computer Ratings')
plt.show()

# Plotting reviews
plt.plot(reviews)
plt.xlabel('Index')
plt.ylabel('Review')
plt.title('Telephone Reviews')
plt.show()