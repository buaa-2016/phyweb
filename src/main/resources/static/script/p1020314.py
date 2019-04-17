# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from math import pi
from phylab import *
from handler import texdir
from jinja2 import Environment
import xml.dom.minidom
import sys
env = Environment(variable_start_string="||", variable_end_string="||")

def GetTheGraph1022(y_init, theta2):
	
	X_TIMES = 30
	Y_TIMES = 0.1 
	x_init = [X_TIMES * i for i in range(len(y_init))]
	X_SIZE = len(x_init) - 1
	Y_SIZE = int(max(y_init)*10) - int(min(y_init)*10) + 3
	Y_LOW = round(min(y_init) - 0.1, 1) - 0.1

	fig = plt.figure(figsize=(X_SIZE,Y_SIZE))
	ax=plt.gca()
	
	plt.xticks([10 * i for i in range(X_SIZE + 1)], x_init)
	plt.yticks([10 * i for i in range(Y_SIZE + 1)], [Y_LOW + Y_TIMES * i for i in range(Y_SIZE + 1)])
	for i in np.arange(0, X_SIZE * 10 + 1, 1):
		plt.plot([i,i], [0, Y_SIZE * 10], color = "red", linewidth = 0.75 if i % 10 == 0 else 0.25 if i % 5 == 0 else 0.10, linestyle = "-")
	for i in np.arange(0, Y_SIZE * 10 + 1, 1):
		plt.plot([0, X_SIZE * 10], [i,i], color = "red", linewidth = 0.75 if i % 10 == 0 else 0.25 if i % 5 == 0 else 0.10, linestyle = "-")

	display_y_init =map(lambda x: 10 * (x - Y_LOW) / Y_TIMES, y_init)
	
	base_line = np.polyfit(x_init, y_init, 3)
	line_func = np.poly1d(base_line)
	display_x = map(lambda x: 10 * x / X_TIMES, x_init)
	display_y = map(lambda x: 10 * (line_func(x) - Y_LOW) / Y_TIMES, x_init)
	
	ax.set_xlabel('t/s')
	ax.set_ylabel('$\Theta_2$/mV')
	plt.plot(display_x,display_y, linestyle='-', c="blue", linewidth=1)
	
	plt.plot(display_x, display_y_init, linestyle=' ', c="black", marker=Line2D.markers.get('x'), markersize=8)
	res = [-1, -1]
	for i in range(len(y_init)):
		if (theta2 - 1e-7 < y_init[i] and theta2 + 1e-7 > y_init[i] and i > 0 and i < len(y_init) - 1):
			res[0] = i - 1
			res[1] = i + 1
			break
	if (res[0] == -1):
		for i in range(1, len(y_init)):
			if (theta2 + 1e-7 > y_init[i] and theta2 - 1e-7 < y_init[i - 1]):
				res[0] = i - 1
				res[1] = i
	res_x = map(lambda t:x_init[t], res)
	res_y = map(lambda t:y_init[t], res)
	tangent_line = np.polyfit(res_x, res_y, 1)
	line_func = np.poly1d(tangent_line)
	plt.plot([0, X_SIZE * 10],[(line_func(0) - Y_LOW) / Y_TIMES * 10, (line_func(X_SIZE * X_TIMES) - Y_LOW) / Y_TIMES * 10], linestyle='-', c="gray", linewidth=1)
	fig.savefig(sys.argv[3] + ".png")

	return res_x, res_y


def readXml1020314(root):
	table = root.getElementsByTagName("table")[0]
	data = []
	# table_name = table.getAttribute("name")
	table_tr_list = table.getElementsByTagName("tr")
	for tr in table_tr_list:
		tr_td_list = tr.getElementsByTagName("td")
		data += [[]]
		for td in tr_td_list:
			if (td.firstChild):
				data[-1] += [float(td.firstChild.nodeValue)]
	return data

def coefficientOfThermalConductivity(theta1, theta2, mp, hp, dp, hb, db, theta, source):
	# theta1 	单位：mV
	# theta2 	单位：mV
	# mp		单位：g
	# hp		单位：mm
	# dp		单位：mm
	# hb		单位：mm
	# db		单位：mm
	# theta 	单位：mV
	c = 0.368 #constant 0.368 J/g*K
	ave_hp = sum(hp) / len(hp)
	ave_dp = sum(dp) / len(dp)
	ave_hb = sum(hb) / len(hb)
	ave_db = sum(db) / len(db)
	dt_t, dt_theta = GetTheGraph1022(theta, theta2)
	tt = (dt_theta[0] - dt_theta[1]) / (dt_t[1] - dt_t[0])
	k = mp * c * tt * (ave_dp + 4 * ave_hp) / (ave_dp + 2 * ave_hp) * ave_hb / (theta1 - theta2) * 2 / pi / ave_db**2 * 1e3
	ua_hp = Ua(hp, ave_hp, len(hp))	#mm
	ua_dp = Ua(dp, ave_dp, len(dp))	#mm
	ua_hb = Ua(hb, ave_hb, len(hb))	#mm
	ua_db = Ua(db, ave_db, len(db))	#mm
	ub = 0.02 / 3**0.5	#mm
	u_mp = 0.01 / 3**0.5	#g
	u_hp = (ua_hp**2 + ub**2) ** 0.5	#mm
	u_dp = (ua_dp**2 + ub**2) ** 0.5	#mm
	u_hb = (ua_hb**2 + ub**2) ** 0.5	#mm
	u_db = (ua_db**2 + ub**2) ** 0.5	#mm
	u_k_k = ((u_mp / mp) ** 2 + 
			 ((1 / (ave_dp + 4 * ave_hp) - 1 / (ave_dp + 2 * ave_hp)) * u_dp)**2 + 
			 ((4 / (ave_dp + 4 * ave_hp) - 2 / (ave_dp + 2 * ave_hp)) * u_hp)**2 + 
			 (u_hb / ave_hb)**2 + 
			 (2 * u_db / ave_db) ** 2) ** 0.5
	u_k = k * u_k_k
	final = BitAdapt(k, u_k)
	return env.from_string(source).render(
			theta1 = theta1, 
			theta2 = theta2, 
			mp = mp, 
			hp = hp, 
			dp = dp, 
			hb = hb, 
			db = db, 
			len_hp = len(hp), 
			len_dp = len(dp), 
			len_hb = len(hb), 
			len_db = len(db), 
			ave_hp = ToScience(ave_hp), 
			ave_dp = ToScience(ave_dp), 
			ave_hb = ToScience(ave_hb), 
			ave_db = ToScience(ave_db), 
			theta = theta, 
			len_theta = len(theta), 
			k = ToScience(k), 
			ua_hp = ToScience(ua_hp * 1e-3), 
			ua_dp = ToScience(ua_dp * 1e-3), 
			ua_hb = ToScience(ua_hb * 1e-3), 
			ua_db = ToScience(ua_db * 1e-3), 
			u_hp = ToScience(u_hp * 1e-3), 
			u_dp = ToScience(u_dp * 1e-3), 
			u_hb = ToScience(u_hb * 1e-3), 
			u_db = ToScience(u_db * 1e-3), 
			u_k_k = ToScience(u_k_k), 
			u_k = ToScience(u_k), 
			final = final,
			figurename = sys.argv[3]
			)

def handler(XML):
	file_object = open(texdir + "Handle1020314.tex","r")
	source = file_object.read().decode('utf-8', 'ignore')
	file_object.close()
	data = readXml1020314(XML)
	return coefficientOfThermalConductivity(data[0][0], data[0][1], data[0][2], data[1], data[2], data[3], data[4], data[5], source)

if __name__ == '__main__':
	scriptdir = 'D:/Apache24/htdocs/PhyLabs/Phylab/storage/app/script/'
	texdir = scriptdir + 'tex/'
	dom = xml.dom.minidom.parse(scriptdir + 'test/1020314test/1020314.xml')
	root = dom.documentElement
	sys.argv = ['', '', '', 'D:/Apache24/htdocs/tmp/1022']
	print handler(root)
