# -*- coding: utf-8 -*-
from math import sqrt
from math import pi
import phylab
from jinja2 import Environment
from handler import texdir
import xml.dom.minidom

#texdir = "./tex/"
env = Environment()

def readXml1010113(root):
	table_list = root.getElementsByTagName("table")
	table = table_list[0]
	data = []
	# table_name = table.getAttribute("name")
	table_tr_list = table.getElementsByTagName("tr")
	for tr in table_tr_list:
		tr_td_list = tr.getElementsByTagName("td")
		data += [map(lambda x: float(x.firstChild.nodeValue), tr_td_list)]
	return data

def SteelWire(m, C_plus, C_sub, D, L, H, b, source):
	# m为等差数列，一般从10到24    单位：kg
	# C     单位：cm
	# D     单位：mm
	# L     单位：cm
	# H     单位：cm
	# b     单位：cm
	C = []
	for i in range(0,len(C_plus),1):
		C.append((C_plus[i] + C_sub[i]) / 2)

	delta_C = []
	for i in range(4):
		delta_C.append(C[i+4] - C[i])

	ave_delta_C = sum(delta_C) / 4
	delta_C.append(round(ave_delta_C,2))

	ave_D = round(sum(D) / len(D), 3)
	D.append(ave_D)
	delta_m = m[4] - m[0];

	E = 16 * 9.8 * L * delta_m * H * pow(10,6) / (pi * pow(ave_D,2) * b * ave_delta_C)
	ua_delta_C = phylab.Ua(delta_C,ave_delta_C,4)#cm
	ub_delta_C = 0.05 / sqrt(3)#cm
	u_delta_C = sqrt(ua_delta_C**2 + ub_delta_C**2)#cm
	ua_D = phylab.Ua(D,ave_D,len(D)-1)#mm
	ub_D = 0.005 / sqrt(3)#mm
	u_D = sqrt(ua_D**2 + ub_D**2)#mm
	u_b = 0.02 / sqrt(3)#cm
	u_L = 0.3 / sqrt(3)#cm
	u_H = 0.5 / sqrt(3)#cm

	u_E_E = sqrt(pow(u_L / L,2)+pow(u_H / H,2)+pow(2 * u_D / ave_D,2)+pow(u_b / b,2)+pow(u_delta_C / ave_delta_C,2))
	u_E = u_E_E * E
	final = phylab.BitAdapt(E,u_E)
	return env.from_string(source).render(
			L = L,
			H = H,
			b = b,
			D = D[:-1],
			ave_D = ave_D,
			m = m,
			delta_m = delta_m, 
			C_plus = C_plus,
			C_sub = C_sub,
			C = C,
			ave_delta_C = ave_delta_C,
			E = phylab.ToScience(E),
			ua_D = phylab.ToScience(ua_D),
			u_D = phylab.ToScience(u_D),
			ua_C = phylab.ToScience(ua_delta_C),
			u_C = phylab.ToScience(u_delta_C),
			u_E_E = phylab.ToScience(u_E_E),
			u_E = phylab.ToScience(u_E),
			final = final
			)

def handler(XML):
	file_object = open(texdir + "Handle1010113.tex","r")
	#将模板作为字符串存储在template文件中
	source = file_object.read().decode('utf-8', 'ignore')
	file_object.close()
	data = readXml1010113(XML)
	return SteelWire(data[2], data[3], data[4], data[1], data[0][0], data[0][1], data[0][2], source)
	
if __name__ == '__main__':
	scriptdir = 'D:/Apache24/htdocs/PhyLabs/Phylab/storage/app/script/'
	texdir = scriptdir + 'tex/'
	dom = xml.dom.minidom.parse(scriptdir + 'test/1010113test/1010113.xml')
	root = dom.documentElement
	print handler(root)