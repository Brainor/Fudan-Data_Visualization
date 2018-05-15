# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
import matplotlib.colors as color
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PolyCollection
from matplotlib import animation
import numpy as np
import pandas
#conda install -c conda-forge ffmpeg
gdp_data = pandas.read_csv('./Data/GDP_14nations.csv')
lons, lats = list(gdp_data['Longitude']), list(gdp_data['Latitude'])

GDP_map = Basemap(lon_0=10)
x, y = GDP_map(lons, lats)
fig = plt.figure(figsize=(14, 9))
ax = Axes3D(fig)

# ax.set_axis_off()
ax.azim = 280
ax.elev = 50
ax.dist = 10
min_gdp, max_gdp = 999999, 0
polys = []
for polygon in GDP_map.landpolygons:
	polys.append(polygon.get_coords())
lc = PolyCollection(polys, facecolor='white', alpha=1, closed=False)
ax.add_collection3d(lc)
ax.add_collection3d(GDP_map.drawcoastlines(color='black', linewidth=0.25))
ax.add_collection3d(GDP_map.drawcountries(color='black', linewidth=0.35))
# ax.add_collection3d(GDP_map.drawcountries(color='black', linewidth=0.35))


year_key = 0

colors=cm.tab20(color.Normalize(0,len(x))(range(len(x))))

def GDPAni(i):
	year = str(1965 + i)
	data = [i / 1e10 for i in gdp_data[year]]
#	colors = cm.tab20(color.Normalize(min(data), max(data))(data))
	# x, y = GDP_map(lons, lats)
	ax.bar3d(x, y, np.zeros(len(x)), 5, 5, data,alpha=0.5, color=colors, linewidth=0)
#	for ii,(xx,yy) in enumerate(zip(x,y)):
#		ax.text(xx,yy,data[ii]+100,'%2.0f'%data[ii],horizontalalignment='right',verticalalignment='center')
	global year_key
	if year == '2016':
		year_key = 1
	if not year_key:
		ax.set_xlabel("GDP of each Country (Year " +
					  str(i + 1965) + ")", fontsize=16)
	else:
		ax.set_xlabel("GDP of each Country (Year " +
					  str(2016) + ")", fontsize=16)
	return fig,

# ax.set_xlabel("Country", fontsize=14)
ani_gdp = animation.FuncAnimation(fig=fig, func=GDPAni, frames=2016 - 1965 + 1,
								  interval=1000, blit=False,repeat_delay=5000)

ax.set_zlabel("GDP (Billon $)", fontsize=14)
max_gdp=(gdp_data.iloc[:,3:]/1e10).max().max()
min_gdp=(gdp_data.iloc[:,3:]/1e10).min().min()

ax.set_zlim(min_gdp * 0.9, max_gdp * 1.1)
mywriter = animation.FFMpegWriter()
mywriter.fps=2
#mywriter.extra_args=['-vcodec', 'libx264']
#ani_gdp.save('basic_animation.mp4',writer=mywriter)

year=str(2016)
data = [i / 1e10 for i in gdp_data[year]]
ax.bar3d(x, y, np.zeros(len(x)), 5, 5, data,alpha=0, color=colors, linewidth=0)

for i,(xx,yy) in enumerate(zip(x,y)):
    ax.text(xx,yy,data[i]+100,'%2.0f'%data[i],horizontalalignment='right',verticalalignment='center',color='r')
plt.show()