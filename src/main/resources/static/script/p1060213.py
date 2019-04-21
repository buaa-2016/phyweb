# -*- coding: utf-8 -*-
#实验一、物距像距法测凸透镜焦距
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

def CollimatedConvex(exper,source):
    f = []
    sum_f = 0
    delta = 35.5
    for i in range(5):
        aver = (exper[i][1] + exper[i][2])/2
        exper[i].append(aver)
        temp_f = exper[i][0] - aver - delta
        sum_f += temp_f
        f.append(temp_f)
    average_f = sum_f / 5
    ua_f = Ua(f,average_f,len(f))
    ub_f = 0.5/sqrt(3)
    uf = sqrt(pow(ua_f,2) + pow(ub_f,2))
    final = BitAdapt(average_f,uf)
    RoundTwo(exper, 2)
    RoundOne(f,2)
    result = env.from_string(source).render(
        EXPER = exper,
        F = f,
        AVERAGE_F = round(average_f,2),
        UA_F = round(ua_f,2),
        UB_F = round(ub_f,2),
        UF = round(uf,2),
        DELTA = delta,
        FINAL = final
        )
    return result

def readXml1060213(root, source):
    exper = []
    table_tr_list = root.getElementsByTagName('table')[0].getElementsByTagName("tr")
    for tr in table_tr_list:
        tr_td_list = tr.getElementsByTagName("td")
        sub_exper  =[]
        for td in tr_td_list:
            sub_exper.append(float(td.firstChild.nodeValue))
        exper.append(sub_exper)

    #exper = [[1400,1315.2,1311.9],[1300.0,1213.9,1209.9],
    #     [1200.0,1116.1,1118.3],[1100.0,1014.8,1013.9],
    #     [1000.0,916.7,918.2]]
    source = CollimatedConvex(exper,source)

    return source

def handler(XML):
    file_object = open(texdir + "Handle1060213.tex","r")
    #将模板作为字符串存储在template文件中
    source = file_object.read().decode('utf-8', 'ignore')
    file_object.close()
    return readXml1060213(XML, source)

if __name__ == '__main__':
    scriptdir = 'D:/Apache24/htdocs/PhyLabs/Phylab/storage/app/script/'
    texdir = scriptdir + 'tex/'
    dom = xml.dom.minidom.parse(scriptdir + 'test/1060213test/1060213.xml')
    root = dom.documentElement
    print handler(root)