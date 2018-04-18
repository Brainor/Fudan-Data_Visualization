from matplotlib import animation
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.style.use('default')
world_cup_predictions_path = './data/world-cup-predictions/'
path_dir = os.listdir(world_cup_predictions_path)
world_cup_predictions = []
for file_name in path_dir:
    info = pd.read_csv(world_cup_predictions_path + file_name)
    world_cup_predictions += [info]
# world_cup_predictions
countries = world_cup_predictions[0].country
countries.head()
countries = list(countries)
countries_predictions = {}
for item in world_cup_predictions:
    for cty in countries:
        try:
            countries_predictions[cty].append(
                float(item[item.country == cty].win))
        except KeyError:
            countries_predictions[cty] = []
            countries_predictions[cty].append(
                float(item[item.country == cty].win))

predictions = np.zeros((32, 84))
index = 0
for country in countries_predictions:
    predictions[index][:] = countries_predictions[country]
#     predictions[index] = countries_predictions[country]
    index += 1

fig6, ani_ax = plt.subplots(1, 1, figsize=(12, 5))

country_index = [i for i in range(32)]
p6, = plt.plot(country_index, predictions[:, 0], marker='o', linestyle='None')


def animate(i):
    p6.set_ydata(predictions[:, i])
    plt.title("The probability of winning the world cup (No." +
              str(i + 1) + ")", fontsize=16)
    return p6,
ani = animation.FuncAnimation(
    fig=fig6, func=animate, frames=84, interval=100, blit=False)
ani_ax.set_xlabel("Country", color='c')
ani_ax.set_ylabel("Probability", color='c')
ani_ax.set_ylim(0, 0.65)
ani_ax.set_xticks(country_index)
ani_ax.set_xticklabels(["   " + i for i in countries], fontsize=8)
plt.xticks(rotation=90)
plt.show()
