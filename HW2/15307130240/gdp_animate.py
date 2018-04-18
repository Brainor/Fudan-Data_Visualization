import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib import animation
mpl.style.use('default')
gdps = np.zeros((7, 2016 - 1960 + 1))
countries = []

with open('./data/GDP.csv') as gdp_file:
    gdp_file.readline()
    index = 0
    for line in gdp_file:
        line = line.strip().split(',')
        countries.append(line[0])
        gdps[index] = [float(i)/1e9 for i in line[1:]]
        index += 1

fig7, ani_ax_gdp = plt.subplots(1, 1, figsize=(9, 6))

country_index = [i for i in range(7)]
p7, = plt.plot(country_index, gdps[
               :, 0], marker='o', markersize=30, linestyle='None', color='red', alpha=.5)


def animate_gdp(i):
    p7.set_ydata(gdps[:, i])
    plt.title("GDP of each Country (Year " +
              str(i + 1960) + ")", fontsize=16)
    return p7,

ani_gdp = animation.FuncAnimation(fig=fig7, func=animate_gdp,
                                  frames=2016 - 1960 + 1, interval=200, blit=False)
ani_ax_gdp.set_xlabel("Country", fontsize=14)
ani_ax_gdp.set_ylabel("GDP (Billon $)", fontsize=14)
ani_ax_gdp.set_xticks(country_index)
ani_ax_gdp.set_xticklabels(["" + i for i in countries], fontsize=8)

lower = min([min(i) for i in gdps]) * 0.9
upper = max([max(i) for i in gdps]) * 1.1
ani_ax_gdp.set_ylim(lower, upper)
plt.show()
