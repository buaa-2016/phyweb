# -*- coding: utf-8 -*-
# 实验一、物距像距法测凸透镜焦距
'''
input:
    exper_1 = []    三个实验情况，每一个都是一个二维列表[光源，光屏，凸透镜1，凸透镜2]
    exper_2 = []    运算过程中会在末尾添加一个凸透镜的均值
    exper_3 = []
output:
    物距u = []  像距v = []
    焦距f = []
'''
import xml.dom.minidom
from jinja2 import Environment
from handler import texdir
from phylab import *

env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


def Ua(x, aver):
    sumx = 0
    k = len(x)
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# calculate the average of two Convex and add into exper
def Average(exper):
    for i in range(3):
        aver = (exper[i][2] + exper[i][3]) / 2
        exper[i].append(aver)


def ObjectImage(exper_convex, exper_concave, source):
    u_convex, v_convex, f_convex = [], [], []
    delta = 35.5
    for exper in exper_convex:
        Average(exper)
        temp_u = []
        temp_v = []
        temp_f = []
        sum_f = 0
        for j in range(3):
            x = abs(exper[j][4] - exper[j][0]) - delta
            temp_u.append(x)
            y = abs(exper[j][1] - exper[j][4])
            temp_v.append(y)
            z = x * y / (x + y)
            sum_f += z
            temp_f.append(z)
        temp_f.append(sum_f / 3)
        u_convex.append(temp_u)
        v_convex.append(temp_v)
        f_convex.append(temp_f)
    average_f_convex = 0
    for i in range(3):
        average_f_convex += f_convex[i][3]
    average_f_convex /= 3

    map(RoundTwo, exper_convex)
    RoundTwo(u_convex)
    RoundTwo(v_convex)
    RoundTwo(f_convex)

    u_concave, v_concave, f_concave = [], [], []
    sum_f = 0
    for i in range(3):
        aver = (exper_concave[i][1] + exper_concave[i][2]) / 2
        exper_concave[i].append(aver)
        temp_u = exper_concave[i][0] - aver
        u_concave.append(temp_u)
        temp_v = abs(exper_concave[i][3] - aver)
        v_concave.append(temp_v)
        temp_f = temp_u * temp_v / (temp_u + temp_v)
        sum_f += temp_f
        f_concave.append(temp_f)
    average_f_concave = sum_f / 3
    RoundTwo(exper_concave)
    RoundOne(f_concave, 2)
    RoundOne(u_concave, 2)
    RoundOne(v_concave, 2)

    result = env.from_string(source).render(
        EXPER_1=exper_convex[0],
        EXPER_2=exper_convex[1],
        EXPER_3=exper_convex[2],
        U_Convex=u_convex,
        V_Convex=v_convex,
        F_Convex=f_convex,
        Average_F_Convex=round(average_f_convex, 2),
        EXPER_Concave=exper_concave,
        F_Concave=f_concave,
        U_Concave=u_concave,
        V_Concave=v_concave,
        AVERAGE_F_Concave=round(average_f_concave, 2)
    )

    return result


def ReadXml1060111(XML, source):
    exper_1 = []
    exper_2 = []
    exper_3 = []
    table_list = XML.getElementsByTagName("table")
    table_tr_list = table_list[0].getElementsByTagName("tr")
    for tr in table_tr_list:
        index = int(tr.getAttribute("index"))
        tr_td_list = tr.getElementsByTagName("td")
        if (index >= 1) & (index <= 3):
            sub_exper_1 = []
            for td in tr_td_list:
                sub_exper_1.append(float(td.firstChild.nodeValue))
            exper_1.append(sub_exper_1)
        elif (index >= 4) & (index <= 6):
            sub_exper_2 = []
            for td in tr_td_list:
                sub_exper_2.append(float(td.firstChild.nodeValue))
            exper_2.append(sub_exper_2)
        elif (index >= 7) & (index <= 9):
            sub_exper_3 = []
            for td in tr_td_list:
                sub_exper_3.append(float(td.firstChild.nodeValue))
            exper_3.append(sub_exper_3)

    # exper_1 = [[1400.0,469.2,1011.5,1014.8],
    #       [1400,492.3,1001.8,1004.6],[1400.0,426.1,1040.3,1037.8]]
    # exper_2 = [[1400.0,507.1,934.1,936.9],
    #       [1400.0,531.2,947.8,947.6],[1400.0,539.8,952.9,954.1]]
    # exper_3 = [[1400.0,410.5,716.9,715.4],
    #       [1400.0,397.1,712.8,711.0],[1400.0,370.4,674.9,672.6]]
    exper = []
    table_tr_list = table_list[1].getElementsByTagName("tr")
    for tr in table_tr_list:
        tr_td_list = tr.getElementsByTagName("td")
        sub_exper = []
        for td in tr_td_list:
            sub_exper.append(float(td.firstChild.nodeValue))
        exper.append(sub_exper)

    # exper = [[949.1,990.3,988.8,808.1],
    #     [950.8,989.9,986.2,841.7],[949.8,987.1,987.9,834.5]]
    source = ObjectImage([exper_1, exper_2, exper_3], exper, source)

    return source


def handler(XML):
    file_object = open(texdir + "Handle1060111.tex", "r")
    # 将模板作为字符串存储在template文件中
    source = file_object.read().decode('utf-8', 'ignore')
    file_object.close()
    return ReadXml1060111(XML, source)


if __name__ == '__main__':
    scriptdir = 'D:/Apache24/htdocs/PhyLabs/Phylab/storage/app/script/'
    texdir = scriptdir + 'tex/'
    dom = xml.dom.minidom.parse(scriptdir + 'test/1060111test/1060111.xml')
    root = dom.documentElement
    print handler(root)
