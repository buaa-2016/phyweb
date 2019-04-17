# -*- coding:utf-8 -*-
# 1060524 平行光管法测凸透镜焦距
"""
:param :
d_list_1 = []
d_list_2 = []
"""

import xml.dom.minidom
from math import sqrt
from jinja2 import Environment
from handler import texdir
from handler import scriptdir

f_1 = 0
u_f_1 = 0
d_list_1 = []  # 4 2 1 -1 -2 -4
d_list_2 = []  # 4 2 1 -1 -2 -4
average_d_list = []  # 4 2 1 -1 -2 -4
d_list = []  # 4 2 1
f_list = []  # 4 2 1
u_f_list = []  # 4 2 1

average_f = 0
u_f = 0
answer = []

D_LIST_1 = []
D_LIST_2 = []
AVERAGE_D_LIST = []
D_LIST = []
F_LIST = []
U_F_LIST = []
AVERAGE_F = ""
U_F = ""

# 定义模板
env = Environment(line_statement_prefix="#", variable_start_string="%%", variable_end_string="%%")


def handler(sublab_root):
    xmlReader(sublab_root)
    niconiconi()
    regulation()
    # file_object = open(texdir + "/Handle1060524.tex", "r")
    # latex = file_object.read().decode('utf-8', 'ignore')
    # return lexFiller(latex)


def xmlReader(sublab_root):
    global d_list_1, d_list_2
    sublab_table_list = sublab_root.getElementsByTagName("table")
    for table in sublab_table_list:
        table_tr_list = table.getElementsByTagName("tr")
        tr1 = table_tr_list[0]
        tr2 = table_tr_list[1]
        table_td_list = tr1.getElementsByTagName("td")
        for td in table_td_list:
            d_list_1.append(float(td.firstChild.nodeValue))
        table_td_list = tr2.getElementsByTagName("td")
        for td in table_td_list:
            d_list_2.append(float(td.firstChild.nodeValue))


def niconiconi():
    global d_list_1, d_list_2, average_d_list, d_list, f_list, u_f_list, average_f, u_f
    for i in range(6):
        average_d_list.append((d_list_1[i] + d_list_2[i]) / 2)
    for i in range(3):
        d_list.append(abs(average_d_list[0 + i] - average_d_list[5 - i]))
    k = [4, 2, 1]
    for i in range(3):
        f_list.append(d_list[i] / k[i] * 550)  # mm
    u_b = 0.005 / sqrt(3)
    for i in range(3):
        u_f_list.append(u_b / k[i] * 550)  # mm
    temp1 = 0  # sum(fi/u^2(fi))
    temp2 = 0  # sum(1/u^2(fi))
    for i in range(3):
        temp1 += f_list[i]/(u_f_list[i]*u_f_list[i])
        temp2 += 1/(u_f_list[i]*u_f_list[i])
    average_f = temp1/temp2
    u_f = sqrt(1/temp2)


def regulation():
    global d_list_1, d_list_2, average_d_list, d_list, f_list, u_f_list, average_f, u_f
    global D_LIST_1, D_LIST_2, AVERAGE_D_LIST, D_LIST, F_LIST, U_F_LIST, AVERAGE_F, U_F, answer
    for i in range(6):
        D_LIST_1.append(toScience(d_list_1[i]))
    for i in range(6):
        D_LIST_2.append(toScience(d_list_2[i]))
    for i in range(3):
        AVERAGE_D_LIST.append(toScience(average_d_list[i]))
    for i in range(3):
        D_LIST.append(toScience(d_list[i]))
    for i in range(3):
        F_LIST.append(toScience(f_list[i]))
    for i in range(3):
        U_F_LIST.append(toScience(u_f_list[i]))
    bitAdapt(average_f, u_f, 1, -3)
    AVERAGE_F = answer[0]
    U_F = answer[1]
    pass


def lexFiller(source):
    result = env.from_string(source).render()
    return result


# a类不确定度计算
def Ua(x, aver, k):
    sumx = 0
    for i in range(k):
        sumx += (x[i] - aver) ** 2
    return sqrt(sumx / (k * (k - 1)))


# 规约最终结果，进行有效位数限定
def bitAdapt(x, u_x, up, low):
    global answer
    answer = [0, 0, 0]
    maxu = 10 ** up
    minu = 10 ** low
    if u_x > maxu:
        print ("误差过大")
        return
    if u_x < minu:
        print ("误差过小")
        return
    for i in range(low, up):
        if 10 ** i < u_x < 10 ** (i + 1):
            break
    if u_x > (10 ** (i + 1) - 10 ** i):
        bit = i + 1
        u_x = 10 ** bit
    else:
        bit = i
        u_x += 10 ** bit
    if int(x / (10 ** (bit - 1))) % 10 > 5:
        x += 10 ** bit
    elif int(x / (10 ** (bit - 1))) % 10 == 5 and int(x / (10 ** bit)) % 2 == 1:
        x += 10 ** bit
    if bit < 0:
        answer[0] = str(int(x / (10 ** bit)) * (10 ** bit))[0:len(str(10 ** bit)) + len(str(int(x))) - 1]
        answer[1] = str(int(u_x / (10 ** bit)) * (10 ** bit))[0:len(str(10 ** bit))]
        answer[2] = 0
    else:
        answer[0] = str(int(x / (10 ** bit)))
        answer[1] = str(int(u_x / (10 ** bit)))
        answer[2] = bit
    return


def toScience(number):
    tempstr = format(number, '.5g')
    if 'e' in tempstr:
        index_str = tempstr.split('e')
        return index_str[0] + '{\\times}10^{' + str(int(index_str[1])) + '}'
    else:
        return tempstr


if __name__ == '__main__':
    dom = xml.dom.minidom.parse(scriptdir+'test/1060524test/1060524.xml')
    root = dom.documentElement
    sublab_list = root.getElementsByTagName('sublab')
    for sublab in sublab_list:
        sublab_status = sublab.getAttribute("status")
        sublab_id = sublab.getAttribute("id")
        if (sublab_status == 'true') & (sublab_id == '10622'):
            handler(sublab)
    print(answer)
    print(D_LIST)
    print(d_list)