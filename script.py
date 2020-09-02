import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]


n = 1  
t = 2 
d = 6 
w = 0.8 
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1)

n = 2  
t = 2 
d = 6
w = 0.8
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store2_x, sales2)

plt.show()
