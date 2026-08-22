from matplotlib import pyplot as plt

days = ['2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08']
prices = [729.77, 735.11, 755.98, 816.04, 880.02]

plt.plot(days, prices)
plt.title('NASDAQ: TSLA')
plt.xlabel("Date")
plt.ylabel('USD')
plt.show()

regions = ['New England', 'North-West', 'Middle East']
sales = [882703, 532648, 714406]

plt.pie(sales, labels=regions, autopct='%1.1f%%')
plt.title('Продажи по регионам')
plt.show()

plt.bar(regions, sales)
plt.xlabel("Регионы")
plt.ylabel("Продажи")
plt.title("Годовой объем продаж по регионам")
plt.show()
